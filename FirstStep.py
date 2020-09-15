# file management
import glob
#content encryption
import os
from cryptography.fernet import Fernet
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#hashing passwords
import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def encryptContent(passw, salt, content):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passw.encode('UTF-8')))
    f = Fernet(key)
    print('encrypting data...')
    token = f.encrypt(bytes(content.encode('UTF-8')))
    print('data encrypted successfully!')
    return token

def decryptContent(passw, salt, content):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    print('decrypting data...')
    key = base64.urlsafe_b64encode(kdf.derive(passw.encode('UTF-8')))
    f = Fernet(key)
    decrypted = f.decrypt(content)
    print('data decrypted successfully!')
    return decrypted

def getSalt():
    with open('key.key', 'rb') as file:
        return file.read()


#removes a text file from the project directory
def removeFile(fileName):
        os.remove(f'{fileName}.txt')
        print("removed")

# returns a list of text files in the project directory
def getFilesList():
    files = glob.glob("*.txt")
    i = 0
    return files


# get text from user
def getInput(stopWord):
    text = ""
    while True:
        line = input()
        if line.strip() == stopWord:
            break
        text += '\n' + line
    return text

# append to file
# returns the number of chars written to file
def writeToFile(fileName, text):
    with open(f'{fileName}.txt', 'wb') as f:
        a = f.write(text)
        f.close()
    return a


# read from file
def readFromFile(fileName):
    text = ''
    with open(f'{fileName}.txt', 'rb') as f:
        text = f.read()
        f.close()
    return text

def loginAuth():
    authorized = False
    hashedPassw = readFromFile('login')
    i = 1
    while not authorized:
        if i > 4:
            quit()
        passw = input(f"{5-i} attempts remaining, enter password: ")
        i += 1
        authorized = check_password(hashedPassw, passw)
    print('authorized!!')
    return passw


userPassw = 'noam'
salt = getSalt()
encryptedContent = encryptContent(userPassw, salt, 'hello world')
print(writeToFile('file1', encryptedContent))
fromFile = readFromFile('file1')
print(f'from file: {fromFile}')
decryptedContent = decryptContent(userPassw, salt, fromFile)
print(decryptedContent)



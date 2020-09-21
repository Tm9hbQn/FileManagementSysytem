import arc4 as ARC4
import glob as fileList
import os
from passlib.hash import pbkdf2_sha256

###########
#
# אבטחה - האשינג, הצפנה ופענוח, קבלת וכתיבת האש לקובץ
#
###########

###########
#
# פונקציות הצפנה ופענוח
#
###########
def encrypt_content(content, key):
    arc4 = ARC4.ARC4(key)
    cipher = arc4.encrypt(content)
    return cipher


def decrypt_content(cipherred_content, key):
    arc4 = ARC4.ARC4(key)
    decrypted = arc4.decrypt(cipherred_content)
    return decrypted

###########
#
# פונקציות גיבוב ובדיקה
#
###########
def hash_password(key):
    return pbkdf2_sha256.hash(key)

def check_password(key, hashedkey):
    return pbkdf2_sha256.verify(key, hashedkey)

###########
#
# שמירת והוצאת ההאש
#
###########
def getHashedPass():
    with open('login.txt', 'rb') as f:
        hashed = f.readline()
        f.close()
        return hashed

def writeHashedPass(hashed):
    with open('login.txt', 'wb') as f:
        bytesUsed = f.write(hashed.encode('UTF-8'))
        f.close()
        return bytesUsed

###########
#
# פונקציות לניהול קבצים
#
###########
###########
#
# מחיקת קובץ
#
###########

def removeFile():
    file_name = input('what is the name of the file you wish to remove?: ')
    os.remove(f'{file_name}.txt')
    print("removed")

###########
#
# כתיבת קובץ חדש
# לפני הצפנה
###########
def writeCotnentToFile(fileName, plain_content, key):
    encryptedContent = encrypt_content(plain_content, key)
    with open(f'{fileName}.txt', 'wb') as f:
        bytes_used = f.write(encryptedContent)
        return bytes_used

###########
#
# קריאת ופענוח קובץ
#
###########
def readContentFromFile(fileName, key):
    with open(f'{fileName}.txt', 'rb') as f:
        encryptedContent = f.read()
        f.close()
    plain_content = decrypt_content(encryptedContent, key)
    return plain_content.decode()
###########
#
# מחזיר את רשימת קבצי הטקסט בתיקיית הפרויקט
#
###########
def getFilesList():
    files = fileList.glob('*.txt')
    return files


###########
#
# פונקציות תקשורת עם המשתמש
#
######################
#
# כתיבת קובץ חדש
#
###########
def createNewFile(key):
    file_name = input('enter file name: ')
    plain_content = ""
    while True:
        line = input()
        if line.strip() == '1!1':
            break
        plain_content += '\n' + line
    return writeCotnentToFile(file_name, plain_content, key)

###########
#
# מקבל את המפתח ומבקש מהמשתמש את שם הקובץ - ומדפיס אותו
#
###########
def readFile(key):
    f_name = input('enter the name of the file you want to read: ')
    plain_content = readContentFromFile(f_name, key)
    return plain_content
###########
#
# מקבל את המפתח ומבקש מהמשתמש את שם הקובץ - ומדפיס אותו
#
###########
def nav_menu(key):
    userChoice = 0
    message = f'\n\nWelcome! this is the main menu. press the number of the desired action\n' \
              f'1 - Write a new file\n' \
              f'2 - Get files list\n' \
              f'3 - Read a file\n' \
              f'4 - Delete a file\n' \
              f'5 - Exit program'

    while userChoice != 5:
        print(message)
        userChoice = int(input('Desired action: '))

        if userChoice == 1:
            x = createNewFile(key)
            print('success') if x > 1 else print('failure')
        if userChoice == 2:
            print('files list in program: ')
            for file in getFilesList():
                print(file)
        if userChoice == 3:
            print('your desired file: ')
            print(readFile(key))
        if userChoice == 4:
            removeFile()

###########
#
# התחברות ואוטוריזציה
#
######################
#
# לא ניתן להשתמש בתוכנה ללא אישור התחברות
#
###########

def loginAuth():
    authorized = False
    hashed_key = getHashedPass()
    i = 1
    while not authorized:
        if i > 4:
            quit()
        key = input(f"{5-i} attempts remaining, enter password: ")
        i += 1
        authorized = check_password(key, hashed_key)
    print('authorized!!')
    return key

key = loginAuth()
nav_menu(key)
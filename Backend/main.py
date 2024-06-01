import sqlite3
import os
import diaryDataBase

DB = diaryDataBase.diaryDataBase('diaryDBFile')
DB.createTable()

print('welcome to "myDiaryApp"!\n')

# Create today's page if it doesn't exist

while True:
    print('1. Write Today\'s Diary\n2. Edit Page\n3. Show All Page\n4. Exit\n')
    select = input('select: ')
    os.system('clear')
    if select == '1':
        print('Write Today\'s Diary')
    elif select == '2':
        print('Edit Page')
    elif select == '3':
        print('Show All Page')
    elif select == '4':
        print('Exit')
        break
    else:
        print('[Wrong input] Try again.\n')
        
    print()
        
print('Have a nice day.\n')
DB.closeTable()
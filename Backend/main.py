import os
import sqlite3
import datetime
import diaryDataBase

def printPage(page):
    for temp in page[1:]:
        print('\t' + temp + '\n')

if __name__ == '__main__':
    os.system('clear')
    DB = diaryDataBase.diaryDataBase('diaryDBFile')
    DB.createTable()

    print('Welcome to "myDiaryApp"!\n')

    today = datetime.date.today().strftime('[%Y.%m.%d]')

    if DB.getEntryByDate(today) == None:
        DB.insert(today,'1. Thankful', '2. Regret', '3. Study', '4. Exercise')
    printPage(DB.getEntryByDate(today))

    while True:
        print('[Select what you want to do]')
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
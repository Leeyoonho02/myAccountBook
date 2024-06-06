import os
import sqlite3
import datetime
import diaryDataBase

entryList = ['Thankful', 'Regret', 'Study', 'Exercise']

def printPage(page):
    for temp in page[1:]:
        print(temp + '\n')
        
def editPage(DB, date):
    page = DB.getEntryByDate(date)
    
    i = 0
    for temp in page[2:]:
        print(page[1] + '\n\n' + temp + '\n')
        text = input('Type Text>>\n')
        
        if text == '':
            continue
        else:
            DB.update(date, entryList[i], temp + '\n' + text)
        
        i += 1    
        os.system('clear')

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
        print('1. Write Today\'s Diary\n2. Edit Page\n3. Show Page\n4. Exit\n')
        select = input('select: ')
        os.system('clear')
        if select == '1':
            print('- Write Today\'s Diary\n')
            editPage(DB, today)
            os.system('clear')
        elif select == '2':
            print('- Edit Page\n')
        elif select == '3':
            print('- Show Page\n')
            printPage(DB.getEntryByDate(today))
        elif select == '4':
            print('- Exit\n')
            break
        else:
            print('[Wrong input] Try again.\n')
            
        print()
            
    print('Have a nice day.\n')
    DB.closeTable()
import sqlite3

class diaryDataBase:
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.c = self.conn.cursor()

    def createTable(self):
        self.c.execute('''
                CREATE TABLE IF NOT EXISTS pages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    thankful TEXT,
                    regret TEXT,
                    study TEXT,
                    exercise TEXT
                )
                ''')
        self.conn.commit()

    def insert(self, date, thankful, regret, study, exercise):
        self.c.execute('''
            INSERT INTO pages (date, thankful, regret, study, exercise)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, thankful, regret, study, exercise))
        self.conn.commit()
    
    def update(self, date, field, value):
        self.c.execute(f'UPDATE pages SET {field} = ? WHERE id = ?', (value, date))
        self.conn.commit()
        
    def getEntry(self):
        self.c.execute('SELECT * FROM pages')
        return self.c.fetchall()
    
    def getEntryByDate(self, date):
        temp = self.c.execute('SELECT * FROM pages WHERE date =?', (date, ))
        if temp == None:
            return None
        else:
            return self.c.fetchone()
    
    def closeTable(self):
        self.conn.close()
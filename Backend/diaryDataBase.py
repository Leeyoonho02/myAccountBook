import sqlite3

class diaryDataBase:
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.c = self.conn.cursor()

    def createTable(self):
        self.c.execute('''
                CREATE TABLE IF NOT EXISTS pages (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Date TEXT,
                    Thankful TEXT,
                    Regret TEXT,
                    Study TEXT,
                    Exercise TEXT
                )
                ''')
        self.conn.commit()

    def insert(self, date, thankful, regret, study, exercise):
        self.c.execute('''
            INSERT INTO pages (Date, Thankful, Regret, Study, Exercise)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, thankful, regret, study, exercise))
        self.conn.commit()
    
    def update(self, date, field, value):
        if field in ['Thankful', 'Regret', 'Study', 'Exercise']:
            self.c.execute(f'UPDATE pages SET {field} = ? WHERE Date = ?', (value, date))
            self.conn.commit()
        else:
            raise ValueError("Invalid field name.")
        
    def getEntry(self):
        self.c.execute('SELECT * FROM pages')
        return self.c.fetchall()
    
    def getEntryByDate(self, date):
        self.c.execute('SELECT * FROM pages WHERE Date =?', (date, ))
        return self.c.fetchone()
    
    def closeTable(self):
        self.conn.close()
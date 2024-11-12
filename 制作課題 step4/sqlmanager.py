import sqlite3
class SqlManager:
    def __init__(self):
        con = sqlite3.connect('history.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS 'history.db' (journal TEXT, subject TEXT, money INTEGER)")
        con.commit()
        con.close()
    
    def select_all(self):
        self.A = []
        con = sqlite3.connect('history.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM 'history.db'")
        self.doc = cur.fetchall()
        for i in self.doc:
            self.A.append(i)
        con.commit()
        con.close()
        return self.A

        '''
        curs.execute('select * from table')
        docs = curs.fetchall()
        for doc in docs:
        print(doc)
        '''

    def insert_all(self, lst):
        con = sqlite3.connect('history.db')
        cur = con.cursor()
        self.date = lst
        cur.execute("DELETE FROM 'history.db'")
        cur.executemany("INSERT INTO 'history.db' VALUES (?, ?, ?)", self.date)
        con.commit()
        con.close()

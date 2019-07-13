'''
Database in sqlite and fuctions
'''

import sqlite3

class Database:

    def __init__(self, db):
        #initializing main part of database
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS logline (id INTEGER PRIMARY KEY, web_adress text, login text, password integer, email integer)")
        self.conn.commit()

    def insert(self,web_adress,login,password,email):
        #modeling "insert" method for adding new data to DB
        self.cur.execute("INSERT INTO logline VALUES (NULL,?,?,?,?)",(web_adress,login,password,email))
        self.conn.commit()

    def view(self):
        #modeling "view" method for display all elements in DB
        self.cur.execute("SELECT * FROM logline")
        rows=self.cur.fetchall()
        return rows

    def search(self,web_adress="",login="",password="",email=""):
        #modeling "search" menthod for searching terms in DB
        self.cur.execute("SELECT * FROM logline WHERE web_adress=? OR login=? OR password=? OR email=?", (web_adress,login,password,email))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        #modeling "delete" method for removing chosen row
        self.cur.execute("DELETE FROM logline WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,web_adress,login,password,email):
        #modeling "update method" for changing data in selected row
        self.cur.execute("UPDATE logline SET web_adress=?, login=?, password=?, email=? WHERE id=?",(web_adress,login,password,email,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


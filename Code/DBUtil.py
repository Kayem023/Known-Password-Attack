import sqlite3

class Database:
    def __init__(self):
        self.db = "Auth.sqlite3"
        
    def addUser(username,password):
        try:
            conn = sqlite3.connect('Auth.sqlite3')
            c = conn.cursor()
            sql ='''INSERT INTO AUTHENTICATION(Username,Password) VALUES(?,?)'''
            c.execute(sql,(username,password))
            conn.commit()
            conn.close()
            return True
        except error:
            print(error)
            return False
    
    def existUser(username):
        try:
            conn = sqlite3.connect('Auth.sqlite3')
            c = conn.cursor()
            sql ='''SELECT * FROM AUTHENTICATION WHERE Username=?'''
            c.execute(sql,(username))
            rows = c.fetchall()
            if(len(rows)>0):
                conn.close()
                return True
            conn.close()
            return False
        except error as e:
            print(e)
            return False
    
    def isValidUser(username,password):
        try:
            conn = sqlite3.connect('Auth.sqlite3')
            c = conn.cursor()
            sql ='''SELECT * FROM AUTHENTICATION WHERE Username=? AND Password=?'''
            c.execute(sql,(username,password))
            rows = c.fetchall()
            if(len(rows)>0):
                conn.close()
                return False
            conn.close()
            return True
        except error as e:
            print(e)
            return True
        
    
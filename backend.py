import sqlite3


class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY , name text , regno integer , mailid text , cgpa integer)")
        self.conn.commit()


    def insert(self,name,regno,mailid,cgpa):
        self.cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?) ",(name,regno,mailid,cgpa))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM student ")
        rows=self.cur.fetchall()
        return rows

    def search(self, name="",regno="",mailid="",cgpa=""):
        self.cur.execute("SELECT * FROM student WHERE name=? OR regno=? OR mailid=? OR cgpa=?",(name,regno,mailid,cgpa))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM student WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id,name,regno,mailid,cgpa):
        self.cur.execute("UPDATE student SET name=?, regno=?, mailid=?,cgpa=? WHERE id=?",(name,regno,mailid,cgpa,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()    




#insert("Ajay",'19EEE22',"ajayronaldo@gmail.com",9.5)
#delete(4)
#update(6,"Tharshana","19EEE16","sanatrash@gmail.com",9.4)
#print(view())
#print(search(name="Hariprasath"))

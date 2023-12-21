# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Mysong(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists mysong(
        id integer primary key autoincrement,
        title text,
            artist text,
            file text,
            tonalitedepart text,
            tonalitearrive text,
            tonalitehauteur text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from mysong")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from mysong where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyfile(self,myid):
        print(self.mydb)
        print("select * from mysong where file like '%' || ? || '%'",(myid,))
        print(myid)
        self.cur.execute("select * from mysong where file like '%' || ? || '%'",(myid,))
        row=self.cur.fetchone()
        return row
    def getbyid(self,myid):

        self.cur.execute("select * from mysong where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        #print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into mysong (title,artist,file,tonalitedepart,tonalitearrive,tonalitehauteur) values (:title,:artist,:file,:tonalitedepart,:tonalitearrive,:tonalitehauteur)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error")
          #print("my error"+str(e))
        azerty={}
        azerty["mysong_id"]=myid
        azerty["notice"]="votre mysong a été ajouté"
        return azerty





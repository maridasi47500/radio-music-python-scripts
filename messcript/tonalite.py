# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Tonalite(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists tonalite(
        id integer primary key autoincrement,
        file text,
            song_id text,
            tonalitedepart text,
            tonalitearrive text,
            myvalue text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select tonalitedepart as note1, tonalitearrive as note2, myvalue as hey, file from tonalite")

        row=self.cur.fetchall()
        return row
    def getplusvite(self,myid):
        self.cur.execute("select "" as note1, "" as note2, vitesse.vitesse as hey, vitesse.file,tonalite.song_id from vitesse left join tonalite on tonalite.id = vitesse.tonalite_id where tonalite.song_id = ?",(myid,))

        row=self.cur.fetchall()
        return row
    def getbyfile(self,file):
        self.cur.execute("select tonalite.id,tonalite.tonalitedepart as note1, tonalite.tonalitearrive as note2, tonalite.myvalue as hey, tonalite.file, tonalite.song_id from tonalite where tonalite.file = ?",(file,))

        row=self.cur.fetchall()
        return row
    def getbysongid(self,myid):
        self.cur.execute("select tonalitedepart as note1, tonalitearrive as note2, myvalue as hey, file, song_id from tonalite where song_id = ?",(myid,))

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from tonalite where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from tonalite where id = ?",(myid,))
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
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into tonalite (file,song_id,tonalitedepart,tonalitearrive,myvalue) values (:file,:song_id,:tonalitedepart,:tonalitearrive,:myvalue)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["tonalite_id"]=myid
        azerty["notice"]="votre tonalite a été ajouté"
        return azerty





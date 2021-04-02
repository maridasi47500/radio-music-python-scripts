import re
import random
import os
from render import Render
from fichier import Fichier
import subprocess
from datetime import datetime
from song import Song
from mysong import Mysong
from myfunc import Myfunc
from myrecording import Myrecording
from program import Myprogram

class Messcripts(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="my thrift shop"
    self.myprogram=Myprogram
    self.dbSong=Mysong()
    self.figure=Render(self.title)
    self.recparams=["name","tonalitedepart","tonalitearrive","title","artist"]
    self.myrecparams=["myid"]
  def script1(self,param):
    xx=self.get_mydata()(uploads=self.myrecparams)
    myid=xx["myid"]
    song=self.dbSong.getbyid(myid)
   
    programs=self.myprogram()
    programs.myargs(["./messcript/changetone.sh"])
    self.figure.set_my_params("mytop", top1)
    self.figure.set_json(Fichier("./welcome","some.css").lire())

    return self
  def get_figure(self):
    return self.figure
  def script2(self,myscrit):
    filename=myscrit["title"][0].replace(".mp3","").split("/")[-1]
    current_dateTime=datetime.now()
    song=Song().save_heure_passage((filename,current_dateTime))
    self.figure.set_my_params("title", song["title"])
    self.figure.set_my_params("artist", song["artist"])
    self.figure.set_my_params("filename", song["filename"])
    self.figure.set_my_params("time", str(song["time"]))

    self.set_json(True)
    self.figure.set_body("")
    self.figure.set_json(Fichier("./welcome","chansonpassages.json").lire())
    print("hi there")
    return self
  def script3(self,myscrit):
    mylist=os.listdir("../radiohaker/public/uploads")
    k=random.randrange(0,(len(mylist) - 1))
    filename=mylist[k]
    print("filename =",filename)
    self.figure.set_my_params("filename", "/uploads/"+filename)
    song=Song().get_song((filename.replace(".mp3",""),))
    self.figure.set_my_params("title", song["title"])
    self.figure.set_my_params("artist", song["artist"])

    self.set_json(True)
    self.figure.set_body("")
    self.figure.set_json(Fichier("./welcome","chansons.json").lire())
    print("hi there")
    return self
  def new(self,myscrit):
    self.figure.set_content(Fichier("./welcome","new.html").lire())
    note=[
    ["c","do"],
    ["c#","do#"],
    ["d","re"],
    ["d#","re"],
    ["e","mi"],
    ["f","fa"],
    ["f#","fa#"],
    ["g","sol"],
    ["g#","sol#"],
    ["a","la"],
    ["a#","la#"],
    ["b","si"],
    ]
    self.figure.set_my_params("note", note)
    print("hi there")
    return self
  def myshop(self,myscrit):
    self.figure.set_content(Fichier("./welcome","myshop.html").lire())
    print("hi there")
    return self
  def hi(self,myscrit):
    self.figure.set_content(Fichier("./welcome","index.html").lire())
    print("hi there")
    return self
  def create(self,myscrit):
    xx=self.get_mydata()(uploads=self.recparams)
    print("create with my params : ", xx)
    rec=Myrecording(xx)
    self.figure.set_content("<a>redirected permanently</a>")

    if rec.create():
      print("uploaded and save...")
      self.set_redirect("/myshop")
    return self

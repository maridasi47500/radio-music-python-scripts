import re
import random
import os
from render import Render
from fichier import Fichier
import subprocess
from datetime import datetime
from song import Song
from myfunc import Myfunc
from myrecording import Myrecording
class Hello(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="my thrift shop"
    self.figure=Render(self.title)
    self.recparams=["name","image","price","date"]
  def mycss(self,param):
    self.figure.set_my_params("myid", param["myid"][0])
    self.css=True
    self.figure.set_body("")
    mylist=[]
    left=random.randrange(0,100)
    myotherlist=[]
    lists=[]
    left1=None
    top1=None
    premier=True
    for i in range(11):


      
      left-=random.randrange(1,5)
      myotherlist.insert(0,left)
      el1=random.randrange(i*10,(i*10 +10))
      mylist.append(el1)
    i=0
    for x in mylist:

      left=myotherlist[i]
      el1=mylist[i]
      lists.append({"left":left, "top": el1})
      i+=1 
      if premier:
        premier=False
        left1=left
        top1=el1
    self.figure.set_my_params("mycss", {"top": mylist,"left":myotherlist})
    self.figure.set_my_params("lists", lists)
    self.figure.set_my_params("myleft", left1)
    self.figure.set_my_params("mytop", top1)
    self.figure.set_json(Fichier("./welcome","some.css").lire())

    return self
  def get_figure(self):
    return self.figure
  def passage(self,myscrit):
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
  def jouerchanson(self,myscrit):
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

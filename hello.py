import re
import random
import os
from render import Render
from fichier import Fichier
import subprocess
from datetime import datetime
from mysong import Mysong
from myfunc import Myfunc
from myrecording import Myrecording
class Hello(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="Bienvenue dans ce repository - chercher des tonalités"
    self.figure=Render(self.title)
    self.dbSong=Mysong()
    self.recparams=["title","artist","file","tonalitedepart","tonalitearrive","tonalitehauteur"]
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
    self.figure.set_my_params("mysongs", self.dbSong.getall())
    self.figure.set_content(Fichier("./welcome","mysongs.html").lire())
    print("hi there")
    return self
  def hi(self,myscrit):
    self.figure.set_content(Fichier("./welcome","index.html").lire())
    print("hi there")
    return self
  def render_some_json(self,x):
    self.figure.set_json(x)
    self.set_json(True)
    print("func json")
    return self
  def create(self,myscrit):
    xx=self.get_mydata()(uploads=self.recparams)
    print("file")
    #print(xx["file"])
    #print("create with my params : ", xx)
    rec=self.dbSong.create(xx)
    self.figure.set_my_params("redirect", "/songs")
    print("func 1")
    return self.render_some_json(Fichier("./welcome","redirect.json").lire())


import re
import random
import os
from render import Render
from fichier import Fichier
import subprocess
from datetime import datetime
from song import Song
from mysong import Mysong
from chaine import Chaine
from myfunc import Myfunc
from myrecording import Myrecording
from program import Myprogram


class Messcripts(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="chercher des tonalités"
    self.myprogram=Myprogram
    self.dbSong=Mysong()
    self.figure=Render(self.title)
    self.recparams=["name","tonalitedepart","tonalitearrive","title","artist"]
    self.myrecparams=["myid"]
    self.vitesseparams=["vitesse","myid"]
  def script1(self,param):
    xx=self.get_mydata()(uploads=self.myrecparams)
    myid=xx["myid"]
    song=self.dbSong.getbyid(myid)
   
    programs=self.myprogram(song["file"])

    programs.myargs(["./messcript/changetone.sh","./uploads/"+song["file"]])
    try:
        if not Fichier("./uploads",song["file"].split(".")[0]+".wav").existe():
           programs.run()
    except:
        print("script 1 déjà executé")
    self.figure.set_my_params("redirect", "/songs")
    self.render_some_json(Fichier("./welcome","redirect.json").lire())

    return self
  def get_figure(self):
    return self.figure
  def script2(self,myscrit):
    xx=self.get_mydata()(uploads=self.myrecparams)
    myid=xx["myid"]
    song=self.dbSong.getbyid(myid)
   
    programs=self.myprogram(song["file"])
    othername=song["file"].split(".")[0]+".wav"
    #python3 tone.py in.wav a g
    programs.myargs(["python3","./messcript/tone.py","./uploads/"+othername, song["tonalitedepart"], song["tonalitearrive"]])
    try:
        programs.run()
    except:
        print("script 2 déjà executé")
    self.figure.set_my_params("redirect", "/songs")
    self.render_some_json(Fichier("./welcome","redirect.json").lire())

    return self
  def script3(self,myscrit):
    xx=self.get_mydata()(uploads=self.vitesseparams)
    myid=xx["myid"]
    vitesse=xx["vitesse"]
    song=self.dbSong.getbyid(myid)
   
    programs=self.myprogram(song["file"])
    othername=song["file"].split(".")[0]+".wav"
    #python3 tone.py in.wav a g
    hey=int(vitesse)
    if hey==50:
        hey=50
    elif hey > 50:
        hey=(hey-50)*2
    elif hey < 50:
        hey=float(hey/50)
    programs.myargs(["python3","./messcript/pluslent_saschangerlahauteur.py","./uploads/"+othername, str(hey)])
    try:
        programs.run()
    except:
        print("script 2 déjà executé")
    self.figure.set_my_params("redirect", "/songs")
    self.render_some_json(Fichier("./welcome","redirect.json").lire())

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

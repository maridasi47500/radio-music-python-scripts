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
class Xmas(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="my thrift shop"
    self.figure=Render(self.title)
    self.recparams=["name","image","price","date"]
  def hello(self,myscrit):
    self.figure.set_content(Fichier("./xmas","hello.html").lire())
    print("hi there")
    return self

from fichier import Fichier
from os import listdir as liste
class Testscript:
    def __init__(self,path,name):
      self.path=path
      self.name=name
    def existe(self):
      mymusic=".wav"
      myname=self.name.replace(".mp3",mymusic)
      myname=myname.replace(".mp4",mymusic)
      return Fichier(self.path,myname).existe()
    def messcripts(self):
      mymusic=".wav"
      myname=self.name.replace(".mp3",mymusic)
      myname=myname.replace(".mp4",mymusic)
      maliste=[]
      print(liste(self.path))
      for x in liste(self.path):
          print(x,myname)
          if myname in x and x != myname and "faster" not in x:
              note=x.split("_")
              note1=note[1]
              note2=note[2]
              maliste.append({"hey":"","file":x,"note1":note1, "note2":note2})
      return maliste
    def messcriptsplusvite(self):
      mymusic=".wav"
      myname=self.name.replace(".mp3",mymusic)
      myname=myname.replace(".mp4",mymusic)
      maliste=[]
      print(liste(self.path))
      for x in liste(self.path):

          if myname in x and x != myname and "faster" in x:
              note=x.split("_")
              print(note)
              hey=str(note[1])
              #print(x,myname,hey,note1,note2)
              maliste.append({"hey":hey,"file":x,"note1":"", "note2":""})
      return maliste

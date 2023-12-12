from fichier import Fichier
class Testscript:
    def __init__(self,path,name):
      self.path=path
      self.name=name
    def existe(self):
      mymusic=".wav"
      myname=self.name.replace(".mp3",mymusic)
      myname=myname.replace(".mp4",mymusic)
      return Fichier(self.path+"/"+myname).existe()

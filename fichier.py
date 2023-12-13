from os.path import exists as existe
class Fichier:
  def __init__(self,path,name):
    self.path=path
    self.name=name
  def existe(self):
    x=existe(self.path+"/"+self.name)
    print(x)
    return x
  def lire(self):
    print(self.path+"/"+self.name)
    j=open(self.path+"/"+self.name, "r")
    return j.read()
  def lirefichier(self):
    print(self.path+"/"+self.name)
    j=open(self.path+"/"+self.name, "rb")
    return j.read()
  def ecrire(self,mycontent):
    hey=open((self.path+"/"+self.name),"a")
    hey.write(mycontent)
    hey.close()
  def ecriremusique(self,mycontent):
    hey=open((self.path+"/"+self.name),"a+b")
    hey.write(mycontent)
    hey.close()

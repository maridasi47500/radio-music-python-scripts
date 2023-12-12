import subprocess
class Pythonscript:
  def __init__(self,name):
    self.name=name
    self.myargs=[]
  def set_args(self,myargs):
    self.myargs=myargs
  def lancer(self):
    myprogram=[]
    if self.name.endswith(".py"):
      myprogram=["python3",self.name]
    elif self.name.endswith(".sh"):
      myprogram=["sh",self.name]
    for myarg in self.myargs:
      myprogram.append(myarg)
    return subprocess.check_output(myprogram)
  
  

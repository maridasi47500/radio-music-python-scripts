from subprocess import check_output as runmyscript
class Myprogram:
  def __init__(self,hey):
    self.hey=hey
    self.someargs=[hey]
    self.runprogram=runmyscript
  def myargs(self,a):
    self.someargs=a
  def run(self):
    self.runprogram(self.someargs)
    

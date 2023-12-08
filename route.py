import re
from hello import Hello
from xmas import Xmas
from erreur import Erreur
from mypic import Pic
from son import Son
from render import Render
from javascript import Js
from pythonscript import Pythonscript
from stylesheet import Css


class Route():
  def __init__(self):
    self.params={}
    self.route={

r"^/songs/jouerunechanson$":"Hello#jouerchanson",
r"^/songs/playmusique1$":"Hello#jouerchanson",
r"^/songs/playmusique$":"Hello#jouerchanson",
r"^/xmas$":"Xmas#hello",
r"^/passage$":"Hello#passage",
r"^/songs/musique$":"Hello#jouerchanson",
r"^/ajouterunemusique$":"Hello#new",
r"^/somecss$":"Hello#mycss",

r"^/$":"Hello#hi"

}
  def get_route(self,myroute,myparams,mydata=None):
    print(myroute,myparams)
    print("myroute")

    self.params=myparams
    if myroute.endswith("ico"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith("webp"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith("png"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith(".mp3"):
        myProgram=Son(name=myroute)
        return myProgram
    elif myroute.endswith(".wav"):
        myProgram=Son(name=myroute)
        return myProgram
    elif myroute.endswith(".css"):
        myProgram=Css(name=myroute)
        return myProgram
    elif myroute.endswith(".js"):
        myProgram=Js(name=myroute)
        return myProgram
    else:
        for i in self.route:
          j=self.route[i]
          if re.match(i,myroute):
            print(j, "my func found")
            loc = {}
            print("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params=params).encode()".format(params=myparams))
            exec("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"')",globals(),loc)
            print(loc["myvar"])
            print("=my var")
            print(mydata)
            print("=my data")
            loc["myparams"]=myparams
            #loc["mydata"]=None


            if mydata:

                loc["myvar"].set_mydata(mydata)
                print(loc["myvar"].get_mydata())
                print("=mydata")

            exec("myvar=myvar.work(params=myparams)",globals(),loc)

            return loc["myvar"]
        mytext=(Erreur().err404())
        return mytext

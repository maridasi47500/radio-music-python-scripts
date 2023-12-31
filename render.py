from fichier import Fichier
from testscript import Testscript
from tonalite import Tonalite
from mysong import Mysong
import os
from db import Db
class Render():
  def __init__(self,title):
    self.title=title
    self.body=title
    self.template="./template/radio.html"
    self.headingone=title
    self.collection={}
    self.tonalite=Tonalite()
    self.song=Mysong()
    self.my_params={"myoutput":""}
    self.collection_string=""
  def get_my_params(self):
    return self.my_params
  def set_my_params(self,name,param):
    self.my_params[name]=param
  def set_collection(self,name,collection):
    self.collection[name]=collection
  def render_collection_json(self,path,view,mycollection,as_,erreur):
    try:
      myview=open(os.path.abspath(path+"/"+view), "r").read()
      string=""
      count=0
      print(len(mycollection),"my collection")
      paspremier=False
      i=1
      lencollection=len(mycollection)
      paspremier=False
      for res in mycollection:
        pasdernier=i<lencollection
        i+=1
        for x in myview.split("<%="):
           if "%>" not in x: 
             string+=x
             continue
           else:
             y=x.split("%>")
             myexpr=y[0]
             print(myexpr)
             try:
               mystr=y[1]
             except:
               mystr=""
             try:
               loc={"params":self.my_params,as_: res,"pasdernier":pasdernier,"paspremier": paspremier}

               print(loc)
               string+=str(eval(myexpr, globals(), loc))
             except:
               string+=""

             string+=mystr
        paspremier=True




      return string
    except Exception as e:
      return "<p>{erreur}</p>".format(erreur=(erreur+str(e)))
  def render_collection(self,path,view,mycollection,as_,erreur):
    try:
      myview=open(os.path.abspath(path+"/"+view), "r").read()
      string=""
      count=0
      print(len(mycollection),"my collection")
      index=0
      for res in mycollection:
        for x in myview.split("<%="):
           if "%>" not in x: 
             string+=x
             continue
           else:
             y=x.split("%>")
             myexpr=y[0]
             print(myexpr)
             try:
               mystr=y[1]
             except:
               mystr=""
             try:
               loc={"Song":self.song,"Tonalite":self.tonalite,"params":self.my_params,("index_"+as_): index,"index":index,as_: res,"Testscript":Testscript,"render_collection":self.render_collection}
               #print(loc)
               print(myexpr)
               string+=str(eval(myexpr, globals(), loc))
             except Exception as e:
               print("erreur",e)
               string+=""
             string+=mystr
        index+=1

      return string
    except Exception as e:
      return "<p>{erreur}</p>".format(erreur=(erreur+str(e)))
  def render_body(self):
    string=""
    myinclude=False
    for x in self.body.split("<%="):
       print(x)
       y=x.split("%>")
       myexpr=y[0]
       try:
         mystr=y[1]
         myinclude=True
       except Exception as e:
         mystr=""
         myinclude=False
       if myinclude:
         try:
           print(myexpr, "monexpression")
           loc={"Tonalite":self.tonalite,"params":self.my_params,"render_collection_json":self.render_collection_json,"self": self,"Db":Db,"render_collection":self.render_collection, "my_params":self.my_params,"Fichier":Fichier,"Testscript":Testscript}
           exec("myres="+myexpr,globals(),loc)
           if type(loc["myres"]) is bytes:
             string+=loc["myres"].decode()
           else:
             string+=loc["myres"]
         except Exception as e:
           print(e,"m error")
           string+=""
         string+=mystr
         myinclude=False
       else:
         string+=myexpr
    self.body=string
  def get_title(self):
    return self.title
  def get_headingone(self):
    return self.title
  def get_body(self):
    return self.body
  def set_json(self,mybody):
    self.template=False
    if len(mybody) > 0:
      if type(mybody) is bytes:
        print(mybody)
        self.body=str(mybody)
      else:
        self.body=mybody
    else:
      self.body+=''
  def set_body(self,mybody):
      self.body=mybody
  def set_content_redirect(self,mybody):
    self.template=False
    if len(mybody) > 0:
      if type(mybody) is bytes:
        print(mybody)
        self.body+=str(mybody)
      else:
        self.body+=mybody
    else:
      self.body+=''
  def set_content(self,mybody):
    if len(mybody) > 0:
      if type(mybody) is bytes:
        print(mybody)
        self.body+=str(mybody)
      else:
        self.body+=mybody
    else:
      self.body+=''
  def ajouter_a_mes_mots(self,mot):
    self.body += mot
  def render_figure(self):
    if self.template:
      template=open(self.template,"r").read()
      self.body= template.format(mots=self.get_headingone(),debutdemesmots=self.get_title(),partiedemesmot=self.get_body())
    self.render_body()
    return self.body

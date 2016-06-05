# Spysql
Detecteur de faille sql
coded By Enokas Worm
# Usage :
 --dork          : pour inserer un dork (voir liste
 	                 avec --dork-list
 --scan-sql      : lancer la recherche de site vulnerable
                   apres la recuperation des urls avec --dork
 --inject or -i  : Verifie si un sire est vulnerable a partir d'une 
                   url donne
 --dork-list      : Affiche une list de dork
 --help          : Affiche les options
Exemple:
 - python spysql.py --dork [dork]
   + python spysql.py --dork inurl:php?id= 
 - python spysql.py --scan-sql
 - python spysql.py --inject [url]
   + python spysql.py --inject http://example.com/index.php?id=2

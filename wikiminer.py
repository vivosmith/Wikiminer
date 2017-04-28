from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys
pages=set()
sys.setrecursionlimit(2000000000)
def getlinks(pageurl):
   global pages
   html=urlopen("http://en.wikipedia.org"+pageurl)
   bsOBJ=BeautifulSoup(html,"html.parser")
   for link in bsOBJ.findAll("a",href=re.compile("^(/wiki/)")):
      if 'href' in link.attrs:
         if link.attrs['href'] not in pages:
            newpage=link.attrs['href']
            print(newpage+'  '+str(bsOBJ.h1.get_text()))
            pages.add(newpage)
            getlinks(newpage)
getlinks("")
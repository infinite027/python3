import os
from bs4 import BeautifulSoup
from urllib import request
from datetime import date

def getUrl(rawList):
      newList=[]
      for raw in rawList:
            equalPosition=[]
            for letter in range(len(raw)):
                  if raw[letter]=="=":
                        equalPosition.append(letter)
            raw=raw[equalPosition[2]+2:equalPosition[3]-7]
            newList.append(raw)
      return newList
                        
                  
def main():
      url='http://www.afwing.com/'
      content=request.urlopen(url).read()
      soup=BeautifulSoup(content)
      pictxt_wrap=soup.find_all('div','pictxt_wrap')
      raw=[]
      for wrap in pictxt_wrap:
            raw.append(wrap.find_all('img'))
      for i in range(len(raw)):
            raw[i]=str(raw[i])
      imgs=getUrl(raw)
      for item in range(len(imgs)):
            imgs[item]='http://www.afwing.com'+imgs[item]
      for name in range(len(imgs)):
            with open('C:/Users/xinyu/Documents/spider image/'+str(date.today())+str(name)+".jpg",'wb') as image:
                  image.write(request.urlopen(imgs[name]).read())
            image.close()
      print('done')

      
if __name__=="__main__":
      main()

from bs4 import BeautifulSoup
import os
import urllib.request
from datetime import date
import re

def removeTags(string):
    string=str(string)
    string.replace('"',"'")
    start=[]
    end=[]
    for count in range(len(string)):
        if string[count]=="<":
            start.append(count)
        if string[count]==">":
            end.append(count)
    print(end)
    print(start)
    try:
        end=end[0]
        start=start[1]
        string=string[end+1:start]
        return string
    except:
        return 0
            
                
            
def main():
    file=open("C:\\Users\\xinyu\\Desktop\\News Everyday.txt",'a')
    today=date.today()
    file.write(str(today))
    file.write('\n')
    url = "http://news.google.ca/"
    url_content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(url_content,'html.parser')
    news = []
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for letter in letters:
        selector='#MAA4AEg'+letter+'UABgAWoCY2E > span'
        new=soup.select(selector)
        new=str(new)
        new.replace("["," ")
        new.replace("]"," ")
        if new:
            news.append(new)
    for new in news:
        new=removeTags(new)
        if new != 0:
            print(new,end='\n')
            file.write(str(new))
            file.write('\n')
        else:
            break
    file.write('\n')
    file.close()
    os.system('pause')

if __name__=="__main__":
    file=open("C:\\Users\\xinyu\\Desktop\\News Everyday.txt",'r')
    ver=str(date.today())+'\n'
    stop=False
    for line in file:
        if line==ver:
            stop=True
            break
    if stop==True:
        print("News already recorded today")
        os.system('pause')
    else:
        main()



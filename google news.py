#! /usr/bin/python3.5
from lxml import etree
import os
import urllib.request as req
from datetime import date


def main():
    file=open("C:\\Users\\xinyu\\Desktop\\News Everyday.txt",'a')
    file.write("\n");
    file.write(str(date.today())+"\n")
    url = 'https://news.google.com/news/?ned=ca&hl=en-CA'
    content = req.urlopen(url).read()
    content = etree.HTML(content)
    xpaths = [ '//*[@id="yDmH0d"]/c-wiz/c-wiz/main/div[1]/div[1]/c-wiz/div/c-wiz[1]/c-wiz/div/div[2]/c-wiz[1]/a','//*[@id="yDmH0d"]/c-wiz/c-wiz/main/div[1]/div[1]/c-wiz/div/c-wiz[2]/c-wiz/div/div[2]/c-wiz/a','//*[@id="yDmH0d"]/c-wiz/c-wiz/main/div[1]/div[1]/c-wiz/div/c-wiz[3]/c-wiz/div/div[2]/c-wiz/a','//*[@id="yDmH0d"]/c-wiz/c-wiz/main/div[1]/div[1]/c-wiz/div/c-wiz[4]/c-wiz/div/div/c-wiz[1]/a','//*[@id="yDmH0d"]/c-wiz/c-wiz/main/div[1]/div[1]/c-wiz/div/c-wiz[5]/c-wiz/div/div[2]/c-wiz/a','//*[@id="yDmH0d"]/c-wiz/c-wiz/main/div[1]/div[1]/c-wiz/div/c-wiz[6]/c-wiz/div/div[2]/c-wiz[1]/a']
    for xpath in xpaths:
        temp = content.xpath(xpath)
        for each in temp:
            print(str(each.text)+"\n")
            file.write(str(each.text)+"\n")
    print("done")
    os.system("pause")
    
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



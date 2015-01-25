import os
import sys
import urllib2

def downloadMp3File(url):
    # mp3file = urllib2.urlopen("http://www.example.com/songs/mp3.mp3")
    mp3file = urllib2.urlopen(url)
    output = open('test.mp3','wb')
    output.write(mp3file.read())
    output.close()

def changeText(text):
    text = text.replace('\n','')
    text_list = re.split('(\,|\.|\;|\:)', text)

    lines = []

def main():
    file_name = raw_input("Enter the name of the file.\n")
    file = open(file_name,'r')
    text = file.read()
    # print(text)
    changeText(text)

main()

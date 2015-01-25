import re
import os
import sys
import urllib2

def downloadMp3File(url):

    # mp3file = urllib2.urlopen("http://www.example.com/songs/mp3.mp3")
    mp3file = urllib2.urlopen(url)
    output = open('test.mp3','wb')
    output.write(mp3file.read())
    output.close()

def sanitizeText(text):

    text = text.replace('\n','')
    text_list = re.split('(\,|\.|\;|\:)', text)
    return text_list

def changeText(text):

    text_list = sanitizeText(text)
    lines = []

    for index,value in enumerate(text_list):

        if (index%2 == 0):
            lines.append(val)
        else:
            connected_string = ''.join((lines.pop(), val))

def main():

    file_name = raw_input("Enter the name of the file.\n")
    file = open(file_name,'r')
    text = file.read()
    # print(text)
    changeText(text)

main()

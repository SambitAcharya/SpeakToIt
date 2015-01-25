import os
import sys
import urllib2

def downloadMp3File():
    mp3file = urllib2.urlopen("http://www.example.com/songs/mp3.mp3")
    output = open('test.mp3','wb')
    output.write(mp3file.read())
    output.close()
def main():
    file_name = raw_input("Enter the name of the file.\n")
    file = open(file_name,'r').read()
    print(file)

main()

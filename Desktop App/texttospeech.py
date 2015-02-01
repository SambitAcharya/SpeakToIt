import re
import os
import sys
import urllib,urllib2

def downloadMp3File(lines,url):

    # mp3file = urllib2.urlopen("http://www.example.com/songs/mp3.mp3")
    # mp3file = urllib2.urlopen(url)
    # output = open('test.mp3','wb')
    # output.write(mp3file.read())
    # output.close()
    for index,line in enumerate(lines):
        query_parameters = {"l":language,'q':line, 'total': len(text_lines),'index':index}
        url = 'http://translate.google.com/translate_tts?ie=UTF-8'+ unicode_urlencode(query_parameters)
        headers = {'Host':'translate.google.com','User-Agent':'Mozilla 5.10'}

def sanitizeText(text):

    text = text.replace('\n','')
    text_list = re.split('(\,|\.|\;|\:)', text)
    return text_list

def changeText(text):

    text_list = sanitizeText(text)
    lines = []

    for index,value in enumerate(text_list):

        if (index%2 == 0):
            lines.append(value)
        else:
            connected_string = ''.join((lines.pop(), value))
            if len(connected_string) < 100:
                lines.append(connected_string)
            else:
                fragments = re.split('( )', connected_string)
                placeholder_array = []
                placeholder_string = ""
                for fragment in fragments:
                    placeholder_string+=fragment
                    if len(placeholder_string) > 80:
                        placeholder_array.append(placeholder_string)
                        placeholder_string = ""

                placeholder_array.append(placeholder_string)
                lines.extend(placeholder_array)

    return lines

def unicode_urlencode(parameters):
    if isinstance(parameters, dict):
        parameters = parameters.items()
    return urllib.urlencode([(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in parameters])

def main():

    file_name = raw_input("Enter the name of the file.\n")
    file = open(file_name,'r')
    text = file.read()
    # print(text)
    changeText(text)

main()

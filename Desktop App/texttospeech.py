#Imports
import re
import os
import sys
import urllib,urllib2
import time
import subprocess
import argparse

def unicode_urlencode(parameters):

    '''

        Function to encode parameters which are to be injected into the URL

    '''

    if isinstance(parameters, dict):
        parameters = parameters.items()
    return urllib.urlencode([(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in parameters])

def sanitizeText(text):

    text = text.replace('\n','')
    text_list = re.split('(\,|\.|\;|\:)', text)
    return text_list

def changeText(text):

    '''

        Function to break the text into parts of 100 characters or smaller
        Owing to the API limitations.

    '''
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

def downloadMp3File(lines,language,file):

    '''

        Function to download the MP3 file generated by the TTS API.

    '''

    for index,line in enumerate(lines):
        query_parameters = {"tl":language,'q':line, 'total': len(lines),'idx':index}
        url = 'http://translate.google.com/translate_tts?ie=UTF-8'+ '&' + unicode_urlencode(query_parameters)
        headers = {'Host':'translate.google.com','User-Agent':'Mozilla 5.10'}
        request  = urllib2.Request(url,'',headers)
        sys.stdout.write('.')
        sys.stdout.flush()
        if len(line)>0:
            try:
                response = urllib2.urlopen(request)
                file.write(response.read())
                time.sleep(0.5)
            except urllib2.HTTPError as e:
                print ('%s' %e)

    print 'Saved MP3 to %s' %(file.name)
    file.close()

def play(file_name):

    '''

        Function to play the file after detecting the platform
        Supports only linux and OSX.

    '''

    if sys.platform == 'linux' or sys.platform == 'linux2':
        # Linux
        subprocess.call(['play',file_name])

    elif sys.platform == "darwin":
		# OS X
		subprocess.call(["afplay", filename])
def main():

    if len(sys.argv)==1:
        sys.exit(1)

    args = parser.parse_args()

    if args.file:
        text = args.file.read()
    if args.string:
        text = ''.join(map(str,args.string))

    lines = changeText(text)
    language = args.language
    output = args.output
    play = args.play
    downloadMp3File(lines,language,output)

    if play == True:
        play(output.name)


if __name__ == '__main__':

    description = 'Text To Speech Converter'
    parser = argparse.ArgumentParser(prog='GoogleTextToSpeech', description=description,epilog='Just do it')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f','--file', type=argparse.FileType('r'), help='File to read text from.')
    group.add_argument('-s', '--string', action='store', nargs='+', help='A string of text to convert to speech.')

    parser.add_argument('-o','--output', action='store', nargs='?',help='Filename to output audio to',type=argparse.FileType('w'),default='VoicedText.mp3')
    parser.add_argument('-l','--language', action='store', nargs='?',help='Language to output text to.', default='en')

    parser.add_argument('-p','--play', action='store_true', help='Play the speech if your computer allows it.')

    main()

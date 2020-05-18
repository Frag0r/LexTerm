""" Term Extract by Marcel Leschnik  ©2020 """

"""
Try	to	write	a code	to	extract	terms	with	the structure:
a. Article	Adjective*	Noun;
b.	Article	Noun	Noun
"""
from pathlib import Path
import re

my_file = Path("data/output.txt")
if my_file.is_file():
    # file exists
    outputData=open("data/output.txt", "a")
else:
    outputData=open("data/output.txt", "w")
    outputData.write("Term_Extract by Marcel Leschnik\n")
    outputData.write("Article Adjective* Noun\n")
    outputData.close()
    outputData=open("data/output.txt", "a")

inputData=open("data/gnu_de_en__german.vert", "r", encoding="utf8") #Path to inputfile TO-DO: Include Extraction of other files w/o changing code
statusCode = 0

regExArtikel = re.compile(r'ART.')
regExNomen = re.compile(r"N.")
regExAdjektiv = re.compile(r"ADJA.")

methodInput = input("What kind of extraction do you want ?\na. Article	Adjective*	Noun;\nb.	Article	Noun	Noun\n")

if methodInput == 'a':
    methodChoice = False
else:
    if methodInput == 'b':
        methodChoice = True
    else:
        print("Wrong Input! Restart Script")
        quit
    

def checkRegEx(wortart,eingabe):
    if wortart.match(eingabe):
        return True
    else:
        return False

def termExtraction(method):
    global statusCode
    if method:  #Method B
        if statusCode == 0:
            if checkRegEx(regExArtikel,entry[1]):
                outputData.write(term+" ")
                statusCode = 1
        if statusCode == 1:
            if checkRegEx(regExNomen,entry[1]):
                outputData.write(term+"\n")
                statusCode = 2
        if statusCode == 2:
            if checkRegEx(regExNomen,entry[1]):
                outputData.write(term+"\n")
                statusCode = 0
    else:   #Method A
        if statusCode == 0:
            if checkRegEx(regExArtikel,entry[1]):
                outputData.write(term+" ")
                statusCode = 1
        if statusCode == 1:
            if checkRegEx(regExNomen,entry[1]):
                outputData.write(term+"\n")
                statusCode = 0
            if checkRegEx(regExAdjektiv,entry[1]):
                outputData.write(term+" ")
                statusCode = 2
        if statusCode == 2:
            if checkRegEx(regExNomen,entry[1]):
                outputData.write(term+"\n")
                statusCode = 0

for line in inputData:
    entry = line.split('\t')
    term = entry[0]
    
    if term.find("<") == -1:
        termExtraction(methodChoice)

inputData.close()
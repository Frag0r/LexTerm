""" Term Extract by Marcel Leschnik  ©2020 """

"""
Try	to	write	a code	to	extract	terms	with	the structure:
a. Article	Adjective*	Noun;
b.	Article	Noun	Noun
"""
from pathlib import Path

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

inputData=open("data/gnu_de_en__german.vert", "r", encoding="utf8")
statusCode = 0

for line in inputData:
    entry = line.split('\t')
    term = entry[0]
    if term.find("<") == -1:
        if statusCode == 0:
            if entry[1].find("ART") != -1:
                outputData.write(term+" ")
                statusCode = 1

        if statusCode == 1:
            if entry[1].find("N.") != -1:
                outputData.write(term+"\n")
                statusCode = 0
            if entry[1].find("ADJA.") != -1:
                outputData.write(term+" ")
                statusCode = 2
        if statusCode == 2:
            if entry[1].find("N.") != -1:
                outputData.write(term+"\n")
                statusCode = 0

inputData.close()
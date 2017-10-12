#feat 1 = discourse markers (first, next then, therefore, etc...)
#feat 2 = first person pronoun - I
#feat 3 = contractions

import re
import os

import nltk

from discourse_markers import markers
from first_person_pronouns import pronouns
from test_file import test
from test_file2 import test as test2

def discRate(text):
    numTimes = 0
    for token in text:
        if token in markers:
            numTimes += 1
    normedRate = (numTimes / len(text)) * 1000
    return normedRate

def proRate(text):
    numTimes = 0
    for token in text:
        if token in pronouns:
            numTimes += 1
    normedRate = (numTimes / len(text)) * 1000
    return normedRate

def contRate(raw_text):
    numTimes = 0
    contraction_re = r"\s([a-zA-Z]+'[a-zA-Z]+)\s"
    for match in re.findall(contraction_re, raw_text):
        numTimes += 1
    normedRate = (numTimes / len(raw_text)) * 1000
    return normedRate

output = open("analysis_results.tsv","w+")

output.write("FILE NAME\tREGISTER\tDISCOURSE MARKERS\tFIRST PERSON\tCONTRACTIONS\n")

def runTest(testStr, testNum):
    raw_text = testStr.lower()
    tokens = nltk.word_tokenize(raw_text)
    text = nltk.Text(tokens)
    register = "test" + str(testNum)
    filename = "test_file" + str(testNum)
    output.write(filename + "\t" + register + "\t{:.4f}".format(discRate(text)) + "\t{:.4f}".format(proRate(text)) + "\t{:.4f}\n".format(contRate(raw_text)))

runTest(test, 1)
runTest(test2, 2)

for filename in os.listdir('Mini-CORE'):
    f = open(os.path.join('./Mini-CORE', filename),"r")
    raw_text = f.read().lower()
    tokens = nltk.word_tokenize(raw_text)
    text = nltk.Text(tokens)
    register = filename[2:4]
    output.write(filename + "\t" + register + "\t{:.4f}".format(discRate(text)) + "\t{:.4f}".format(proRate(text)) + "\t{:.4f}\n".format(contRate(raw_text)))
print("Analysis finished.")

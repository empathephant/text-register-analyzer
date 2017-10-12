#feat 1 = discourse markers (first, next then, therefore, etc...)
#feat 2 = first person pronoun - I
#feat 3 = contractions

import re
import os

import nltk

from discourse_markers import markers
from first_person_pronouns import pronouns
from test_document import test

# defaults for testing
# raw_text = test
# register = "HG2G"
# filename = "test_file"

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

def contRate(text):
    numTimes = 50
    normedRate = (numTimes / len(text)) * 1000
    return normedRate

print("FILE NAME\tREGISTER\tDISCOURE MARKERS\tFIRST PERSON\tCONTRACTIONS")
for filename in os.listdir('Mini-CORE'):
    f = open(os.path.join('./Mini-CORE', filename),"r")
    raw_text = f.read().lower()
    tokens = nltk.word_tokenize(raw_text)
    text = nltk.Text(tokens)
    register = filename[2:4]
    print(filename + "\t" + register + "\t{:.2f}".format(discRate(text)) + "\t{:.2f}".format(proRate(text)) + "\t{:.2f}".format(contRate(text)))

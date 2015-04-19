"""
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
Hint: The string module provides strings named whitespace, which contains space, tab, newline, etc., and punctuation which contains the punctuation characters. Let’s see if we can make Python swear:
>>> import string
>>> print string.punctuation
"""

import string

def starPlotter(count):
    retString = '*' * count
    return retString
        
def constantWidth(string,width):
    if len(string) <= width:
        retString = string + ' ' * ( width - len(string))
    else:
        retString = string[:width]
    return retString

def createDict(fileName):
    wordDict = {}
    fin = open(fileName)
    for line in fin:
        words = line.strip(string.punctuation + string.whitespace).lower().split()
        for word in words:
            stripWord = word.strip(string.punctuation + string.whitespace)
            wordDict[stripWord] = wordDict.get(word,0) + 1
    return wordDict

def createWordFreqList(dictName, minFreq):
    wordList = []               
    for word,freq in wordDict.items():
        if freq > minFreq :
            wordList.append((word,freq))
    return wordList
    
wordList = []               
fileName = 'analysis.txt'
wordDict = createDict(fileName)
wordList = createWordFreqList(wordDict, 30)

wordList.sort(key = lambda x: x[0], reverse = False)
for item in wordList:
    col1, col2 = item
    print ( constantWidth(col1,30), starPlotter(col2), sep  = " | " )
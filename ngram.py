import os.path  # to checking file
import glob  # for file reading
from tkinter import *  # for removing punctuations
import time
start_time = time.time()

fileExist = True
if os.path.exists('result.txt') != fileExist:
    read_files = glob.glob("*.txt")

    with open("result.txt", "wb") as outfile:  # merge all txt's in one
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

with open('result.txt', 'r') as myFile:  # txt to String
    novelAsString = myFile.read()

exe = True    
while exe:
    n = int(input("Press 1 for Unigram, 2 for Digram, 3 for Trigram: "))  # take input

    wordsSplit = []  # firstly words will be splitted
    wordsCombined = []  # then will be combined according to selected ngram
    wordsCounted = []  # checked words will be gathered in this array
    counts = []  # this will control the number of frequencies

    text = novelAsString.lower()
    x = re.sub(r"[^\w\s]", "", text)  # remove punctuation characters
    wordsSplit = x.split()  # split and store in wordsSplit as a list
    returnString = "Total number of words = " + str(len(wordsSplit)) + "\n"  # will be the output

    for i in range(len(wordsSplit) - n + 1):
        j = i
        array = []
        for j in range(j, j + n, 1):  # making word combinations
            array.append(wordsSplit[j])
        temp = ""
        for j in range(len(array)):
            if j == 0:
                temp = array[j]
            else:
                temp = temp + " " + array[j]

        wordsCombined.append(temp)

    for i in range(len(wordsCombined)):
        controlrepeat = True
        counter = 0
        wordIsChecking = wordsCombined[i]  # select the word that will be checked
        if wordIsChecking in wordsCounted:  # if the word checked before, select another
            controlrepeat = False
        if controlrepeat:
            counter = wordsCombined.count(wordIsChecking)  # counter equals to frequency of word, will be at least 1
            if counter > 1:
                wordsCounted.append(wordIsChecking)
                counts.append(counter)

    counterNew = 1
    for i in range(100):
        numbersPrinting = max(counts)  # get the max frequency
        indexer = counts.index(max(counts))
        returnString = str(returnString) + str(counterNew) + ")" + str(wordsCounted[indexer]) + "--" + str(numbersPrinting) + "\n"
        wordsCounted.remove(wordsCounted[indexer])  # remove the printed word
        counts.remove(counts[indexer])  # remove word's frequency value
        counterNew = counterNew + 1
    print("Completion Time is " + str(time.time() - start_time) + " seconds for " + str(n) + "gram")
    print(returnString)


# -*- coding: utf-8 -*-
""" A4Q1Instructors

COMP 1012  SECTION A01/A02/A03
INSTRUCTOR Andres/Boyer/Janjic
ASSIGNMENT: A4 Question 1
AUTHOR    The Instructors
VERSION   2016-Feb-28

PURPOSE: To help someone become better at Scrabble®
"""
# imports
import random # to shuffle the letter list in tryLetters
import sys    # to use sys.exit to stop the program in one of the stubs
              # This import can be deleted later.
import time   # For timing user input as well as termination output

# constants
COUNTS = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2,
          2, 1, 2, 1) # quantity of each letter A to Z in Scrabble collection
MIN_WORD_LENGTH = 2 # shortest word to use in anagram
MAX_WORD_LENGTH = 15 # longest word to use in anagram
POINTS = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1,
          4, 4, 8, 4, 10) # Scrabble points for each letter A to Z
PRIMES = (2,  3,  5,  7,  11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 1) # prime
          # numbers used to create unique hash for each letter collection
REGISTERED = "\N{REGISTERED SIGN}" # registered trade mark sign
STOP = "Q" # input used to stop the program

# function definitions

#..........................................................................main
def main() :
    """main function that drives the program operations"""
    global allLetters, LETTERS, sampleSize, subscripts, timeOut
    print("WELCOME TO SCRABBLE%s TUTOR!" % REGISTERED)
    print("'Scrabble' is a registered trade mark of Hasbro, Inc.")
    print()
    print("Test your ability to find Scrabble words!")
    
    LETTERS = genCharRange('A','Z') # lowercase from 'a' to 'z'
    subscripts = list(genCharRange('₀','₉'))
    subscripts.append(subscripts[1] + subscripts[0])
    allLetters = genRepeatedChars(LETTERS, COUNTS) # list of Scrabble letters
    sampleSize = 7 # number of letters in Scrabble hand
    timeOut = 20 # [s] guessing time
    
    words = getWordList(MIN_WORD_LENGTH, MAX_WORD_LENGTH) # read word list; 
                                                         # print stats
    
    wordhashes = calcWordHashes(words) # calculate a hash for each word
    sortedHashes, wordGroups = groupWords(wordhashes, words) # sort the hashes
                                     # group words with the same hashes
                                     # print extreme cases
    
    result = doMenu(sortedHashes, wordGroups) # result is user choice
    
    while result != STOP :
        result = doMenu(sortedHashes, wordGroups)
      
    showTermination()
    return    
    
#............................................................... calcWordHashes
def calcWordHashes(words) :
    """hash each word by multiplying an appropriate prime number for
    each letter in the word. Return list of hashes."""
    wordhashes = [] # hashes for the words
    for word in words :
        word = word.lower()
        hashVal = 1 # hash for this specific word
        for letter in word.upper() : # calculate one letter at a time
            hashVal *= PRIMES[LETTERS.find(letter)] # nonletters have factor 1
        wordhashes.append(hashVal)
    return wordhashes

#.................................................................. filterWords
def filterWords(origHash, hashes, wordGroups) :
    """Eliminate hashes and corresponding word groups that do not divide
    evenly into origHash. Return the reduced lists of hashes and word
    groups."""
    newhashes = [] # hash values that divide evenly into origHash
    newWordGroups = [] # wordGroups corresponding to newHashes
    for loc, hashVal in enumerate(hashes) :
        useThisOne = origHash % hashVal == 0  # if True, a word to retain
        newhashes += useThisOne * [hashVal]
        newWordGroups += useThisOne * [wordGroups[loc]]
    return newhashes, newWordGroups

#..................................................................genCharRange
def genCharRange(firstChar, lastChar) :
    """Return a string containing every character from firstChar to
    lastChar inclusive."""
    letters =  [chr(num) for num in range(ord(firstChar), ord(lastChar) + 1)] #
               # list comprehension to produce characters from first to last
    return ''.join(letters)

#...................................................................getWordList
def getWordList(minLength, maxLength) :
    """Open a standard list of English words and return them in a list.
    minLength and maxLength are inclusive bounds on the length of word
    we want to keep."""
    filename = "twl06.txt" # name of word file, assumed in local folder
    flink = open(filename, 'r', encoding="utf-8") # link to input file
    print( "\nReading words from %s" % filename)
    words = [ ]            # word list
    for eachline in flink :
        text = eachline.strip()  # line contains one word
        # print(eachline, text)
        # text = text.replace('%','') # not needed with this file
        words += [text.upper()] * (minLength <= len(text) <= maxLength)
    flink.close()
    print( "%d words read: %s" % (len(words),', '.join(words[:6]+['...'])))
    return words

#................................................................... groupWords
def groupWords(hashes, words) :
    """Put both hashes and words in sorted order by hashes. Then group words
    that have the same hash, and return hashes and word groups. The hashes
    should be sorted, and each hash is unique. Each corresponding word group
    is formatted as a single string like this: 'baker|brake|break' """
    sortedPairs = sorted(zip(hashes,words)) # (hash, word) pairs sorted by hash
    sortedHashes = [] # unique hashes sorted in increasing order
    wordGroups = []  # groups of words with same hash, each as a list
    prevhash = 0 # hash for previous entry
    for hashVal, word in sortedPairs :
        newhash = hashVal != prevhash # new hash value found
        sortedHashes += newhash * [hashVal] # add new hash entry?
        wordGroups  += newhash * [[]]   # add new empty list of words?
        wordGroups[-1].append(word)
        prevhash = hashVal
    return sortedHashes, ['|'.join(group) for group in wordGroups]

#.............................................................. showTermination
def showTermination() :
    '''Print termination output, including author and date.'''
    print( "\nProgrammed by Edison Guillermo from Instructors")
    print( "Date: " + time.ctime())
    print( "End of processing")
    
#***************************** PUT YOUR CODE HERE *****************************

#...................................................................... display
def display(words, label) :
    print("-" * 82)
    wordList = list(words)
    newLine = 1
    print(label)
    print("\t", end ="")
    wordPoints = []
    for word in words:
        wordPoint = wordValue(word)
        wordPoints.append(wordPoint)
        print("%19s%4s%s" %((displayLetters(word),"(%d)" % (wordPoint),
                "\n\t" * (newLine % 3 == 0))), end="")
        
        newLine +=1
    print("\nBest word:", end ="")
    if len(wordList) > 0:
        bestWordVal = max(wordPoints)
        bestWord = displayLetters(wordList[wordPoints.index(bestWordVal)])
    else:
        bestWord = ""
        bestWordVal = 0
    
    print("\t %33s%4s" % (bestWord,"(%d)" % (bestWordVal)*(bestWordVal != 0)))
    return
    
#............................................................... displayLetters
def displayLetters(text) :
    text.replace(" ", "")
    newText = ""
    for letter in text:
        newText += letter + subscripts[POINTS[LETTERS.find(letter)]]
    return newText
    
#....................................................................... doMenu
def doMenu(hashes, wordGroups) :
    global sampleSize, timeOut
    cont = False
    
    
    whata = "Enter int n so that 7 <= n < 9 for number of letters to play: "
    whatb = "Enter int n so that 1 <= n < 121 for seconds to guess words: "
    while cont == False:
        print("Choose one of the following and enter the letter:")
        print("%4s a) change the number of random letters" % (" "))
        print("%4s b) change the time limit" % (" "))
        print("%4s c) try a new set of letters" % (" "))
        print("%4s q) quit" % (" "))
        cont = True
        userChoice = input()
        userChoice = userChoice.upper()
        if userChoice == "A":
            sampleSize = getInt(7,9, whata)
        elif userChoice == "B":            
            timeOut = getInt(1,121,whatb)
        elif userChoice == "C": 
            tryLetters(hashes, wordGroups)
        elif userChoice == "Q":
            pass
            
        else:
            print("\nInvalid response '%s'; try again" % (userChoice))
            cont = False
    return userChoice

#............................................................. genRepeatedChars
def genRepeatedChars(chars, repeats) :
    newChars=[]
    for letter in range(len(chars)):
        for repeater in range(repeats[letter]):
            newChars.append(chars[letter])
    return newChars

#.................................................................getInt
def getInt(lo, hi, what) :
    validInt = False    
    while validInt == False:
        numberStr = input(what)
        if not numberStr.isdigit():
            print("*** %s is not an int" % (numberStr))
        else:
            numberStr = int(numberStr)
            if lo > numberStr:
                print("*** %d is too small" % (numberStr))
            elif hi <= numberStr:
                print("*** %d is too big" % (numberStr))
            else:
                validInt = True
        
    return int(numberStr)

#..................................................................... getWords
def getWords(letters) :
    scoreLetters = displayLetters(letters)
    words = []
    timeTotal = 0
    print("Time limit: %d seconds" % (timeOut))
    while timeTotal <= timeOut:
        timea = time.time()
        word = input("Enter a word made from letters in %23s "%(scoreLetters))
        timeb = time.time()
        timeTotal += (timeb-timea)
        userWord = word.upper()
        words.append(userWord)
        
    word = set(words)
    
    
    return word

#................................................................... tryLetters
def tryLetters(hashes, wordGroups) :

    random.shuffle(allLetters)
    letters = allLetters [0:sampleSize]
    newLetters = ["".join(letters)]
    hashletters = calcWordHashes(newLetters)
    allWords = []
    
    newHashes,filteredLetters = filterWords(hashletters[0],hashes,wordGroups)
    for splitter in filteredLetters:
        word = splitter.split("|")
        allWords += word
    wordSet = set(allWords)
    userWords = getWords("".join(letters))
    invalidLet = userWords - wordSet 
    validLet = userWords.intersection(wordSet)
    print("Invalid user words: %s" % ", ".join(invalidLet))
    display(validLet,"Valid User Words:")
    display(wordSet,"Valid words:")
    """
    userIn = input("Press <Enter> to continue, <q> to quit:") 
    if  userIn.upper() == STOP :
        sys.exit() 
    """                                                   
    return

#.................................................................... wordValue
def wordValue(word) :  
    wordPoint = 0
    
    for letter in word:
        wordPoint += POINTS[LETTERS.find(letter)]
    
    return wordPoint 


main()
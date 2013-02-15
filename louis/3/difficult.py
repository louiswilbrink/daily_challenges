'''
[2/11/2012] challenge #3 [difficult]
Welcome to cipher day!

For this challenge, you need to write a program that will take the scrambled words from this post, and compare them against [THIS WORD LIST](http://pastebin.com/jSD873gL) to unscramble them. For bonus points, sort the words by length when you are finished. Post your programs and/or subroutines!

Here are your words to de-scramble:


'mkeart' 'sleewa' 'edcudls' 'iragoge' 'usrlsle' 'nalraoci' 'nsdeuto' 'amrhat' 'inknsy' 'iferkna'
'''
import os

wordBank = []

scrambled = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle', 'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']

# Read in word bank.
f = open('word_bank.txt', 'r')
for line in f:
  wordBank.append(line.rstrip())

# Check each scrambled word.
for word in scrambled:
  print "The scrambled word is %s" % word

  # Compare scrambled word to word bank.
  for checkWord in wordBank:
    
    # Split check string into a list of individual letters.
    checkLetters = list(checkWord)
    found = True

    # Check if every letter in the scrambled word is found in the check word.
    for letter in word:
      if (letter not in checkLetters):
        found = False
    if (found == True):
      print "UNSCRAMBLED: %s" % checkWord
      break

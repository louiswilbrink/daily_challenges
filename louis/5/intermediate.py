'''
Your challenge today is to write a program that can find the amount of anagrams within a .txt file. For example, "snap" would be an anagram of "pans", and "skate" would be an anagram of "stake".
'''

import string

# Load text from file.
f = open('I-have-a-dream.txt', 'r')
text = f.read()
f.close()

# Remove punctuation.
text = text.translate(string.maketrans("",""), string.punctuation)

# Split entire text into a list of words.
words = text.split(' ')
compareWords = words

# Collect anagrams in a dictionary.
anagrams = {}

def findAnagrams ():
  for word in words:
    letters = list(word)

    for compareWord in compareWords:

      # Set anagram flag.  Changes to False if any disqualifiers are encountered.
      isAnagram = True

      # Disqualify for being the same word or if comparing words of differing length.
      # We shant waste time on such trivialities.
      if (word == compareWord or len(word) != len(compareWord)):
        continue

      # For each word in the text, check if the same letters are found in the compare word.
      # This check needs to be two-way: 'seared' and 'sacred' only successfully compare ONE way.
      for letter in letters:
        if (letter not in compareWord):
          isAnagram = False

      # If still seemingly an anagram, check if all the letters in the compare word are found
      # in the current word.
      if (isAnagram):
        compLetters = list(compareWord)

        for compLetter in compLetters:
          if (compLetter not in word):
            isAnagram = False

        # This word/compareWord have passed all qualifiers and can confidently be
        # identified as anagrams.
        if (isAnagram):

          # First time we find an anagram for this word
          if (word not in anagrams):
            anagrams[word] = []
            anagrams[word].append(compareWord)

          # avoid saving the same compare word.
          elif (compareWord in anagrams[word]):
            continue

          # In this case, the word has at least one anagram already.  Append the the list.
          else:
            anagrams[word].append(compareWord)

print "This program will find anagrams within MLK Jr.'s famous 'I have a dream' speech\n"

findAnagrams()

print "Anagrams found!\n"
for word in anagrams:
  print word
  print anagrams[word]

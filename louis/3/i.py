'''
[2/11/2012] Challenge #3 [intermediate]
Welcome to cipher day! 

Create a program that can take a piece of text and encrypt it with an alphabetical substitution cipher. This can ignore white space, numbers, and symbols.

for extra credit, make it encrypt whitespace, numbers, and symbols!
'''

from random import randint

# Create substitution list.
def createSubstitutionCipher ():
  cipher = {}
  # Generate substitution pairs for 'A' through 'Z'
  for i in range(65, 91):
    found = False
    while (not found):
      randy = randint(65,90)
      if randy not in cipher.values():
        cipher[i] = randy
        found = True
  # Generate substitution pairs for 'a' through 'z'
  for i in range(97, 123):
    found = False
    while (not found):
      randy = randint(97, 122)
      if randy not in cipher.values():
        cipher[i] = randy
        found = True
  return cipher

# For each letter, return it's substitution for encryption.
def encryptThis(letter):
  ascVal = ord(letter);
  if (not letter.isalpha()):
    return letter 
  else:
    return chr(subCipher[ascVal])

# Main starts here.
text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.\n"

# Split text to single character list.
textList = list(text)

encryptedList = []

subCipher = createSubstitutionCipher()

# Encrypt each letter.
for letter in textList:
  encryptedList.append(encryptThis(letter))

print "\nORIGINAL TEXT: "
print text

print "generating substitution cipher..."

for i in subCipher:
  print "%s : %s" % (chr(i), chr(subCipher[i]))

print "\nENCRYPTED TEXT:"
print ''.join(encryptedList)

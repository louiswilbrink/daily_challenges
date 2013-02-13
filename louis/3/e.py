'''
[2/11/2012] Challenge #3 [easy]
Welcome to cipher day!

write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.

for extra credit, add a "decrypt" function to your program!
'''

cypher = 3

specialCases = {
                'a' : 'x',
                'b' : 'y',
                'c' : 'z',
                'A' : 'X',
                'B' : 'Y',
                'C' : 'Z'
               }

decryptCases = {
                'x' : 'a',
                'y' : 'b',
                'z' : 'c',
                'X' : 'A',
                'Y' : 'B',
                'Z' : 'C'
               }
              
text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

# Split text to single character list.
textList = list(text)

encryptedList = []
decryptedList = []

def encryptThis(letter):
  asciiValue = ord(letter)
  if (not letter.isalpha()):
    return letter 
  # If letter is a, b, c, etc. return x, y, z, etc.
  elif (letter in specialCases):
    encyptedLetter = specialCases[letter]
    return encyptedLetter
  else:
    newAsciiValue = asciiValue - cypher
    return chr(newAsciiValue)

def decryptThis(letter):
  asciiValue = ord(letter)
  if (not letter.isalpha()):
    return letter 
  # If letter is x, y, z, etc. return a, b, c, etc.
  elif (letter in decryptCases):
    decyptedLetter = decryptCases[letter]
    return decyptedLetter
  else:
    newAsciiValue = asciiValue + cypher
    return chr(newAsciiValue)

print "\nORIGINAL TEXT:"
print text

# Encrypt each letter.
for letter in textList:
  encryptedList.append(encryptThis(letter))

print "\nENCRYPTED TEXT:"
print ''.join(encryptedList)

cmd = raw_input("Would you like to decrypt this text? (yes/no): ")

if (cmd == 'yes'):
  for letter in encryptedList:
    decryptedList.append(decryptThis(letter))
  print "\nDECRYPTED TEXT:"
  print ''.join(decryptedList)

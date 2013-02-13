"""
[intermediate] challenge #2
create a short text adventure that will call the user by their name. The text adventure should use standard text adventure commands ("l, n, s, e, i, etc."). 

for extra credit, make sure the program doesn't fault, quit, glitch, fail, or loop no matter what is put in, even empty text or spaces. These will be tested rigorously!

For super extra credit, code it in C
"""

from random import choice

charisma = 1.0
targets = []
crew = []

def listActions ():
  print ""
  for action in nonObjActions:
    print action
  print ""

def dance ():
  print "\nGangnam Style comes on and you dance your ass off.  Everyone is impressed. (Charisma improves)\n"

def pushUps ():
  print "\nYou start doing push ups.  Everyone knows you're overcompensating for something.  What kind of loser are you? (Charisma plummets)\n"

def fart ():
  print "\nYou fart.  Your friends all laugh hysterically.\n"

def cry ():
  print "\nOMG you're crying.  You've lost all confidence and no girl would ever want to be with you.  You'll probably remember this night forever, blame everyone else for your problems, and die alone.\n"
  decision = 'quit'

def look ():
  targets.append(choice(girls))
  targets.append(choice(girls))
  targets.append(choice(girls))
  print "You scope out the joint and see %s, %s, and %s" % (targets[0], targets[1], targets[2])

def nope ():
  print "\nYou cannot perform this action.  You're game needs work..\n"

def quit ():
  print "\nYou exit the club like a pimp\n"

# Initialize variables.
intro = "\nYou enter the hottest bar in the city with your three best friends.  Time to own the night!\n"
decision = ''
objActions = [
   'approach',
   'ask a question to',
   'compliment',
   'harrass',
   'hit on',
   'make out with'
   'joke with'
   'move to'
  ]
nonObjActions = {
   'dance' : dance,
   'do push ups' : pushUps,
   'fart' : fart,
   #'laugh' : laugh,
   'cry' : cry,
   #'scream' : scream,
   #'stalk the club' : stalk,
   #'walk around' : walkAround,
   'look around' : look,
   'list' : listActions,
   'quit' : quit
  }
objs = [
   'a beer',
   'a martini',
   'a jameson and ginger ale', 
   'a sombrero',
   'some cash', 
   'a credit card', 
   'an ancient relic', 
   'an amulet', 
   'an engagement ring', 
   'some nachos', 
   'some onion rings', 
   'some french fries',
   'your number',
   'my number'
  ] 
girls = [ 
   'Kelly',
   'Michelle',
   'Natasha', 
   'Lindsey', 
   'Cara', 
   'Monique', 
   'Jennifer',
   'Mary'
  ]
guys = [
   'Tom Brady', 
   'Matt Forte', 
   'Adrian Peterson', 
   'Dave', 
   'Ralph', 
   'Tim',
   'Lyh',
   'Daeyou',
   'Gary'
  ]
characters = [girls, guys]
characterOrders = [
   'give me ',
   'dance with me',
   'pay for'
  ]
special = { 
           'list' : listActions,
           'quit' : quit
          }

print intro
while decision != 'quit':
  decision = raw_input("What do you want to do? (for a list of actions, you can type 'list'): ")
  nonObjActions.get(decision, nope)()

'''
[2/12/2012] Challenge #5 [easy]
Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given. 

For extra credit, have the user and password in a seperate .txt file.

for even more extra credit, break into your own program :)
'''

import json
from pprint import pprint

# Read login data from a secret file.
# Formatted in JSON.
json_file = open('secret.json')
data = json.load(json_file)
json_file.close()

loggedIn = False;

# Prompt the user for login credentials.  Loop until
# this matches login data from the secret file.
while (not loggedIn):
  user = raw_input("username: ")
  pw = raw_input("password: ")

  if (user == data["username"] and pw == data["password"]):
    loggedIn = True;
  else:
    print "Incorrect login credentials.  Try again (hounds released):"

print "You have successfully logged in!"

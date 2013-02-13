"""
[easy] challenge #1
  create a program that will ask the users name, age, and reddit username.
  have it tell them the information back, in the format:
  your name is (blank), you are (blank) years old, and your username is (blank)
  for extra credit, have the program log this information in a file to be accessed later.
"""

def reddit_display():
  
  name = raw_input("name: ");
  age = raw_input("age: ");
  redditUser = raw_input("reddit username: ");

  print "your name is %s, you are %s years old, and your username is %s" % (name, age, redditUser) 

  f = open('e.user_info', 'a')
  f.write("name: %s\nage: %s\nusername: %s\n\n" % (name, age, redditUser))
  f.close()

reddit_display();

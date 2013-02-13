"""
[intermediate] challenge #1
  create a program that will allow you to enter events organizable by hour. 
  There must be menu options of some form, and you must be able to easily edit, add, and delete events without directly changing the source code.

  (note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you how to use the program, it will probably be fine)
"""

def displaySchedule ():
  print "H: Event"
  for time, event in events.items():
    print "%s: %s" % (time, event)

def addEvent (): 
  time = raw_input("Enter a time the event will take place: ")
  event = raw_input("Enter the name of the event to add: ")
  events[time] = event

def editEvent ():
  displaySchedule()
  hour = raw_input("Enter the hour of the event you'd like to edit: ")
  change = raw_input("Would you like to change the time or event? enter 'time' or 'event': ")
  if change == 'time':
    newHour = raw_input("Enter the new time for this event: ")
    events[newHour] = events[hour]
    del events[hour]
  elif change == 'event':
    newEvent = raw_input("Enter the new event for this hour: ")
    events[hour] = newEvent
  print "Change is made, here is the new schedule:"
  displaySchedule()

def deleteEvent ():
  displaySchedule()
  hour = raw_input("Enter the hour of the event you'd like to delete: ")
  if hour in events:
    del events[hour]
    print "New schedule:"
    displaySchedule()
  else:
    print "No events take place in that hour."

# START HERE
# initialize variables
events = {
          '2' : 'appointment',
          '5' : 'dinner',
          '9' : 'date'
         }
menu = "Welcome to Events Organizer!\nYou can 'add', 'edit', 'delete', or 'view' events by typing the action, or type 'exit' to quit:\n"
options = {'add'    : addEvent,
           'edit'   : editEvent,
           'delete' : deleteEvent,
           'view'   : displaySchedule
          }
choice = ''

# Menu
while choice != 'exit':
  choice = raw_input(menu)
  options.get(choice, lambda: None)()

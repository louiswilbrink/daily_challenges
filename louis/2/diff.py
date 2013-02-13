'''
[difficult] challenge #2
Your mission is to create a stopwatch program. this program should have start, stop, and lap options, and it should write out to a file to be viewed later.
'''

from datetime import datetime

startTime = None
f = open('d.time_file', 'w')
cmd = raw_input("Type 'start' to being stopwatch: ");

if (cmd == 'start'):
  startTime = datetime.now()

while (cmd != 'stop'):
  cmd = raw_input("type 'stop' or 'lap' or press enter to see how much time has elapsed: ");
  if (cmd == ''):
    elapsedTime = datetime.now() - startTime
    print "Elapsed time: %s" % elapsedTime
    f.write("Elapsed time: %s\n" % elapsedTime)
  if (cmd == 'lap'):
    lapTime = datetime.now() - startTime
    print "************* LAP TIME ************"
    print "%s" % lapTime
    print "***********************************"
    f.write("************* LAP TIME ************\n%s\n***********************************\n" % lapTime)

stopTime = datetime.now() - startTime
print "************ STOP TIME ************"
print "Your time is: %s" % stopTime
print "***********************************"
f.write("************ STOP TIME ************\n%s\n***********************************\n" % stopTime)

f.close()

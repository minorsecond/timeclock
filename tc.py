# A timeclock program for project-based jobs
# Robert Ross Wardrup
# 08/31/2014

import time
import datetime
import sys
import csv
import os.path
import select

ABBREV      =   []
pName       =   []
sumtime     =   0
projTime    =   0
minuteCount     =   0
companyMinutes = 0

os.system('cls' if os.name == 'nt' else 'clear')

#initialize dictionary
times = {'Date' : 0, 'Day Start' : 0, 'Project Abbrev' : 0, 'Project Name' : 0, 'Project Start' : 0, 'Project End' : 0, 'Time Out': 0, 'Time In' : 0, 'Day End' : 0, 'ID' : 0}

#load csv writer for csv output in future)
if os.path.isfile("times.csv"):
    wr = csv.writer(open("times.csv", "a"))
else:
    wr = csv.writer(open("times.csv", "w"))
    columns = ["Date", "Day Start", "Project Abbrev", "Project Name", "Project Start", "Project End", "Time Out", "Time In", "Day End", "ID"]
    wr.writerow(columns)

def timer(): 
    seconds = 0
    minutes = 0
    hours = 0
    while True:

			sys.stdout.write("\r {hours} Hours {minutes} Minutes {seconds} Seconds".format(hours=hours, minutes=minutes, seconds=seconds))
			sys.stdout.flush()
			time.sleep(1)
			seconds = int(time.time() - time_start) - minutes * 60
                        if seconds >= 60:
				minutes += 1
				seconds = 0
                                minuteCount += 1
			if minutes >= 60:
				hours += 1
				minutes = 0
			if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
				raw_input()	
                                print '\n','What are you doing? (lunch, home, break, switch task)'
				answer = raw_input()
				timesOut = ["holder", Daybegin, ABBREV, pName, time_start, "placeholder", "placeholder", "placeholder","placeholder"," placeholder"]
                                wr.writerow(timesOut)
                                choices(answer)

#Trying to figure out how to round minutes to nearest 6 minutes. 
def companyTimer():
    if minuteCount % 6 > .5:
        companyMinutes = minuteCount + 1
    elif minuteCount % 6 < 5:
        companyMinutes = minuteCount - 1
    else:
        companyMinutes = minuteCount / 6
    return companyMinutes

def choices(answer):
	if answer == 'lunch':
		print 'Bon appetit'
		ltimeout = time.time()
		quit()
	elif answer == 'home':
		print 'Take care!'
		hometime = time.time()
		quit()
	elif answer == 'break':
		breaktime = time.time()
		quit()
	else:
		quit()

print "\n"
print "Hello there. I will log your project time and create a .csv file with the results."
print "Your current logged time for this week is: ", sumtime
print "\n"
print "-----------------------------------------------------------"
raw_input("Please press <ENTER> to log current time and begin your day")
print "\n"

Date = datetime.datetime.now().date()
Daybegin    =   datetime.datetime.now()
times['Date'] = str(Date)

raw_input("What are you working on? (ABBREV) ")
ABBREV = str(raw_input)
times['Project Abbrev'] = (ABBREV)

raw_input("What is the name of this project? ")
pName = str(raw_input)
times['Project Name'] = pName

print
time_start = time.time()


print "----------------------------------------------"
print "The day's start time is ", Daybegin
print "\n", 'Press enter to exit timer', '\n'

print "The project elapsed time is: "
timer()
print "The timesheet time elapsed is: "
companyTimer()

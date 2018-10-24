#################################
# Athena v003 - main module     #
# Adds additional information   #
# to alarm readout - news,      #
# weather, river level, bmi     #
# 16/10/2018                    #
#################################

import datetime
import subprocess
from greetingmodule001 import greeting
from datetimeparser001 import systemtimeparser
from datetimeparser001 import scheduletimeparser
from alarm001 import alarm01
from alarm001 import alarm02
from alarm001 import alarm03
from alarm001 import alarm04

current_datetime = datetime.datetime.now()
current_day = datetime.datetime.today().strftime('%A')
todays_schedule_name = str(current_datetime.year) + str(current_datetime.month) + str(current_datetime.day) + '.csv'

#print('Athena002 triggered: ' + str(current_datetime))
test_string='Athena003 triggered.'
#subprocess.call(['bash','/home/user/scripts/speech01.sh',test_string])
print(str(current_datetime.year) + str(current_datetime.month) + str(current_datetime.day))

user_details = {} # copy user details into memory as a dictionary
with open('/home/user/scripts/athena/user_details.csv') as f:
    for line in f:
        (key, val) = line.split(',')
        user_details[str(key)] = val.strip() # strip() function strips trailing whitespace *only* from values, i.e. the \n characters
    #test_string='User details read. '
    #subprocess.call(['bash','/home/user/scripts/speech01.sh',test_string])

full_schedule = [] # copy user schedule into memory as a 2d list
with open('/home/user/scripts/athena/myschedule/' + todays_schedule_name) as f:
    for line in f:
        full_schedule.append(line.strip().split(','))
    #test_string='Schedule read. '
    #subprocess.call(['bash','/home/user/scripts/speech01.sh',test_string])

for row in full_schedule: # check to see whether the current time matches any of the scheduled times
    #print(row)
    if row[2][0:5] == 'alarm' and (str(int(row[0][0:2])) + '.' + str(int(row[0][3:5]))) == (str(current_datetime.hour) + '.' + str(current_datetime.minute)): # triggers alarm module if alarm flag is set
        if row[2][5:7] == '01':
            alarm01(current_datetime, current_day, user_details, full_schedule)
        elif row[2][5:7] == '02':
            alarm02(current_datetime, user_details)
            schedule_alert_output_string = ' The current time is ' + str(systemtimeparser(current_datetime)) + ' and it\'s time for you to ' + row[1] + '.' # still need to give schedule updates after news bulletins
            subprocess.call(['bash','/home/user/scripts/speech01.sh',schedule_alert_output_string])
        elif row[2][5:7] == '03':
            #subprocess.call(['bash','/home/user/scripts/speech01.sh','alarm03 has been called'])
            alarm03(current_datetime, user_details)
        elif row[2][5:7] == '04':
            alarm04(current_datetime, user_details)

    elif (str(int(row[0][0:2])) + '.' + str(int(row[0][3:5]))) == (str(current_datetime.hour) + '.' + str(current_datetime.minute)): # single item timely announcements
        schedule_alert_output_string = greeting(current_datetime, user_details['nickname']) + ' The current time is ' + str(systemtimeparser(current_datetime)) + ' and it\'s time for you to ' + row[1] + '.'
        subprocess.call(['bash','/home/user/scripts/speech01.sh',schedule_alert_output_string])
        #print(schedule_alert_output_string)

#################################
# Athena alarm module v001      #
# Runs alarm processes when     #
# called                        #
# 16/10/2018                    #
#################################

import datetime
import subprocess
from greetingmodule001 import greeting
from datetimeparser001 import systemtimeparser
from datetimeparser001 import scheduletimeparser
from news001 import newsparser
from weather001 import weatherparser
from river001 import riverparser

####### for testing script as standalone:


######################## alarm01 ########################

def alarm01(current_datetime, current_day, user_details, full_schedule): # numbered so that multiple different alarms can potentially be designed depending upon weekdays/weekends etc

    greet_plus_datetime_output_string = greeting(current_datetime, user_details['nickname']) + ' The current time is ' + str(systemtimeparser(current_datetime)) + ' and today is ' + current_day + ' ' + str(current_datetime.day) + '/' + str(current_datetime.month) + '/' + str(current_datetime.year) + '.'
    subprocess.call(['bash','/home/user/scripts/speech01.sh',greet_plus_datetime_output_string])

    schedule__announcement_output_string = 'Your schedule for today is as follows:'
    subprocess.call(['bash','/home/user/scripts/speech01.sh',schedule__announcement_output_string])

    for row in full_schedule:
        schedule_parsed_time = scheduletimeparser(row[0])
        row_output_string = schedule_parsed_time + ': ' + row[1] + '.'
        subprocess.call(['bash','/home/user/scripts/speech01.sh',row_output_string])

    news_intro_output_string = 'The latest news headlines from the BBC are as follows.'
    subprocess.call(['bash','/home/user/scripts/speech01.sh',news_intro_output_string])

    news_stories = newsparser()

    for i in range(len(news_stories)):
        individual_story = news_stories[i][0] + news_stories[i][1]
        subprocess.call(['bash','/home/user/scripts/speech01.sh',individual_story])

    weather_output = weatherparser('alarm 1')

    for i in range(len(weather_output)):
        individual_weather = weather_output[i]
        subprocess.call(['bash','/home/user/scripts/speech01.sh',individual_weather])

    river_info = riverparser()

    for i in range(len(river_info)):
        individual_river_info = river_info[i]
        subprocess.call(['bash','/home/user/scripts/speech01.sh',individual_river_info])

    return()

#########################################################

#################### alarm02 - news #####################

def alarm02(current_datetime, user_details): # news headlines only

    greet_test_alarm02_output_string = greeting(current_datetime, user_details['nickname']) + ' The latest news headlines from the BBC are as follows.'
    subprocess.call(['bash','/home/user/scripts/speech01.sh',greet_test_alarm02_output_string])

    news_stories = newsparser()

    for i in range(len(news_stories)):
        individual_story = news_stories[i][0] + news_stories[i][1]
        subprocess.call(['bash','/home/user/scripts/speech01.sh',individual_story])

    return()

#########################################################

################### alarm03 - weather ###################

def alarm03(current_datetime, user_details): # weather only

    greet_test_alarm03_output_string = greeting(current_datetime, user_details['nickname'])
    subprocess.call(['bash','/home/user/scripts/speech01.sh',greet_test_alarm03_output_string])

    weather_output = weatherparser('alarm 3')

    for i in range(len(weather_output)):
        individual_weather = weather_output[i]
        subprocess.call(['bash','/home/user/scripts/speech01.sh',individual_weather])

    return()

#########################################################

#################### alarm04 - river ####################

def alarm04(current_datetime, user_details): # river only

    greet_test_alarm04_output_string = greeting(current_datetime, user_details['nickname'])
    subprocess.call(['bash','/home/user/scripts/speech01.sh',greet_test_alarm04_output_string])

    river_info = riverparser()

    for i in range(len(river_info)):
        individual_river_info = river_info[i]
        subprocess.call(['bash','/home/user/scripts/speech01.sh',individual_river_info])

    return()

#########################################################

####### for testing script as standalone ################

def test_alarm_behaviour():
    current_datetime = datetime.datetime.now()
    user_details = {} # copy user details into memory as a dictionary
    with open('/home/user/scripts/athena/user_details.csv') as f:
        for line in f:
            (key, val) = line.split(',')
            user_details[str(key)] = val.strip()

    alarm02(current_datetime, user_details) # put the alarm you want to test as a standalone here
    return()

#test_alarm_behaviour() # NB uncomment this line to trigger the above function when this script is run

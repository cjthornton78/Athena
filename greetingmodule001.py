#################################
# Athena greeting module v001   #
# Takes current time &          #
# user name & generates natural #
# greeting                      #
# 15/10/2018                    #
#################################

import subprocess

def greeting(current_datetime, user_name):

    #test_string='Greeting code reached. '
    #subprocess.call(['bash','/home/user/scripts/speech01.sh',test_string])

    greeting = 'Hello' # default greeting

    if current_datetime.hour < 12:
        greeting = 'Good morning ' + user_name + '.'

    elif current_datetime.hour < 18:
        greeting = 'Good afternoon ' + user_name + '.'

    else:
        greeting = 'Good evening ' + user_name + '.'

    return(greeting)

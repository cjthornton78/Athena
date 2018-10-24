#################################
# Athena datetime module v001   #
# Takes a datetime &            #
# parses it to natural          #
# language                      #
# 16/10/2018                    #
#################################

import subprocess

def systemtimeparser(input_datetime):

    #test_string='Sys timer code reached. '
    #subprocess.call(['bash','/home/user/scripts/speech01.sh',test_string])

    sys_parsed_time = 'TIME PARSING FAILURE'
    sys_am_pm = ''

    sys_parsed_hour = input_datetime.hour
    sys_parsed_minute = input_datetime.minute

    if input_datetime.hour > 11:
        sys_am_pm = 'PM'
        if input_datetime.hour > 12:
            sys_parsed_hour = input_datetime.hour - 12 # correct 24 hour time to 12 hour time
    elif input_datetime.hour < 1:
        sys_parsed_hour = 12 # change times from midnight to 1am to 12 hour time
        sys_am_pm = 'AM'
    else:
        sys_am_pm = 'AM'

    if input_datetime.minute == 0: # makes output say e.g. 2 PM instead of 2-oh-oh PM on the hours
        sys_parsed_minute = ''
    elif input_datetime.minute < 10: # makes output say oh for 3 oh 2 pm, rather than 3 2 pm as str() function strips leading zeroes
        sys_parsed_minute = ':0' + str(input_datetime.minute)
    else:
        sys_parsed_minute = ':' + str(input_datetime.minute)

    # TODO add specific responses for noon and midnight

    sys_parsed_time = str(sys_parsed_hour) + sys_parsed_minute + ' ' + sys_am_pm

    return(sys_parsed_time)

###############################################################

def scheduletimeparser(scheduletime):

    #test_string='Sched timer code reached. '
    #subprocess.call(['bash','/home/user/scripts/speech01.sh',test_string])

    sched_parsed_time = 'TIME PARSING FAILURE'
    sched_am_pm = ''

    sched_parsed_hour = scheduletime[0:2]
    sched_parsed_minute = scheduletime[3:5]

    if int(scheduletime[0:2]) > 11: # need to cast strings as ints for evaluation to work
        sched_am_pm = 'PM'
        if int(scheduletime[0:2]) > 12:
            sched_parsed_hour = str(int(scheduletime[0:2]) - 12)
    elif int(scheduletime[0:2]) < 1:
        sched_parsed_hour = str(12) # change times from midnight to 1am to 12 hour time
        sched_am_pm = 'AM'
    else:
        sched_am_pm = 'AM'
        sched_parsed_hour = str(int(scheduletime[0:2]))

    if scheduletime[3:5] =='00':
        sched_parsed_minute = ''
    else:
        sched_parsed_minute = ':' + scheduletime[3:5]

    sched_parsed_time = sched_parsed_hour + sched_parsed_minute + ' ' + sched_am_pm

    # TODO add specific responses for noon and midnight

    return(sched_parsed_time)

#################################
# Athena river module 001       #
# Collects latest river level   #
# from gov.uk and parses for    #
# Athena to read.               #
# 22/10/2018                    #
#################################

import urllib2
from bs4 import BeautifulSoup
import subprocess # only necessary for testing tts compatibility - can be commented out

def riverparser():

    url = 'https://flood-warning-information.service.gov.uk/station/9167'

    raw_page = urllib2.urlopen(url)

    soup = BeautifulSoup(raw_page, 'html.parser')

    station_name = soup.find(class_="intro").find(class_="heading-secondary").text.strip()

    water_level = soup.find(class_="intro").find_all(class_="bold-small")[0].text.strip()

    reading_time = soup.find(class_="intro").find_all(class_="bold-small")[1].text.strip()

    forecast = soup.find(class_="target-areas").find_all('p')[1].text.strip()

    river_info_output = []

    river_info_output.append("The water level of the " + station_name + " was " + water_level + " at " + reading_time + ".")
    river_info_output.append(forecast)

    #print(river_info_output[0] + " " + river_info_output[1])
    #subprocess.call(['bash','/home/user/scripts/speech01.sh',river_info_output[0]])
    #subprocess.call(['bash','/home/user/scripts/speech01.sh',river_info_output[1]])

    #return()
    return(river_info_output)

#riverparser() # runs function from this script for testing - uncomment to use

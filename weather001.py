# -*- coding: utf-8 -*-
#################################
# Athena weather module 001     #
# Collects latest local weather #
# and the forecast today for a  #
# specified location for Athena #
# to parse                      #
# 22/10/2018                    #
#################################

import urllib2
from bs4 import BeautifulSoup
import subprocess # only necessary for testing tts compatibility - can be commented out

def weatherparser(passing_module): # passing_module input is only present to try to figure out why this bit of script keeps triggering by itself - TODO - fix this weird, currently inexplicable behaviour

    url = 'https://www.wunderground.com/weather/gb/hebden%20bridge/53.7362432%2C-1.9873792' # wunderground.com weather info page url goes here

    raw_page = urllib2.urlopen(url)

    soup = BeautifulSoup(raw_page, 'html.parser')

    location = soup.find(class_="city-header").find(class_="columns small-12").find('h1').text.strip()

    current_temp_farenheit = soup.find(class_="current-temp").find(class_="wu-value wu-value-to").text.strip() # recursively drills down to the current temp, first by div, then by the span within that div, then strips the html to leave the number (farenheit, because america, so needs converting)

    current_temp_celsius = int((float(current_temp_farenheit) - 32) * (5.0 / 9.0))

    current_conditions = soup.find(class_="conditions-extra small-9 medium-5 columns small-centered medium-uncentered").find(class_="condition-icon small-6 medium-12 columns").text.strip().lower()

    current_wind_speed = soup.find(class_="conditions-extra small-9 medium-5 columns small-centered medium-uncentered").find(class_="condition-wind small-6 medium-12 columns").find(class_="wind-speed").text.strip()

    current_wind_direction_letters = soup.find(class_="conditions-extra small-9 medium-5 columns small-centered medium-uncentered").find(class_="condition-wind small-6 medium-12 columns").find('p').find('strong').text.strip()
    current_wind_direction = current_wind_direction_letters.replace('N', 'north ').replace('S', 'south ').replace('E', 'east ').replace('W', 'west ').strip() + 'erly' # turn a direction like NNW into something intelligible

    feels_like = ' with a ' # only add a 'feels like' statement to the current weather if it doesn't match the current temperature, otherwise it's a redundant statement
    feels_like_temp = int((float(soup.find(class_="feels-like").text.strip().replace('Feels like ', '')[0:2]) - 32) * (5.0 / 9.0))
    if feels_like_temp != current_temp_celsius:
        feels_like = ' but it\'s going to feel like ' + str(feels_like_temp) + ' degrees Celsius with a '
    else:
        print('feels like the temperature it really is right now') # testing only, can be commented out

    day_string = soup.find(class_="weather-quickie").text.strip()[0:3]
    if day_string == 'Tod': #today
        forecast_intro = soup.find(class_="weather-quickie").text.strip().lower().capitalize() + " and "
        tomorrow_intro = ''
    elif day_string == 'Tom': #tomorrow
        forecast_intro = "Tonight will be "# TODO - keep checking this still works in the evening & at night
        final_part_of_the_tomorrow_string = soup.find_all(class_="small-12 medium-4 large-3 columns forecast-wrap")[1].find_all(class_="module-link")[1].text.strip().split('.')[0].lower().replace('cloudy/wind', 'cloudy with wind') # when i try to evaluate this exact same code inline it screws everything up for some reason i can't work out - TODO - figure out why?
        #print('foo ' + soup.find_all(class_="small-12 medium-4 large-3 columns forecast-wrap")[1].find_all(class_="module-link")[1].text.strip().split('.')[0].lower() + ' fooo')
        print(final_part_of_the_tomorrow_string)
        tomorrow_intro = soup.find(class_="weather-quickie").text.strip().lower().capitalize().replace('.', '') + ' and ' + final_part_of_the_tomorrow_string + '.'
    else:
        print('unknown forecast time detected') # error response here
        forecast_intro = 'Unknown forecast time detected. '
        tomorrow_intro = ''

    forecast_conditions = soup.find_all(class_="small-12 medium-4 large-3 columns forecast-wrap")[0].find_all(class_="module-link")[1].text.strip().split('.')[0].lower() # man, i hope they don't change the names of their tags - really drilling down, splitting into lists, then drilling down again a ton here & with precipitation (below)

    forecast_precipitation = int(soup.find_all(class_="small-12 medium-4 large-3 columns forecast-wrap")[0].find_all(class_="hook")[0].text.strip().split('%')[0])

    check_forecast_high = soup.find(class_="hi-lo").find(class_="hi").text.strip()[0:2] # error check - the website changes the high to '--' in the afternoon as temperatures start to drop
    if check_forecast_high == '--':
        forecast_high_string = ''
    else:
        forecast_high = int((float(soup.find(class_="hi-lo").find(class_="hi").text.strip()[0:2]) - 32) * (5.0 / 9.0))
        if forecast_high == 1:
            forecast_high_string = '  a high of ' + str(forecast_high) + ' degree,' # use correct plural or singular form for degrees
        elif forecast_high == -1:
            forecast_high_string = '  a high of ' + str(forecast_high) + '  degree,'
        else:
            forecast_high_string = '  a high of ' + str(forecast_high) + '  degrees,'

    forecast_low = int((float(soup.find(class_="hi-lo").find(class_="lo").text.strip()[0:2]) - 32) * (5.0 / 9.0))
    if forecast_low == 1:
        forecast_low_string = str(forecast_low) + ' degree'
    elif forecast_low == -1:
        forecast_low_string = str(forecast_low) + ' degree'
    else:
        forecast_low_string = str(forecast_low) + ' degrees'

    weather_info = "The current weather in " + location + ", is " + str(current_temp_celsius) + " degrees celsius and " + current_conditions + feels_like  + current_wind_speed + "mph " + current_wind_direction + " wind." # TODO - check if wind speed is km/h or mph

    coming_forecast = forecast_intro.replace('.', '') + forecast_conditions + " with" + forecast_high_string + " a low of " + forecast_low_string + " and a " + str(forecast_precipitation) + " percent chance of precipitation. " + tomorrow_intro

    print(weather_info)
    print(coming_forecast)
    #print('test output')
    # subprocess.call(['bash','/home/user/scripts/speech01.sh','weather module called by' + passing_module])
    # subprocess.call(['bash','/home/user/scripts/speech01.sh',weather_info])
    # subprocess.call(['bash','/home/user/scripts/speech01.sh',coming_forecast])

    return([weather_info, coming_forecast])
    #return()

#weatherparser('self') # runs function from this script for testing - uncomment to use

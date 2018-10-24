#################################
# Athena news module 001        #
# Collects latest headlines     #
# from BBC news and parses for  #
# Athena to read.               #
# 16/10/2018                    #
#################################

import urllib2
from bs4 import BeautifulSoup

def newsparser():

    number_of_stories = 5 # NB minimum number of stories = 1
    news_stories = [['' for x in range(2)] for y in range(number_of_stories)] # initialises a blank 2d list for the stories, number_of_stories tall with a column for headlines and another for main stories

    url = 'https://www.bbc.co.uk/news'

    raw_page = urllib2.urlopen(url)

    soup = BeautifulSoup(raw_page, 'html.parser')

    main_headline_box = soup.find(class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text") # NB class_ needs an underscore after it in BeautifulSoup 4+, also soup.find() only finds the 1st instance on the page
    main_headline = main_headline_box.text.strip()
    #print(main_headline + '.')
    news_stories[0][0] = main_headline + '. ' # this seems to weirdly prepend the story with a 'u' character when the full list is output to the terminal, but when any individual element is displayed it gets stripped again so leaving for now

    main_story_box = soup.find(class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary") # finds first instance of a story box - always the main headline
    main_story = main_story_box.text.strip()
    news_stories[0][1] = main_story

    headlines_list_box = soup.find_all(class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text") # gets all sub headlines
    stories_list_box = soup.find_all(class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary") # actually includes first story as well, so needs to be skipped in range and offset applied to list referencing below

    for h in range(1,number_of_stories):
        #print(headlines_list_box[h].text.strip() + '. ' + stories_list_box[(h + 1)].text.strip())
        news_stories[h][0] = headlines_list_box[h].text.strip() + '. '
        news_stories[h][1] = stories_list_box[(h + 1)].text.strip()

    #print(news_stories)

    return(news_stories)

#newsparser() # runs function from this script for testing - uncomment to use

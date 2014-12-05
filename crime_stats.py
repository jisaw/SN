__author__ = 'jakesawyer'

import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter
import time
import webbrowser
import os

def main():
    url = 'http://data.cityofchicago.org/resource/ijzp-q8t2.json'
    r = requests.get(url)
    data = r.text

    df = pd.read_json(data)
    t = 0
    f = 0
    for i in df['arrest']:
        if i:
            t += 1
        if not i:
            f +=1
    print "Welcome to our MIS 407 project!"
    time.sleep(7)
    print("This is a little story about crime in the city of Chicago IL")
    time.sleep(7)
    print("This story is special though because it is automated!")
    time.sleep(7)
    print "The data and figures used in this story are calculated from a random grouping of 1000 crimes that happened in Chicago over the last year"
    time.sleep(7)
    print "This set of data is different every time you run this script"
    time.sleep(7)
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "Out of 1000 crimes that the Chicago Police responded to this year %s ended in arrests while %s didn't.\n" % (t, f)
    time.sleep(7)
    crime_per_community = Counter(df['block'])
    number = max(crime_per_community.values())
    maxcrime = max(crime_per_community)
    print "The block with the most crimes on it is %s, with a total of %s crimes from our 1000 random crime sample.\n" % (str(maxcrime).lower(), number)
    time.sleep(7)
    print "Here's a map of the block!"
    time.sleep(7)
    formatted_maxcrime = str(maxcrime).lower().replace('x', '0') + 'chicago il'
    webbrowser.open('http://maps.google.com/?q=%s' % formatted_maxcrime)
    time.sleep(7)
    max_loc = df['location_description']
    locals = []
    for i in df['location_description']:
        locals.append(i)
    locals = Counter(locals)
    loc = max(max_loc)
    print "A crime is most likely to happen in a %s environment.\n" % str(loc).lower()
    time.sleep(7)
    print "Take a look at the attached graph if you want some more info on where crime are most likely to take place in Chicago!\n"
    time.sleep(7)
    make_dict_bar_graph(locals)

    domestic_count = 0
    for i in df['domestic']:
        if i == True:
            domestic_count += 1
    domestic_crime_percent = (float(domestic_count)/1000.0)*100.0
    print "In the city of Chicago, from what our random of 1000 sample crimes says, " + str(domestic_crime_percent) +"%  of crimes are domestic.\n"
    time.sleep(7)
    print "That is %s domestic cases each year out of our sample size.\n" % domestic_count
    time.sleep(7)

    distCount = Counter(df['district'])
    typeCount = Counter(df['primary_type'])
    typeCommonKey = typeCount.most_common()

    make_dict_bar_graph(typeCount)

    print "Here you can see that the most occuring crime in Chicago is theft, so keep your valuables in a safe place!\n"
    time.sleep(7)
    
    communityCrime = Counter(df['community_area'])
    make_dict_bar_graph(communityCrime)
    
    most_common_dist = communityCrime.most_common()
    most_common_dist = most_common_dist[0]

    print "Moving on to the next graph, you can see that community %s is involved with the most crime by almost double the amount of the next highest, with %s crimes.\n" % (most_common_dist[0], most_common_dist[1])
    time.sleep(7)
    print "It's also interesting to note that the neighboring communities also have a consistent crime rate."
    time.sleep(7)
    
    locationCount = Counter(df['location_description'])
    
    make_dict_bar_graph(locationCount)
    
    print "Now as you can see, a majority of these crimes appear to occur mostly in the streets, followed by residence and apartments.\n"
    time.sleep(7)

    print "To end this story I would like to leave you to play with our very own interactive map of Chicago Crime"
    time.sleep(7)
    current_dir = os.getcwd()
    webbrowser.open('file://%s/chiCrimesCircles.html' % current_dir)

def make_dict_bar_graph(data):
    plt.bar(range(len(data)), data.values())
    plt.xticks(range(len(data)), data.keys(), rotation=90)
    matplotlib.rc('xtick', labelsize=9)
    plt.show()

if __name__ == "__main__":
    main()
__author__ = 'jakesawyer'

import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter
import time
import webbrowser
import os

def get_df():
    url = 'http://data.cityofchicago.org/resource/ijzp-q8t2.json'
    r = requests.get(url)
    data = r.text
    df = pd.read_json(data)
    return df

def arrests(df):
    t = 0
    f = 0
    for i in df['arrest']:
        if i:
            t += 1
        if not i:
            f +=1
    return "Out of 1000 crimes that the Chicago Police responded to this year %s ended in arrests while %s didn't.\n" % (t, f)

def most_dangerous_block(df):
    crime_per_community = Counter(df['block'])
    number = max(crime_per_community.values())
    maxcrime = max(crime_per_community)
    result =  "The block with the most crimes on it is %s, with a total of %s crimes from our 1000 random crime sample.\n" % (str(maxcrime).lower(), number)
    return result

def most_dangerous_block_url(maxcrime):
    formatted_maxcrime = str(maxcrime).lower().replace('x', '0') + 'chicago il'
    return 'http://maps.google.com/?q=%s' % formatted_maxcrime
    
def worst_place(df):
    max_loc = df['location_description']
    locals = []
    for i in df['location_description']:
        locals.append(i)
    locals = Counter(locals)
    loc = max(max_loc)
    result =  "A crime is most likely to happen in a %s environment.\n" % str(loc).lower()
    return result

def worst_place_graph(df):
    max_loc = df['location_description']
    locals = []
    for i in df['location_description']:
        locals.append(i)
    locals = Counter(locals)
    return make_dict_bar_graph(locals)

def domestic(df):
    domestic_count = 0
    for i in df['domestic']:
        if i == True:
            domestic_count += 1
    domestic_crime_percent = (float(domestic_count)/1000.0)*100.0
    result =  "In the city of Chicago, from what our random of 1000 sample crimes says, " + str(domestic_crime_percent) +"%  of crimes are domestic." + "That is %s domestic cases each year out of our sample size.\n" % domestic_count
    return result

def theft(df):
    return "Here you can see that the most occuring crime in Chicago is theft, so keep your valuables in a safe place!\n"

def theft_graph(df):
    distCount = Counter(df['district'])
    typeCount = Counter(df['primary_type'])
    typeCommonKey = typeCount.most_common()

    return make_dict_bar_graph(typeCount)

def community(df):
    communityCrime = Counter(df['community_area'])
    
    most_common_dist = communityCrime.most_common()
    most_common_dist = most_common_dist[0]

    return "Moving on to the next graph, you can see that community %s is involved with the most crime by almost double the amount of the next highest, with %s crimes.\n" % (most_common_dist[0], most_common_dist[1])

def community_graph():
    make_dict_bar_graph(communityCrime)

def location_graph():
    locationCount = Counter(df['location_description'])
    
    return make_dict_bar_graph(locationCount)


def make_dict_bar_graph(data):
    plt.bar(range(len(data)), data.values())
    plt.xticks(range(len(data)), data.keys(), rotation=90)
    matplotlib.rc('xtick', labelsize=9)
    return plt

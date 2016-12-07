#import numpy
import json

#global dictionary
pdict = {}

#opens the json file and creates a dictionary
def parse_and_dict():
    #just change the filename to read the whole json
    #working on a smaller subset to save speed
    json1_file = open('bbjson3.json')
    json1_str = json1_file.read()

    #json.loads turns the json into a list of dictionaries
    json1_data = json.loads(json1_str) #gets the whole dictionary


    for player in json1_data:
        pname = player['name']
        pdict[pname] = player
        pseason = str(player['season']) #season is treated as an int
        pmhs = player['max_hit_speed']
        print "in " + pseason + ", " + pname + " had max hit speed of " + pmhs
#end parse_and_dict


#the main machine
def main():
#dictionary is a lot faster than list
#will be useful when updating a player's FA stats
#dictionary AO(1) speed to update
#list is O(n) update
    parse_and_dict()
    gs1 = pdict['Giancarlo Stanton']
    print str(gs1['name']) + " had an average speed of " + str(gs1['gb']) + " mph on his groundballs"

#end main

main()

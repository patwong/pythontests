#import numpy
import json

# global dictionary
pdict = {}

# opens the json file and creates a dictionary
def parse_and_dict():
    # just change the filename to read the whole json
    # working on a smaller subset to save speed
    json1_file = open('bbjson3.json')
    json1_str = json1_file.read()

    # json.loads turns the json into a list of dictionaries
    json1_data = json.loads(json1_str)  # gets the whole dictionary



    for player in json1_data:
        pname = player['name']

        # to int: avg_distance, avg_hr_distance, batter, max_distance, player_id
        player['avg_distance'] = int(player['avg_distance'])
        player['avg_hr_distance'] = int(player['avg_hr_distance'])
        player['batter'] = int(player['batter'])
        player['max_distance'] = int(player['max_distance'])
        player['player_id'] = int(player['player_id'])

        # to float: avg_hit_speed, brl_pa(%), brl_percent(%), fbld, gb, max_hit_speed, min_hit_speed
        player['avg_hit_speed'] = float(player['avg_hit_speed'])
        player['brl_pa'] = float(player['brl_pa'].strip('%')) / 100
        player['brl_percent'] = float(player['brl_percent'].strip('%')) / 100
        player['fbld'] = float(player['fbld'])
        player['gb'] = float(player['gb'])
        player['max_hit_speed'] = float(player['max_hit_speed'])
        player['min_hit_speed'] = float(player['min_hit_speed'])

        # to bool: freeagent
        if player['freeagent'].lower() == 'true':
            player['freeagent'] = True
        else:
            player['freeagent'] = False

        pdict[pname] = player
        pseason = str(player['season'])     # season is treated as an int
        pmhs = player['max_hit_speed']
        print "in " + pseason + ", " + pname + " had max hit speed of " + str(pmhs)
# end parse_and_dict


# the main machine
def main():
    # dictionary is a lot faster than list
    # will be useful when updating a player's FA stats
    # dictionary AO(1) speed to update
    # list is O(n) update
    parse_and_dict()
    gs1 = pdict['Giancarlo Stanton']
    print str(gs1['name']) + " had an average speed of " + str(gs1['gb']) + " mph on his groundballs"

# end main

main()

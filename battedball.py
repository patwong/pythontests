import json

#global dictionary
pdict = {}

def parse_and_dict():
    json1_file = open('bbjson3.json')
    json1_str = json1_file.read()

    #json.loads turns the json into a list of dictionaries
    json1_data = json.loads(json1_str) #gets the whole dictionary


    #neatly outputs the list
    #abd = json.dumps(json1_data, indent=4, separators=(',', ': '))
    #outfile = open('outtest2.txt', 'w')
    #outfile.write(abd)


    gs = json1_data[0] #gets giancarlo stanton


    #print json1_data #prints the whole dictionary
    print gs['name'] #prints out 'Giancarlo Stanton'
    print gs['brl_pa']

    #rp2 = json1_data[2] #tyler flowers? yes

    for player in json1_data:
        pname = player['name']
        pdict[pname] = player
        pseason = str(player['season']) #season is treated as an int
        pmhs = player['max_hit_speed']
        print "in " + pseason + ", " + pname + " had max hit speed of " + pmhs
#end parse_and_dict

def main():
    parse_and_dict()
    gs1 = pdict['Giancarlo Stanton']
    print str(gs1['name']) + " had an average speed of " + str(gs1['gb']) + " mph on his groundballs"

#end main

main()

#ccsmhs = float(rp1mhs) * 2 #cast to float, mult by 2
#print str(ccsmhs)

#####################################################################

######################### WORKS!!!!!!!!!!!!!!!!! ####################

#tests on the whole dictionary/json
#json2_file = open('out.txt')
#json2_str = json2_file.read()
#json2_data = json.loads(json2_str)
#rp1 = json2_data[43] #chris carter
#rp1name = rp1['name']
#season = rp1['season'] #season is treated as an int
#rp1mhs = rp1['max_hit_speed']
#
#print rp1['name']
#print "in " + str(rp1['season']) + ", " + rp1name + " had max hit speed of " + rp1mhs

#ccsmhs = float(rp1mhs) * 2 #cast to float, mult by 2
#print str(ccsmhs)

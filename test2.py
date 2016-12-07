import json

json1_file = open('bbjson3.json')
json1_str = json1_file.read()

json1_data = json.loads(json1_str) #gets the whole dictionary
gs = json1_data[0] #gets giancarlo stanton


#print json1_data #prints the whole dictionary
print gs['name'] #prints out 'Giancarlo Stanton'
print gs['brl_pa']

rp2 = json1_data[2] #tyler flowers?
rp2name = rp2['name']
season = rp2['season'] #season is treated as an int
rp2mhs = rp2['max_hit_speed']

print rp2['name']
print "in " + str(rp2['season']) + ", " + rp2name + " had max hit speed of " + rp2mhs

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

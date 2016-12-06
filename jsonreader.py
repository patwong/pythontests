import json

f = open('out.txt', 'w')
with open('bbjson.json') as json_data:
    d = json.load(json_data)
    abd = json.dumps(d, sort_keys=True,indent=4,separators=(',', ': '))
    #print abd #works!!!!
    f.write(abd)

#json.dumps({"name":"Giancarlo Stanton","attempts":248,"max_hit_speed":"123.9","min_hit_speed":"41.1","avg_hit_speed":"95.1","fbld":"97.4","gb":"94.6","max_distance":"504","avg_distance":"234","avg_hr_distance":"422","player_id":"519317","player_type":"batter","season":2016,"batter":"519317","barrels":43,"brl_percent":"17.3%","brl_pa":"9.1%","rowId":"row_519317","freeagent":"false"})

####works!!!!####
#jsonstring = '{"name":"Giancarlo Stanton","attempts":248,"max_hit_speed":"123.9","min_hit_speed":"41.1",' \
#             '"avg_hit_speed":"95.1","fbld":"97.4","gb":"94.6","max_distance":"504","avg_distance":"234",' \
#             '"avg_hr_distance":"422","player_id":"519317","player_type":"batter","season":2016,"batter":"519317",' \
#             '"barrels":43,"brl_percent":"17.3%","brl_pa":"9.1%","rowId":"row_519317","freeagent":"false"}'

#parsed_json = json.loads(jsonstring)
#print(parsed_json['brl_pa'])
import json

with open("chefmozhours4_final.json") as json_file:
    data = json.load(json_file)




# keys, values = [k for k, v in schedule.items()], [v for k, v in schedule.items()]
with open('chefmozhours4_final_final.json', 'w') as outfile:
    json.dump(data, outfile)
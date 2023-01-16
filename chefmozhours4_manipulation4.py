import json

with open("chefmozhours4_final.json") as json_file:
    data = json.load(json_file)

result = []
for x in data:
    hours = []
    x['days'] = list(set(x['days']))
    if x['hours'] == '00:00-00:00': continue
    for i in range(len(x['days'])):
        hours.append(x['hours'])
    x['hours'] = hours
    result.append(x)

# keys, values = [k for k, v in schedule.items()], [v for k, v in schedule.items()]
with open('chefmozhours4_final_final.json', 'w') as outfile:
    json.dump(result, outfile)
import json

with open('data.txt') as json_file:
  data = json.load(json_file)
  for d in data:
    print(data[d])
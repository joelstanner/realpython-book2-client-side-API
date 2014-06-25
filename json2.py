# json parsing 2


import json

# decode the json file

output = json.load(open('cars.json'))

# display output to the screen
print output[0]["CAR"][0]["MODEL"]
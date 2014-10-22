import json


tweets = []

for line in open('tstream.json'):
  try: 
    tweets.append(json.loads(line))
  except:
	pass

	
for item in tweets:



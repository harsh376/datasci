import json

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

#print scores.items() # Print every (term, score) pair in the dictionary

tweets = []

for line in open('turn_in.json'):
  try: 
    tweets.append(json.loads(line))
  except:
	pass

# tweets[13]: 'dict' type

results = []
for tweet_data in tweets:      						# tweet_data: 'dict' type
    
	if 'text' in tweet_data:
		results.append( tweet_data['text'])

#print len(results)  length: 14


count = 1
for item in results:
	#print type(item)
	print item.encode('utf-8')
	words = (item.encode('utf-8')).split()
	sum = 0
	for w in words:
		if(scores.has_key(w)):
			sum = sum + scores[w]
	
	print "tweet score:"+str(sum)
	count+=1
	
	
		

	





	
	
	

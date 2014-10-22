import sys
import json
import operator

stateScore = {}					# {state,sentiment score}
scores = {}
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
		
    for line in tweet_file:
        t = json.loads(line)					# t: each line(tweet info) is of 'dict' type
        if t.has_key('place') and t['place'] and t['place']['country_code']=='US':
            state = (t['place']['full_name'].encode('utf-8'))[-2:]
            if stateScore.has_key(state):
                stateScore[state] = stateScore[state]+sentScore(extractTweet(line))  
            else:
                stateScore[state] = sentScore(extractTweet(line))		
    #print stateScore
    highest()    

def highest():
    print max(stateScore.iteritems(), key=operator.itemgetter(1))[0]
        

	
def extractTweet(line):					# tweet as a list
	lineInJson = json.loads(line)
	if 'text' in lineInJson.keys():		#Test if the result is a tweet            
		tweet = lineInJson['text'].encode('utf-8').split()		# tweet: is broken down 
	return tweet

	
def sentScore(tweet1):					# actual tweet
        sum = 0
        for each in tweet1:
			if(scores.has_key(each)):
				sum = sum + scores[each]
        return sum 

		
	
	
if __name__ == '__main__':
    main()
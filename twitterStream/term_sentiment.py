import sys
import json

scores = {}
tweetsString = {}
newTerms=[]
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def extractTweet(line):					# tweet as a list
	lineInJson = json.loads(line)
	if 'text' in lineInJson.keys():		#Test if the result is a tweet            
		tweet = lineInJson['text'].encode('utf-8').split()		# tweet: is broken down 
	return tweet
	
def extractTweet1(line):				# tweet as a string
	lineInJson = json.loads(line)
	if 'text' in lineInJson.keys():		#Test if the result is a tweet            
		tweet = lineInJson['text'].encode('utf-8')		# tweet as a string 
	return tweet

def first():
    for item in newTerms:
        sum=0
        for tweet in tweetsString:					# tweet is the key in tweetsString
            if item in tweet:					
		        sum+=tweetsString[tweet]
        print item+" "+str(float(sum))
	            
		    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    """hw()
    lines(sent_file)
    lines(tweet_file)"""
   
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        t1 = extractTweet1(line)			# string: for dict- t1:sentScore
        t2 = extractTweet(line)				# list: for calculating sentScore
        for item in t2:
            if termScore(item)==0:
		        newTerms.append(item)
        tweetsString[t1]=sentScore(t2)		# (tweet,tweet score) in tweetsString dict
    #print newTerms
    #print tweets
    	
    first()


			
def termIsPresent(term,tweet):			
	for item in tweet:
		if (item == term):
			return True
	return False
		
def termScore(term1):			# returns score of the term from the dict 'score'
	if(scores.has_key(term1)):
		return scores[term1]
	else:
		return 0


		
def sentScore(tweet1):					# tweet1: actual tweet as a list
        sum = 0
        for each in tweet1:
			if(scores.has_key(each)):
				sum = sum + scores[each]
        return sum        

if __name__ == '__main__':
    main()

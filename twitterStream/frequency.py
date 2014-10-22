import sys
import json

termFreq = {}
termList = []					# stores all the words in a list

def extractTweet(line):					# tweet as a list
	lineInJson = json.loads(line)
	if 'text' in lineInJson.keys():		#Test if the result is a tweet            
		tweet = lineInJson['text'].encode('utf-8').split()		# tweet: is broken down 
	return tweet

def main():
    tweet_file = open(sys.argv[1])
    #print type(tweet_file)
    ct=0								# counter for total number of terms
    for line in tweet_file:
        t = extractTweet(line)
        for item in t:
	        termList.append(item)
	        ct+=1
    
    for item in termList:
        termFreq[item] = (termList.count(item))/(float)(ct)
	
    for item in termFreq:
        print item + " " + str(termFreq[item])







if __name__ == '__main__':
    main()
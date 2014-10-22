import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #my_file = open("stdout.json","w")
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file: 
        lineInJson = json.loads(line)		#convert to JSON
        if 'text' in lineInJson.keys():		#Test if the result is a tweet            
            tweet = lineInJson['text'].encode('utf-8').split() 
            sum = 0
            for each in tweet:
                if(scores.has_key(each)):
                    sum = sum + scores[each]
            print str(float(sum))
				#my_file.write(str(float(sum))+"\n")
    #my_file.close()	   
			
    #lines(sent_file)
    #lines(tweet_file)

	
	

if __name__ == '__main__':
    main()

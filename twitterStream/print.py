import sys
import json
import operator

hashtagCount = {}
topten = []

def main():
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        t = json.loads(line)
        print t.keys
        # if t.has_key('entities'):
            # for item in(t['entities']['hashtags']):
            	# print item

		
if __name__ == '__main__':
    main()
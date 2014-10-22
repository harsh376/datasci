import sys
import json
import operator

hashtagCount = {}
topten = []

def main():
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        t = json.loads(line)
        if t.has_key('entities'):
            for item in(t['entities']['hashtags']):
                if hashtagCount.has_key(item['text']):
	                hashtagCount[item['text']] = hashtagCount[item['text']] + 1
                else:
                    hashtagCount[item['text']] = 1
    for i in range(10):
        h = highest()
        print h + " " + str(float(hashtagCount[h]))
        topten.append(h)
        del hashtagCount[h]		
    #print hashtagCount
    #highest()
    #print topten
		
def highest():
    return max(hashtagCount.iteritems(), key=operator.itemgetter(1))[0]

		
if __name__ == '__main__':
    main()
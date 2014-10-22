import json

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.
"""
d1={'one':1,'two':2,'three':3}
print len(d1)
print d1.keys()
"""
item = "@shrey7 accepted accepting accepts accident accidental htsg http://harshverma.com"
print item.encode('utf-8')
words = (item.encode('utf-8')).split()
sum = 0
for w in words:
	if(scores.has_key(w)):
		sum = sum + scores[w]
print str(sum)


"""
accepted	1
accepting	1
accepts	1
accident	-2
accidental	-2
"""


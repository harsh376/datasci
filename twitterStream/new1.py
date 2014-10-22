s=['hello','how','are','you']

def termIsPresent(term1,tweet1):
	for item in tweet1:
		print item
		if (item == term1):
			return True
	return False
	
if termIsPresent("how",s):
	print "found"
else:
	print "not found"
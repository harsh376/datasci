import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    row = record[1]
    col = record[2]
    value = record[3]

    if matrix == 'a':
        for k in range(5):
            mr.emit_intermediate((row,k),(col,value))
    elif matrix == 'b':
        for i in range(5):
            mr.emit_intermediate((i,col),(row,value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    sum=0
    for i in range(len(list_of_values)):
        a1=list_of_values[i][1]
        b1=0
        for j in range(i,len(list_of_values)):
            if list_of_values[i][0]==list_of_values[j][0] and i!=j:
                b1=list_of_values[j][1]
                break			
        sum+=(a1*b1)	
		
    mr.emit((key[0],key[1],sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

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
    key = record[1]
    mr.emit_intermediate(key,record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    ct = len(list_of_values)
    for i in range(1,ct):
        mr.emit(list_of_values[0]+list_of_values[i])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

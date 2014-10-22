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
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.intermediate.setdefault(value,[])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for item in list_of_values:
        if key not in mr.intermediate[item]:
            mr.emit((key,item))
            mr.emit((item,key))
    #mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

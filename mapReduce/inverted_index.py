import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):							# record : line by line ["docid",text]
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()					# words : array i.e  ["hello","how","are"]
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #for v in list_of_values:
    #  total += v
    output = []
    for x in list_of_values:
        if x not in output:
            output.append(x)
    mr.emit((key, output))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

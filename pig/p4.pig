register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD '$INPUT' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the objects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;


g = group count_by_subject by (count);
h = foreach g generate flatten(group), COUNT($1);
c = group h all;
ct = foreach c generate COUNT(h);

-- store ct into 'results/' using PigStorage();

store ct into '$OUTPUT';


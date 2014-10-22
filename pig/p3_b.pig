register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- filtering the data
ntriples1 = filter ntriples by (subject matches '.*rdfabout\\.com.*');

-- duplicating the filtered data
ntriples2 = foreach ntriples1 generate subject as subject2, predicate as predicate2, object as object2;

-- joining the two data 
n = JOIN ntriples1 BY object, ntriples2 BY subject2;

-- removing duplicates
n = DISTINCT n;

-- counting the number of records
n_group = group n all;
n_count = foreach n_group generate COUNT(n);

-- store the final count
store n_count into 'results/' using PigStorage();
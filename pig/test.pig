register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

subjects_countTuples = group ntriples by (subject);

-- count : <subject> <2>
count = foreach subjects_countTuples generate flatten($0), COUNT($1) as count PARALLEL 50;			

-- <tuple count> <number of subjects>
tupleCount_subjectCount = group count by (count);

-- count the number of subjects in the bag now

y = foreach tupleCount_subjectCount generate flatten($0),COUNT($1) as ct PARALLEL 50;

store y into 'results1a/' using PigStorage();




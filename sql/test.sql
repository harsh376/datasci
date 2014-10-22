
DROP TABLE dt;

CREATE TABLE dt(
docid VARCHAR(255),
term VARCHAR(255),
count int,
PRIMARY KEY(docid,term));

INSERT INTO dt(docid,term,count)
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

DROP TABLE dt1;

CREATE TABLE dt1(
docid VARCHAR(255),
term VARCHAR(255),
count int,
PRIMARY KEY(term,docid));

INSERT INTO dt1(term,docid,count)
SELECT term,docid,count FROM dt;
 
SELECT sum(dt.count*dt1.count) FROM dt,dt1 WHERE dt.docid='q' AND dt1.docid!='q' AND dt.term=dt1.term;



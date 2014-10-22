/*SELECT * FROM Frequency;*/

DELETE FROM Frequency 
WHERE docid='q';

INSERT INTO Frequency(docid, term, count)
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

DROP TABLE dt;

CREATE TABLE dt
(
term VARCHAR(255),
docid VARCHAR(255),
count int,
PRIMARY KEY(term, docid));

INSERT INTO dt (term, docid, count)
SELECT term, docid, count
FROM Frequency;

select max(Frequency.count*dt.count) from Frequency,dt where Frequency.term=dt.term and (Frequency.docid="q" and dt.docid!="q");

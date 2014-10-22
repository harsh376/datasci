/*SELECT * FROM Frequency;*/
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

/*SELECT * FROM dt;*/

/*select sum(a.value*b.value) from a,b where a.col_num=b.row_num and a.row_num=2 and b.col_num=3;*/

select sum(Frequency.count*dt.count) from Frequency,dt where Frequency.term=dt.term and Frequency.docid="10080_txt_crude" and dt.docid="17035_txt_earn";

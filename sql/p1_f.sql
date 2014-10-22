select count(distinct d1)
from (select docid as d1 from Frequency where term="world"),
(select docid as d2 from Frequency where term="transactions")
where d1=d2;

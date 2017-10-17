-- List number of records with same score in table, second_table, in database hbtn_0c_0
SELECT score, COUNT(score) FROM second_table AS C
GROUP BY score
ORDER BY score DESC;

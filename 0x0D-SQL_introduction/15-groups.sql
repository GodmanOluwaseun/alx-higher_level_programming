-- List count of recods with same score.
SELECT COUNT(DISTINCT score), id
FROM second_table
ORDER BY score DESC;

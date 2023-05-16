-- Script: List the number of records with the same score in the table second_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- List the number of records for each score
SELECT score, COUNT(*) AS number
FROM @database_name.second_table
GROUP BY score
ORDER BY number DESC;


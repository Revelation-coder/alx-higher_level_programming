-- Script: List records with score >= 10 in the table second_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- List records with score >= 10
SELECT score, name
FROM @database_name.second_table
WHERE score >= 10
ORDER BY score DESC;


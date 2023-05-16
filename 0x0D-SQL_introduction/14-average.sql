-- Script: Compute the average score of all records in the table second_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Compute the average score
SELECT AVG(score) AS average
FROM @database_name.second_table;


-- Script: List all records of the table second_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- List all records
SELECT score, name
FROM @database_name.second_table
ORDER BY score DESC;


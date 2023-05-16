-- Script: List all records from the table second_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- List all records with score and name
SELECT score, name
FROM @database_name.second_table
WHERE name IS NOT NULL
ORDER BY score DESC;


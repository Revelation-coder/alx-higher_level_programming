-- Script: Remove records with score <= 5 in the table second_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Remove records with score <= 5
DELETE FROM @database_name.second_table
WHERE score <= 5;


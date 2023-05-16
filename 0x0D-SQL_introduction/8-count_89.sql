-- Script: Display the number of records with id = 89 in the table first_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Count the number of records
SELECT COUNT(*)
FROM @database_name.first_table
WHERE id = 89;

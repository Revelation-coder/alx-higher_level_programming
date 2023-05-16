-- Script: Update the score of Bob to 10 in the table second_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Update the score of Bob
UPDATE @database_name.second_table
SET score = 10
WHERE name = 'Bob';


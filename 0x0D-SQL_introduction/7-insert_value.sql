-- Script: Insert a new row in the table first_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Insert new row
INSERT INTO @database_name.first_table (id, name)
VALUES (89, 'Best School');

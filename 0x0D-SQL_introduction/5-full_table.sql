-- Script: Print the full description of the table first_table

-- Set the database name
SET @database_name = 'hbtn_0c_0';

-- Print table description
SELECT column_name, column_type
FROM information_schema.columns
WHERE table_schema = @database_name
  AND table_name = 'first_table';


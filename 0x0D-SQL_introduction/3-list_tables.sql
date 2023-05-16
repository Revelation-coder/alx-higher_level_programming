-- Script: List all tables of a database in MySQL server

-- Set the database name
SET @database_name = 'your_database_name';

-- List all tables
SELECT table_name
FROM information_schema.tables
WHERE table_schema = @database_name;


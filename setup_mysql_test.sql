-- Create the test database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;

-- Create the test user if it does not exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the test database to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Ensure the test user has SELECT privilege on the performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Make sure the changes are applied
FLUSH PRIVILEGES;

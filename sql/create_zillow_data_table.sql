-- виконуємо скрипт в Redshift db dev після створення

CREATE TABLE IF NOT EXISTS zillow_data_table(
zipcode INT,
city VARCHAR(255),
homeType VARCHAR(255),
homeStatus VARCHAR(255),
livingArea NUMERIC,
bathrooms NUMERIC,
bedrooms NUMERIC,
price NUMERIC,
zestimate NUMERIC
);

SELECT *
FROM zillow_data_table;


SELECT COUNT(*)
FROM zillow_data_table;
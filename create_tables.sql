CREATE EXTERNAL TABLE pokemon_table (
    id int,
    name varchar(50),
    base_experience int,
    height DECIMAL(10, 2),
    is_default boolean,
    order int,
    weight DECIMAL(10, 2),
    `Type 1` varchar(20),
    `Type 2` varchar(20)
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://nasrsolobucket/cleaned_pokemon/';



CREATE EXTERNAL TABLE berries_table (
    id int,
    name varchar(50),
    growth_time int,
    max_harvest int,
    natural_gift_power int,
    size int,
    smoothness int,
    soil_dryness int
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://nasrsolobucket/cleaned_berries/';

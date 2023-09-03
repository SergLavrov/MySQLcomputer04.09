# 1. Создать БД
# 2. Создать таблицу computer (id primary key, firm not null, year_prod, store_count )
# 3. Запросы:
#    a- получить все данные;
#    б- получить данные в которых есть фирма и год выпуска;
#    в- получить данные, где указан год выпуска;
#    г- получить таблицу с полями фирма и год выпуска, которые есть на складе.


-- create database comps;

use comps;

-- create table computer
-- (
-- id int PRIMARY KEY auto_increment,
-- firm VARCHAR(25) NOT NULL,
-- production_year YEAR,
-- count_computers INT
-- );


INSERT INTO computer (firm, production_year, count_computers)
VALUES
('HP', 2021, 10),
('ASUS', 2022, 15),
('ASER', NULL, 14),
('LENOVO', 2020, NULL),
('SAMSUNG', NULL, NULL),
('SONY', 2019, NULL);

# а- получить все данные;
SELECT * FROM computer;

# б--получить данные в которых есть фирма и год выпуска;
SELECT firm, production_year FROM computer
WHERE production_year IS NOT NULL;

# в-- получить данные, где указан год выпуска;
SELECT production_year FROM computer
WHERE production_year IS NOT NULL;

# г-- получить таблицу с полями фирма и год выпуска, которые есть на складе:
SELECT firm, production_year, count_computers
FROM computer
WHERE count_computers IS NOT NULL;


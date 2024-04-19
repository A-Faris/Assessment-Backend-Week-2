-- Database creation

DROP DATABASE IF EXISTS clown;
CREATE DATABASE clown;
\c clown;

CREATE TABLE IF NOT EXISTS speciality (
    speciality_id INT GENERATED ALWAYS AS IDENTITY,
    speciality_name VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (speciality_id)
);

CREATE TABLE IF NOT EXISTS clown (
    clown_id INT GENERATED ALWAYS AS IDENTITY,
    clown_name VARCHAR(50) NOT NULL,
    speciality_id INT NOT NULL,
    PRIMARY KEY (clown_id),
    FOREIGN KEY (speciality_id) REFERENCES speciality(speciality_id)
);

CREATE TABLE IF NOT EXISTS review (
    review_id INT GENERATED ALWAYS AS IDENTITY,
    clown_id INT NOT NULL,
    rating INT NOT NULL,
    PRIMARY KEY (review_id),
    FOREIGN KEY (clown_id) REFERENCES clown(clown_id)
);

-- Seeding the database

INSERT INTO speciality
    (speciality_name)
VALUES
    ('balloons'),
    ('magic'),
    ('trapeze'),
    ('jokes'),
    ('terror'),
    ('juggling')
;

INSERT INTO clown
    (clown_name, speciality_id)
VALUES
    ('Beppo', 1),
    ('ZigZag', 2),
    ('Monty', 1),
    ('Truffles', 5),
    ('Ferdy', 3),
    ('Monty', 4),
    ('Satchel', 2),
    ('Minnie', 1),
    ('Gustavo', 1),
    ('Konrad', 6),
    ('Ricardo', 3)
;
SELECT speciality_id, speciality_name
FROM speciality;

SELECT clown_id, clown_name, speciality_id
FROM clown;

SELECT review_id, clown_id, rating
FROM review;

SELECT clown_id, clown_name, speciality_name
FROM clown
JOIN speciality USING(speciality_id)
WHERE clown_id = 1;
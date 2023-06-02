-- What query would you run to get all the customers inside city_id = 312?
-- Your query should return customer first name, last name, email, and address.
SELECT c.first_name, c.last_name, c.email, a.address
FROM customer AS c
JOIN address AS a ON c.address_id = a.address_id
JOIN city AS ci ON a.city_id = ci.city_id
WHERE ci.city_id = 312;

-- What query would you run to get all comedy films?
-- Your query should return film title, description,
-- release year, rating, special features, and genre (category).
SELECT f.film_id, f.title, f.description, f.release_year, f.rating, f.special_features, c.name AS genre
FROM film AS f
JOIN film_category AS fc ON f.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy';

-- What query would you run to get all the films joined by actor_id=5?
-- Your query should return the actor id, actor name, film title,
-- description, and release year.
SELECT a.actor_id, CONCAT(a.first_name, ' ', a.last_name) AS actor_name, f.title, f.description, f.release_year
FROM film_actor AS fa
JOIN actor AS a ON fa.actor_id = a.actor_id
JOIN film AS f ON fa.film_id = f.film_id
WHERE a.actor_id = 5;

-- What query would you run to get all the customers in store_id = 1
-- and inside these cities (1, 42, 312, and 459)?
-- Your query should return customer first name, last name, email, and address.
SELECT c.store_id, ci.city_id, c.first_name, c.last_name, c.email, a.address
FROM customer AS c
JOIN address AS a ON c.address_id = a.address_id
JOIN city AS ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (1, 42, 312, 459) AND c.store_id = 1;

-- What query would you run to get all the films with a "rating = G"
-- and "special feature = behind the scenes", joined by actor_id = 15?
-- Your query should return the film title, description, release year,
-- rating, and special feature. Hint:
-- You may use LIKE function in getting the 'behind the scenes' part.
SELECT f.title, f.description, f.release_year, f.rating, f.special_features
FROM film AS f
JOIN film_actor AS fa ON f.film_id = fa.film_id
JOIN actor AS a ON fa.actor_id = a.actor_id
WHERE f.rating = 'G' AND f.special_features LIKE '%behind the scenes%' AND a.actor_id = 15;

-- What query would you run to get all the actors that joined in the film_id = 369?
-- Your query should return the film_id, title, actor_id, and actor_name.
SELECT f.film_id, f.title, a.actor_id, CONCAT(a.first_name, ' ', a.last_name) AS actor_name
FROM film_actor AS fa
JOIN actor AS a ON fa.actor_id = a.actor_id
JOIN film AS f ON fa.film_id = f.film_id
WHERE f.film_id = 369;

-- What query would you run to get all drama films with a rental rate of 2.99?
-- Your query should return film title, description, release year, rating,
-- special features, and genre (category).
SELECT f.film_id, f.title, f.description, f.release_year, f.rating, f.special_features, c.name AS genre
FROM film AS f
JOIN film_category AS fc ON f.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Drama' AND f.rental_rate = 2.99;

-- What query would you run to get all the action films which are joined by SANDRA KILMER?
-- Your query should return film title, description, release year, rating, special features,
-- genre (category), and actor's first name and last name.
SELECT a.actor_id, f.title, f.description, f.release_year, f.rating, f.special_features, c.name AS genre, a.first_name, a.last_name
FROM film AS f
JOIN film_actor AS fa ON f.film_id = fa.film_id
JOIN actor AS a ON fa.actor_id = a.actor_id
JOIN film_category AS fc ON f.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Action' AND CONCAT(a.first_name, ' ', a.last_name) = 'SANDRA KILMER';


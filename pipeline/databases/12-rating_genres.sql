-- list all the shows by rating the genres
SELECT tv_genres.name, SUM(rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.show_id=tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
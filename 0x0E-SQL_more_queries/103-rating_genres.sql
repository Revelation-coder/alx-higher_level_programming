--script  that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(rating) AS rating
FROM tv_genres
JOIN tv_show_ratings ON tv_genres.id = tv_shows_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;

-- List all shows from hbtn_0d_tvshows_rate by their rating
USE hbtn_0d_tvshows_rate;

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows
JOIN tv_show_ratings ON id
WHERE id=show_id
GROUP BY id
ORDER BY rating ASC;

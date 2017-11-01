-- List all shows from hbtn_0d_tvshows_rate by their rating
SELECT title, sum(rate) FROM tv_shows
JOIN tv_show_ratings ON id
WHERE id=show_id
GROUP BY id
ORDER BY sum(rate) ASC;

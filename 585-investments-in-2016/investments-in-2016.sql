# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT 
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv_cnt,
        COUNT(*) OVER (PARTITION BY lat, lon) AS loc_cnt
    FROM Insurance
) AS sub
WHERE tiv_cnt > 1 AND loc_cnt = 1;
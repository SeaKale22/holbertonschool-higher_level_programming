-- 15-groups.sql
-- Lists number of records with same score
SELECT score, COUNT(*) as number FROM second_table GROUP BY score;
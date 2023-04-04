-- 1. Sign up:
-- Insert a new user account into the database
START TRANSACTION;
INSERT INTO Account(username, email, acc_pass)
VALUES ('shayanmk', 'sample@test.con', 'Hello123');

INSERT INTO User(account_id, full_name, pic_url)
VALUES (LAST_INSERT_ID(), 'Shayan Mohammadi', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fuser%2F&psig=AOvVaw22I-TzPPUBkB32_4dK3Y4V&ust=1680027563292000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCOi_psLc_P0CFQAAAAAdAAAAABAE');

SELECT *
FROM Account
WHERE account_id = LAST_INSERT_ID()
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/1.out';

COMMIT;


-- 2. Sign in:
-- Return the account_id for a specific username and password
-- Returns empty if no account is found
SELECT account_id
FROM Account
WHERE username = 'shayanmk'
  AND acc_pass = 'Hello123'
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/2.out';


-- 3a. Get top 10 search results for players whose names contain 'ab'
-- Sorted by how recent they have played
SELECT DISTINCT player_id, player_name, pic_url, game_date
FROM (SELECT *
      FROM Player
      WHERE player_name LIKE '%ab%') AS pab
JOIN PG USING (player_id)
JOIN Game USING (game_id)
ORDER BY game_date DESC
LIMIT 10
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/3a.out';

-- 3b. Show a specific player's details
SELECT *
FROM Player
WHERE player_id = 8469534
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/3b.out';

-- 4a. Top 10 search results for teams whose names contain 'm'
-- ordered by team's age
SELECT team_id, abbrv, team_name, logo_url
FROM Team
WHERE team_name LIKE '%m%'
ORDER BY since
LIMIT 10
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/4a.out';;


-- 4b. Show a specific team's details
SELECT *
FROM Team
WHERE team_id = 197
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/4b.out';;

-- 5a. Get 5 recent games of a player (ordered by date)
SELECT *
FROM (SELECT game_id
      FROM PG
      WHERE player_id = 8469534) AS gop
JOIN Game USING (game_id)
ORDER BY game_date DESC
LIMIT 5
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/5a.out';;

-- 5b. Get 5 recent games of a team (ordered by date)
SELECT *
FROM Game
WHERE team_home_id = 197
   OR team_away_id = 197
ORDER BY game_date DESC
LIMIT 5
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/5b.out';

-- 6a. Add favorite Player to a User
INSERT INTO Fav_Players
VALUES (11796, 8469534);

SELECT *
FROM Fav_Players
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/6a.out';

-- 6b. Add favorite Team to a User
INSERT INTO Fav_Teams
VALUES (11796, 197);

SELECT *
FROM fav_teams
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/6b.out';


-- 7. Show a User's favorite Players
SELECT player_id, player_name, pic_url
FROM (SELECT player_id
      FROM Fav_Players
      WHERE account_id = 11796) AS fp
JOIN Player USING (player_id)
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/production_out/7.out';


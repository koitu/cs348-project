INSERT INTO Admin VALUES
    (100001, 'Admin001', 'cs348@uwaterloo.ca','cs348',3),
    (100002, 'Admin002', 'NHL@uwaterloo.ca','NHL',1);

INSERT INTO User VALUES
    (200001, 'User001', 'user001@uwaterloo.ca','user001','Alice','https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg'),
    (200002, 'User002', 'user002@uwaterloo.ca','user002','Bob','https://upload.wikimedia.org/wikipedia/commons/6/6b/Dog_%28Canis_lupus_familiaris%29_%283%29.jpg');

INSERT INTO Player VALUES
	(8469534, 'Aaron Johnson', '1983-04-30', 204, 188, 'BOS', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8469534.jpg', 40, 'D'),
	(8479447, 'Anthony Greco', '1993-09-30', 176, 180, 'NYR', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8479447.jpg', 30, 'R'),
	(8475757, 'Brett Bulmer', '1992-04-26', 212, 196, 'MIN', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8475757.jpg', 31, 'R'),
	(8473712, 'Frazer McLaren', '1987-10-29', 230, 198, 'TOR', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/skater.jpg', 36, 'L'),
	(8468510, 'Jeff Taffe', '1981-02-19', 207, 193, 'MIN', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/skater.jpg', 42, 'L'),
	(8469598, 'Kevin Bieksa', '1981-06-16', 197, 188, 'ANA', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8469598.jpg', 42, 'D'),
	(8470121, 'Matt Greene', '1983-05-13', 236, 193, 'LAK', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8470121.jpg', 40, 'D'),
	(8476200, 'Paul Thompson', '1988-11-30', 200, 188, 'FLA', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8476200.jpg', 35, 'R'),
	(8468011, 'Ryan Miller', '1980-07-17', 168, 190, 'ANA', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8468011.jpg', 43, 'G'),
	(8478407, 'Vince Dunn', '1996-10-29', 203, 185, 'SEA', 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/8478407.jpg', 27, 'D');


INSERT into Team VALUES
	(101, "ANA", "Anaheim Ducks", "https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Anaheim_Ducks.svg/330px-Anaheim_Ducks.svg.png", "1993"),
	(103, "BOS", "Boston Bruins", "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Boston_Bruins.svg/800px-Boston_Bruins.svg.png", "1924"),
    (113, "FLA", "Florida Panthers", "https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Florida_Panthers_2016_logo.svg/330px-Florida_Panthers_2016_logo.svg.png", "1993"),
    (114, "LAK", "Los Angeles Kings", "https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Los_Angeles_Kings_logo.svg/330px-Los_Angeles_Kings_logo.svg.png", "1967"),
	(115, "MIN", "Minnesota Wild", "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Minnesota_Wild.svg/330px-Minnesota_Wild.svg.png", "2000"),
	(120, "NYR", "New York Rangers", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/New_York_Rangers.svg/330px-New_York_Rangers.svg.png", "1926"),
	(124, "SEA", "Seattle Kraken", "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Seattle_Kraken_official_logo.svg/330px-Seattle_Kraken_official_logo.svg.png", "2021"),
	(128, "TOR", "Toronto Maple Leafs", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Toronto_Maple_Leafs_2016_logo.svg/330px-Toronto_Maple_Leafs_2016_logo.svg.png", "1917");

INSERT into Fav_Teams VALUES
    (200001, 123),
    (200001, 126);

INSERT into Fav_players VALUES
    (200001, 8473712),
    (200002, 8473712),
    (200002, 8479447);

INSERT into Player_team VALUES
--the season attribute is not based on real data!
    (8469534, 103, '2015', 'D'),
	(8479447, 120, '2019', 'R'),
	(8475757, 115, '2004', 'R'),
	(8473712, 128, '2014', 'L'),
	(8468510, 115, '1999', 'L'),
	(8469598, 101, '2015', 'D'),
	(8470121, 114, '2010', 'D'),
	(8476200, 113, '2016', 'R'),
	(8468011, 101, '2007', 'G'),
	(8478407, 124, '2022', 'D');

INSERT into Game VALUES
    (2015020731, 2015, 124, "2016-01-26", 197, 199),
    (2015021066, 2015, 125, "2016-03-18", 199, 197);

INSERT into Play_in VALUES
--the relationship is not based on real data!
    (8469534, 2015020731),
    (8469598, 2015020731),
    (8469534, 2015021066),
    (8469598, 2015021066);



INSERT INTO Account VALUES
	(100001, 'Admin001', 'cs348@uwaterloo.ca', 'cs348'),
    (100002, 'Admin002', 'NHL@uwaterloo.ca', 'NHL'),
    (200001, 'User001', 'user001@uwaterloo.ca', 'user001'),
    (200002, 'User002', 'user002@uwaterloo.ca', 'user002');

-- SPLIT --

INSERT INTO Admin VALUES
    (100001, 3),
    (100002, 1);

-- SPLIT --

INSERT INTO User VALUES
    (200001, 'Alice', 'https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg'),
    (200002, 'Bob', 'https://upload.wikimedia.org/wikipedia/commons/6/6b/Dog_%28Canis_lupus_familiaris%29_%283%29.jpg');

-- SPLIT --

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

-- SPLIT --

INSERT into Team VALUES
	(101, 'ANA', 'Anaheim Ducks', 'https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Anaheim_Ducks.svg/330px-Anaheim_Ducks.svg.png', '1993', NULL),
	(103, 'BOS', 'Boston Bruins', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Boston_Bruins.svg/800px-Boston_Bruins.svg.png', '1924', NULL),
    (113, 'FLA', 'Florida Panthers', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Florida_Panthers_2016_logo.svg/330px-Florida_Panthers_2016_logo.svg.png', '1993', NULL),
    (114, 'LAK', 'Los Angeles Kings', 'https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Los_Angeles_Kings_logo.svg/330px-Los_Angeles_Kings_logo.svg.png', '1967', NULL),
	(115, 'MIN', 'Minnesota Wild', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Minnesota_Wild.svg/330px-Minnesota_Wild.svg.png', '2000', NULL),
	(120, 'NYR', 'New York Rangers', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/New_York_Rangers.svg/330px-New_York_Rangers.svg.png', '1926', NULL),
	(124, 'SEA', 'Seattle Kraken', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Seattle_Kraken_official_logo.svg/330px-Seattle_Kraken_official_logo.svg.png', '2021', NULL),
	(128, 'TOR', 'Toronto Maple Leafs', 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Toronto_Maple_Leafs_2016_logo.svg/330px-Toronto_Maple_Leafs_2016_logo.svg.png', '1917', NULL);

-- SPLIT --

INSERT INTO Fav_Teams VALUES
    (200001, 124),
    (200001, 128);

-- SPLIT --

INSERT INTO Fav_Players VALUES
    (200001, 8473712),
    (200002, 8473712),
    (200002, 8479447);

-- SPLIT --

INSERT INTO PT VALUES
-- the season attribute is not based on real data!
    (8469534, 103, '2015', 'D'),
	(8479447, 120, '2015', 'R'),
	(8475757, 115, '2004', 'R'),
	(8473712, 128, '2015', 'L'),
	(8468510, 115, '1999', 'L'),
	(8469598, 101, '2015', 'D'),
	(8470121, 114, '2010', 'D'),
	(8476200, 113, '2016', 'R'),
	(8468011, 101, '2007', 'G'),
	(8478407, 124, '2022', 'D');

-- SPLIT --

INSERT INTO Game VALUES
    (2015020731, 114, 115, NULL, NULL, 2015, '2016-01-26', NULL),
    (2015021066, 120, 128, NULL, NULL, 2015, '2016-03-18', NULL),
    (2015020738, 101, 114, NULL, NULL, 2015, '2016-01-28', NULL),
    (2015022888, 114, 120, NULL, NULL, 2015, '2016-03-13', NULL),
    (2015022891, 101, 115, NULL, NULL, 2015, '2016-01-22', NULL),
    (2015022883, 113, 115, NULL, NULL, 2015, '2016-03-12', NULL);

-- SPLIT --

INSERT INTO PG VALUES
	(2015021066, 8479447),
    (2015021066, 8473712),
	(2015021066, 8469534),
	(2015020731, 8469534);

-- SPLIT --

INSERT INTO Account VALUES
	(13230, 'yellowpanda307', 'melina.teodosic@example.com', 'X4QsMaeHlYLIUWTXxLym'),
	(81262, 'yellowswan194', 'laetitia.rodriguez@example.com', 'iVFEhBJHCMGP0GI'),
	(28374, 'lazyostrich354', 'elliot.singh@example.com', 'LTTKG03xXrGu'),
	(89796, 'purpleladybug689', 'sasa.ristovic@example.com', 'wJ6IFgwX2Kcd9EYMj'),
	(79143, 'organicladybug225', 'luise.renard@example.com', 'oNxm4Gfo4sAzlZOm'),
	(61165, 'bigswan740', 'lydia.washington@example.com', 'Sx2BK3bvv5JnhY0leB'),
	(94076, 'heavyrabbit548', 'afet.oztonga@example.com', 'e7Jya9J7kYtdXGQQ3'),
	(39297, 'purpleladybug789', 'yehudi.viana@example.com', 'bazt35lIMtW2Dkr6R'),
	(32793, 'sadswan729', 'valtteri.kantola@example.com', 'VBM3ZbKYWkh31czbDDAZQG8'),
	(35817, 'yellowrabbit953', 'harrison.zhang@example.com', 'BUiiTuFUQvJtFpkLa'),
	(25761, 'purpleduck838', 'etienne.white@example.com', '44UgbKlgzj0H'),
	(28747, 'brownrabbit517', 'livia.david@example.com', '5K440tAOuqadJdUA2fO'),
	(36768, 'greenbird153', 'necati.tuzun@example.com', 'DO5l6YWInAL848MCFpj'),
	(95656, 'organicladybug430', 'brent.porter@example.com', '2iA6w0sc8IyeGQNRIgJenF'),
	(39700, 'happydog681', 'marco.ronnestad@example.com', 'q0argGMGHmSyptC6U'),
	(11796, 'orangedog640', 'iegor.kozakevich@example.com', 'ac3cG9k8uxayvxVFsQ'),
	(84589, 'smallgorilla451', 'nathan.robinson@example.com', 'h7pkJRdZznwlu'),
	(99356, 'lazykoala790', 'emilie.chu@example.com', 'nUzREoeN9Eyr2B'),
	(63736, 'beautifulbear387', 'helienay.dacunha@example.com', 'wyg5SgfonvRDlBpX'),
	(13531, 'purplemouse522', 'viridiana.castro@example.com', 'eqBfdhHURRzWB3'),
	(90795, 'bluegorilla896', 'mary.edwards@example.com', 'wtvooi7RH7UeRm'),
	(83058, 'purplefish418', 'brittany.grant@example.com', 'UCl2OTqu7Gz29X8Rtj9'),
	(79821, 'orangegorilla323', 'jorge.ramos@example.com', 'KxtolVomfGsTdDh3eFQH'),
	(18706, 'bluepanda703', 'axel.arnaud@example.com', 'yFwFs823jGsaj9mP');

-- SPLIT --

INSERT INTO User VALUES
	(13230, 'Melina Teodosić', 'https://randomuser.me/api/portraits/thumb/women/33.jpg'),
	(81262, 'Laetitia Rodriguez', 'https://randomuser.me/api/portraits/thumb/women/44.jpg'),
	(28374, 'Elliot Singh', 'https://randomuser.me/api/portraits/thumb/men/14.jpg'),
	(89796, 'Saša Ristović', 'https://randomuser.me/api/portraits/thumb/men/63.jpg'),
	(79143, 'Luise Renard', 'https://randomuser.me/api/portraits/thumb/women/5.jpg'),
	(61165, 'Lydia Washington', 'https://randomuser.me/api/portraits/thumb/women/27.jpg'),
	(94076, 'Afet Öztonga', 'https://randomuser.me/api/portraits/thumb/women/58.jpg'),
	(39297, 'Yehudi Viana', 'https://randomuser.me/api/portraits/thumb/women/47.jpg'),
	(32793, 'Valtteri Kantola', 'https://randomuser.me/api/portraits/thumb/men/30.jpg'),
	(35817, 'Harrison Zhang', 'https://randomuser.me/api/portraits/thumb/men/20.jpg'),
	(25761, 'Etienne White', 'https://randomuser.me/api/portraits/thumb/men/24.jpg'),
	(28747, 'Livia David', 'https://randomuser.me/api/portraits/thumb/women/87.jpg'),
	(36768, 'Necati Tüzün', 'https://randomuser.me/api/portraits/thumb/men/11.jpg'),
	(95656, 'Brent Porter', 'https://randomuser.me/api/portraits/thumb/men/39.jpg'),
	(39700, 'Marco Rønnestad', 'https://randomuser.me/api/portraits/thumb/men/90.jpg'),
	(11796, 'Iegor Kozakevich', 'https://randomuser.me/api/portraits/thumb/men/14.jpg'),
	(84589, 'Nathan Robinson', 'https://randomuser.me/api/portraits/thumb/men/55.jpg'),
	(99356, 'Emilie Chu', 'https://randomuser.me/api/portraits/thumb/women/91.jpg'),
	(63736, 'Helienay da Cunha', 'https://randomuser.me/api/portraits/thumb/women/66.jpg'),
	(13531, 'Viridiana Castro', 'https://randomuser.me/api/portraits/thumb/women/44.jpg'),
	(90795, 'Mary Edwards', 'https://randomuser.me/api/portraits/thumb/women/16.jpg'),
	(83058, 'Brittany Grant', 'https://randomuser.me/api/portraits/thumb/women/21.jpg'),
	(79821, 'Jorge Ramos', 'https://randomuser.me/api/portraits/thumb/men/14.jpg'),
	(18706, 'Axel Arnaud', 'https://randomuser.me/api/portraits/thumb/men/7.jpg');

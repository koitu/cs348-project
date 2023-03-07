
INSERT INTO Player VALUES
	(8478421, 'A.J. Greer', '1996-12-14', 210, 190, 'CAN', NULL, 24, 'L'),
    (8478424, 'Jansen Harkins', '1997-05-23', 182, 186, 'USA', NULL, 58, 'C'),
    (8478425, 'Brendan Guhle', '1997-07-29', 196, 183, 'CAN', NULL, 45, 'D'),
    (8478427, 'Sebastian Aho', '1997-07-26', 176, 1, 'FIN', NULL, 20, 'C'),
    (8478430, 'Oliver Kylington', '1997-05-19', 183, 180, 'SWE', NULL, 58, 'D');


INSERT into Team VALUES
    (123, "TML", "Toronto Maple Leafs", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Toronto_Maple_Leafs_2016_logo.svg/640px-Toronto_Maple_Leafs_2016_logo.svg.png", "1999"),
    (124, "BBR", "BOSTON BRUINS", "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Boston_Bruins.svg/800px-Boston_Bruins.svg.png", "1999"),
    (125, "EDO", "Edmonton Oilers", "https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Logo_Edmonton_Oilers.svg/1200px-Logo_Edmonton_Oilers.svg.png", "1999"),
    (126, "MCA", "Montreal Canadiens", "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Boston_Bruins.svg/800px-Boston_Bruins.svg.png", "1999");
    
INSERT into game VALUES
    (1234, 123, 124, "HOME", "2022" ,null),
    (1235, 123, 125, "AWAY", "2022" ,null),
    (1236, 124, 125, "AWAY", "2022" ,null),
    (1237, 126, 125, "AWAY", "2022" ,null),
    (1238, 125, 123, "HOME", "2022" ,null),
    (1239, 124, 126, "AWAY", "2022" ,null);

INSERT into pg VALUES 
    (1234, 8478421, 3),
    (1234, 8478425, 4),
    (1234, 8478427, 4),
    (1235, 8478421, 8);




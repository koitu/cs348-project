CREATE TABLE PT (
	player_id	INT,
    team_id		INT,
    season		NUMERIC(4,0),
    pos			CHAR(1) CHECK(pos IN ('G', 'D', 'L', 'C', 'R')),
    
    PRIMARY KEY (player_id, team_id),
    FOREIGN KEY (player_id)
		REFERENCES Player(player_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
	FOREIGN KEY (team_id)
		REFERENCES Team(team_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE GT (
	game_id		INT,
    team_id		INT,
    -- TODO: add attributes
    
    PRIMARY KEY (game_id, team_id),
    FOREIGN KEY (game_id)
		REFERENCES Game(game_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
	FOREIGN KEY (team_id)
		REFERENCES Team(team_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE PT (
	game_id		INT,
    player_id	INT,
    -- TODO: add attributes
    
    PRIMARY KEY (game_id, player_id),
    FOREIGN KEY (game_id)
		REFERENCES Game(game_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
	FOREIGN KEY (player_id)
		REFERENCES Player(player_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE Fav_Players (
	account_id 	INT,
    player_id	INT,
    
    PRIMARY KEY (account_id, player_id),
    FOREIGN KEY (account_id)
		REFERENCES User(account_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
	FOREIGN KEY (player_id)
		REFERENCES Player(player_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE Fav_Teams (
	account_id 	INT,
    team_id		INT,
    
    PRIMARY KEY (account_id, team_id),
    FOREIGN KEY (account_id)
		REFERENCES User(account_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
	FOREIGN KEY (team_id)
		REFERENCES Team(team_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);
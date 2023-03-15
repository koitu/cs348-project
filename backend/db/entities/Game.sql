CREATE TABLE Game (
	game_id		INT PRIMARY KEY AUTO_INCREMENT,
	team1_id	INT NOT NULL,
	team2_id	INT NOT NULL,
    home_away	CHAR(4) CHECK(home_away IN ('HOME','AWAY')),
    season		NUMERIC(4,0),
    game_date	DATE,
	FOREIGN KEY (team1_id)
		REFERENCES Team(team_id)
		ON UPDATE RESTRICT
        ON DELETE CASCADE,
	FOREIGN KEY (team2_id)
		REFERENCES Team(team_id)
		ON UPDATE RESTRICT
        ON DELETE CASCADE
);

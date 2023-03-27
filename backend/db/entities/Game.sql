CREATE TABLE Game (
	game_id			INT PRIMARY KEY AUTO_INCREMENT,
	team_home_id	INT NOT NULL,
	team_away_id	INT NOT NULL,
	team_home_score	INT,
	team_away_score	INT,
    season			NUMERIC(4,0),
    game_date		DATE,
    location		VARCHAR(255),
	FOREIGN KEY (team_home_id)
		REFERENCES Team(team_id)
		ON UPDATE RESTRICT
        ON DELETE CASCADE,
	FOREIGN KEY (team_away_id)
		REFERENCES Team(team_id)
		ON UPDATE RESTRICT
        ON DELETE CASCADE
);

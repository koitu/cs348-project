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

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

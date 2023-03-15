CREATE TABLE PG (
	game_id		INT,
    player_id	INT,
    -- TODO: add attributes
    points      INT,
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

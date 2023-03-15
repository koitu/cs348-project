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

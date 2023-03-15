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

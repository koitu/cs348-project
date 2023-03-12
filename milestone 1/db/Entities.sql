CREATE TABLE Account (
	account_id	INT PRIMARY KEY AUTO_INCREMENT,
	username 	VARCHAR(255) NOT NULL UNIQUE,
	email 		VARCHAR(255) NOT NULL UNIQUE CHECK(email LIKE '%@%.%'),
	acc_pass 	VARCHAR(255) NOT NULL -- TODO: Use PASSWORD() hash function
);

CREATE TABLE User (
	account_id	INT PRIMARY KEY,
	full_name 	VARCHAR(255) NOT NULL,
	pic_url 	VARCHAR(255),
	FOREIGN KEY (account_id) 
		REFERENCES Account(account_id)
		ON UPDATE CASCADE 
        ON DELETE CASCADE
);

CREATE TABLE Admin (
	account_id	INT PRIMARY KEY,
    -- TODO: add more admin attributes...
	FOREIGN KEY (account_id) 
		REFERENCES Account(account_id)
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

-- Team/Player Account ?!

CREATE TABLE Player (
	player_id 	INT PRIMARY KEY AUTO_INCREMENT,
	player_name	VARCHAR(255) NOT NULL,
	birth_date 	DATE,
    weight 		INT,
    height 		INT,
	nationality CHAR(3),
	pic_url		VARCHAR(255),
    primary_num INT,
    primary_pos	CHAR(1) CHECK(primary_pos IN ('G', 'D', 'L', 'C', 'R'))
);

CREATE TABLE Team (
	team_id		INT PRIMARY KEY AUTO_INCREMENT,
    abbrv		CHAR(3) NOT NULL UNIQUE,
	team_name	VARCHAR(255) NOT NULL UNIQUE,
    logo_url	VARCHAR(255),
    since 		NUMERIC(4,0)
);

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

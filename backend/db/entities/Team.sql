CREATE TABLE Team (
	team_id		INT PRIMARY KEY AUTO_INCREMENT,
    abbrv		CHAR(3),
	team_name	VARCHAR(255),
    logo_url	VARCHAR(255),
    since 		NUMERIC(4,0)
    -- location    VARCHAR(255)
);

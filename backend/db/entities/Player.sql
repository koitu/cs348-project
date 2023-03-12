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

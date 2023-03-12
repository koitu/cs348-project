CREATE TABLE User (
	account_id	INT PRIMARY KEY,
	full_name 	VARCHAR(255) NOT NULL,
	pic_url 	VARCHAR(255),
	FOREIGN KEY (account_id)
		REFERENCES Account(account_id)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);

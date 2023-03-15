CREATE TABLE Admin (
	account_id	INT PRIMARY KEY,
    -- TODO: add more admin attributes...
	FOREIGN KEY (account_id)
		REFERENCES Account(account_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

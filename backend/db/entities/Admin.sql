CREATE TABLE Admin (
	account_id	INT PRIMARY KEY,
    privilege INT CHECK(privilage BETWEEN 1 AND 3),
    -- TODO: add more admin attributes...
	FOREIGN KEY (account_id)
		REFERENCES Account(account_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

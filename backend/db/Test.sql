CREATE TABLE if not exists PAIN (
    pain_id INT PRIMARY KEY,
    aaaa INT
);

CREATE TABLE if not exists Account (
	account_id	INT PRIMARY KEY,
	username 	VARCHAR(255) NOT NULL UNIQUE,
	acc_pass 	VARCHAR(255) NOT NULL
);
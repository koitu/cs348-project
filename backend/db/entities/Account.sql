CREATE TABLE Account (
	account_id	INT PRIMARY KEY AUTO_INCREMENT,
	username 	VARCHAR(255) NOT NULL UNIQUE,
	email 		VARCHAR(255) NOT NULL UNIQUE CHECK(email LIKE '%@%.%'),
	acc_pass 	VARCHAR(255) NOT NULL -- TODO: Use PASSWORD() hash function
);

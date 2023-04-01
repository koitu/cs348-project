CREATE INDEX game_date_idx USING BTREE ON Game(game_date);

CREATE INDEX player_name USING HASH ON Player(player_name);

CREATE INDEX team_name USING HASH ON Team(team_name);



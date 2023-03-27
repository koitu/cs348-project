from errors import BadRequest, MatchExistsError, MatchNotFoundError
from utils import mysql_connection

from mysql.connector import errorcode, IntegrityError


class Match:
    match_id = None
    team_home_id = None
    team_away_id = None
    team_home_score = None
    team_away_score = None
    season = None
    date = None
    location = None

    def set(self, values: tuple = ()) -> None:
        assert(len(values) == 8)
        self.match_id, \
            self.team_home_id, \
            self.team_away_id, \
            self.team_home_score, \
            self.team_away_score, \
            self.season, \
            self.date, \
            self.location = values

    def __init__(
        self,
        match_id: int = None,
        team_home_id: int = None,
        team_away_id: int = None,
        team_home_score: int = None,
        team_away_score: int = None,
        season: int = None,
        date: str = None,
        location: str = None,
    ):
        self.set((
            match_id,
            team_home_id,
            team_away_id,
            team_home_score,
            team_away_score,
            season,
            date,
            location,
            ))

    def to_tuple(self) -> tuple:
        return (
            self.match_id,
            self.team_home_id,
            self.team_away_id,
            self.team_home_score,
            self.team_away_score,
            self.season,
            self.date,
            self.location,
        )

    def to_dict(self) -> dict:
        return {
            'match_id': self.match_id,
            'team_home_id': self.team_home_id,
            'team_away_id': self.team_away_id,
            'team_home_score': self.team_home_score,
            'team_away_score': self.team_away_score,
            'season': self.season,
            'date': self.date,
            'location': self.location,
        }

    def valid(self) -> bool:
        return all(
            x is not None for x in [
                self.match_id,
                self.team_home_id,
                self.team_away_id,
            ])

    def get(self) -> None:
        if self.match_id is None:
            raise BadRequest("Please specify the match to retrieve")
        if type(self.match_id) is not int:
            raise BadRequest("match_id is required to be an integer")

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "SELECT * "
                "FROM Game "
                "WHERE game_id = %s"
            )
            cursor.execute(query, (self.match_id,))
            result = cursor.fetchall()
            if len(result) == 0:
                raise MatchNotFoundError(self.match_id)

            self.set(result[0])

    def create(self) -> None:
        if self.team_home_id is None:
            raise BadRequest("Home team ID is a required field")
        if self.team_away_id is None:
            raise BadRequest("Away team ID is a required field")

        match_id = self.match_id
        with mysql_connection() as con, con.cursor() as cursor:
            con.start_transaction()

            try:
                query = (
                    "INSERT INTO Game "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                )
                cursor.execute(query, self.to_tuple())
                if match_id is None:
                    match_id = cursor.lastrowid

            except IntegrityError as err:
                con.rollback()

                if err.errno == errorcode.ER_DUP_ENTRY:
                    # if the error is a primary key violation
                    raise MatchExistsError(self.match_id)
                else:
                    # else rethrow error
                    raise err

            except Exception as err:
                con.rollback()
                raise err

            else:
                con.commit()
                self.match_id = match_id

    def update(self) -> None:
        # save updated values to tuple
        new = self.to_tuple()

        # get old values into tuple (get() also checks that match exists)
        self.get()
        merge = self.to_tuple()

        # overwrite old values with new values
        for i, x in enumerate(new):
            if x is not None:
                merge[i] = x
        self.set(merge)

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "UPDATE Game SET "
                "team_home_id = %s "
                "team_away_id = %s "
                "team_home_score = %s "
                "team_away_score = %s "
                "season = %s "
                "game_date = %s "
                "location = %s "
                "WHERE game_id = %s"
            )
            cursor.execute(query, self.to_tuple()[1:] + (self.match_id,))

    def delete(self) -> None:
        # check that match exists before deleting
        self.get()

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "DELETE FROM Game "
                "WHERE game_id = %s"
            )
            cursor.execute(query, (self.match_id,))


def search_matches(
        teams: list[str] = [],
        players: list[str] = [],
        # TODO: pagementation
        # page_num: int,
        # res_per_page: int,
) -> list[Match]:
    tn = len(teams)
    pn = len(players)
    query = (
        "SELECT game_id "
        "FROM Game"
    )
    filter = []
    args = []

    if tn > 0:
        if tn == 1:
            filter.append(
                "(team_home_id = %s OR team_away_id = %s)"
            )
            args += teams + teams

        elif tn == 2:
            filter.append(
                "(team_home_id = %s AND team_away_id = %s)"
            )
            args += teams

        else:
            raise BadRequest("There cannot be more than 2 teams in a game")

    if pn > 0:
        filter.append(
            "(" + ",".join(["%s" for _ in range(pn)]) + ") "
            "IN (SELECT team_id FROM PG WHERE PG.game_id = Game.game_id)"
        )
        args += players

    if len(filter) > 0:
        query += " WHERE "
        query += " AND ".join(filter)
    query += " LIMIT 10 "

    with mysql_connection() as con, con.cursor() as cursor:
        print("query:", query)
        print("args:", args)
        cursor.execute(query, args)
        result = cursor.fetchall()

        matches = [Match(match_id=r[0]) for r in result]
        for m in matches:
            m.get()
        return matches

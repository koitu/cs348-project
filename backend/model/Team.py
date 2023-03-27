from errors import BadRequest, TeamExistsError, TeamNotFoundError
from utils import mysql_connection

from mysql.connector import errorcode, IntegrityError


class Team:
    team_id = None
    abbrv = None
    team_name = None
    logo_url = None
    since = None
    # location = None

    def set(self, values: tuple = ()):
        assert(len(values) == 5)
        # assert(len(values) == 6)
        self.team_id, \
            self.abbrv, \
            self.team_name, \
            self.logo_url, \
            self.since = values
        # self.location

    def __init__(
        self,
        team_id: int = None,
        abbrv: str = None,
        team_name: str = None,
        logo_url: str = None,
        since: int = None,
        # location: str = None,
    ):

        self.set((
            team_id,
            abbrv,
            team_name,
            logo_url,
            since,
            # location,
            ))

        if logo_url is None:
            self.logo_url = "/static/default_team_logo.png"

    def to_tuple(self) -> tuple:
        return (
            self.team_id,
            self.abbrv,
            self.team_name,
            self.logo_url,
            self.since,
            # self.location,
            )

    def to_dict(self) -> dict:
        return {
            'team_id': self.team_id,
            'abbrv': self.abbrv,
            'team_name': self.team_name,
            'logo_url': self.logo_url,
            'since': self.since,
            # 'location': self.location,
        }

    def valid(self) -> bool:
        return all(
            x is not None for x in [
                self.team_id,
                self.abbrv,
                self.team_name,
            ])

    def check_team_id(self) -> None:
        if self.team_id is None:
            raise BadRequest("Please specify the team to retrieve")
        if type(self.team_id) is not int:
            raise BadRequest("team_id is required to be an integer")

    def get(self) -> None:
        self.check_team_id()

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "SELECT * "
                "FROM Team "
                "where team_id = %s"
            )
            cursor.execute(query, (self.team_id,))
            result = cursor.fetchall()
            if len(result) == 0:
                raise TeamNotFoundError(self.team_id)

            self.set(result[0])

    def create(self) -> None:
        team_id = self.team_id

        with mysql_connection() as con, con.cursor() as cursor:
            con.start_transaction()

            try:
                query = (
                    "INSERT INTO Team "
                    "VALUES(%s, %s, %s, %s, %s, %s)"
                )
                cursor.execute(query, self.to_tuple())
                if team_id is None:
                    team_id = cursor.lastrowid

            except IntegrityError as err:
                con.rollback()

                if err.errno == errorcode.ER_DUP_ENTRY:
                    # if the error is a primary key violation
                    raise TeamExistsError(self.team_id)
                else:
                    # else rethrow error
                    raise err

            except Exception as err:
                con.rollback()
                raise err

            else:
                con.commit()
                self.team_id = team_id

    def update(self) -> None:
        # save updated values to tuple
        new = self.to_tuple()

        # get old values into tuple (get() also checks that team exists)
        self.get()
        merge = self.to_tuple()

        # overwrite old values with new values
        for i, x in enumerate(new):
            if x is not None:
                merge[i] = x
        self.set(merge)

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "UPDATE Team SET "
                "team_id = %s "
                "abbrv = %s "
                "team_name = %s "
                "logo_url = %s "
                "since  = %s "
                # "location = %s "
                "WHERE team_id = %s"
            )
            cursor.execute(query, self.to_tuple()[1:] + (self.team_id,))

    def delete(self) -> None:
        # check that team exists before deleting
        self.get()

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "DELETE FROM Team "
                "WHERE team_id = %s"
            )
            cursor.execute(query, (self.team_id,))


def search_teams(
        team_name: str,
        players: list[str] = [],
        ) -> list[Team]:
    pn = len(players)

    query = (
        "SELECT team_id "
        "FROM Team "
        "WHERE team_name LIKE %s"
    )
    filter = []
    args = []

    if team_name is not None:
        filter.append(
            "team_name LIKE %s"
        )
        args.append(team_name + "%")

    if pn > 0:
        filter.append(
            "(" + ",".join(["%s" for _ in range(pn)]) + ") "
            "IN (SELECT player_id FROM PT WHERE PT.team_id = Team.team_id)"
        )
        args.extend(players)

    if len(filter) > 0:
        query += " WHERE "
        query += " AND ".join(filter)
    query += " LIMIT 10 "

    with mysql_connection() as con, con.cursor() as cursor:
        print("query:", query)
        print("args:", args)
        cursor.execute(query, args)
        result = cursor.fetchall()

        teams = [Team(team_id=r[0]) for r in result]
        for t in teams:
            t.get()
        return teams

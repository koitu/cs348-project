from errors import BadRequest, MatchAlreadyExistsError, MatchNotFoundError
from utils import mysql_connection


class Match:
    def __init__(
        self,
        match_id: int = None,
        team1_id: int = None,
        team2_id: int = None,
        team1_score: int = None,
        team2_score: int = None,
        date: str = None,
        location: str = None,
    ):
        self.match_id = match_id
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.date = date
        self.location = location

    def to_dict(self) -> dict:
        return {
            'match_id': self.match_id,
            'team1_id': self.team1_id,
            'team2_id': self.team2_id,
            'team1_score': self.team1_score,
            'team2_score': self.team2_score,
            'date': self.date,
            'location': self.location
        }

    def valid(self) -> bool:
        return all(
            x is not None for x in [
                self.match_id,
                self.team1_id,
                self.team2_id,
            ])

    def check_match_id(self) -> None:
        if self.match_id is None:
            raise BadRequest("Please specify the match to retrieve")
        if type(self.match_id) is not int:
            raise BadRequest("match_id is required to be an integer")

    def get(self) -> None:
        self.check_match_id()

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

            # TODO
            # self.match_id,
            # self.team1_id,
            # self.team2_id,

            # result[0]

    def create(self) -> None:
        if self.team1_id is None:
            raise BadRequest("Team 1 ID is a required field")
        if self.team2_id is None:
            raise BadRequest("Team 2 ID is a required field")
        if self.date is None:
            raise BadRequest("Date is a required field")

        # TODO
        # perform SQL query that may raise MatchAlreadyExistsError
        # after SQL match creation get the match_id and set self.match_id
        pass

    def update(self) -> None:
        self.check_match_id()

        # TODO
        # perform SQL query to update match
        # if the match does not exist then raise MatchNotFoundError
        # permission checking will be handled by caller
        pass

    def delete(self) -> None:
        self.check_match_id()

        # TODO
        # perform SQL query to delete match
        # if the match does not exist then raise MatchNotFoundError
        # permission checking will be handled by caller
        pass


def search_matches(
        teams: list[str] = [],
        players: list[str] = [],
):
    tn = len(teams)
    pn = len(players)
    query = (
        "SELECT game_id, team1_id, team2_id, season, game_date "
        "FROM Game"
    )

    filter = []
    if tn > 0:
        filter.append(
            "(" + ",".join(["%s" for _ in range(tn)]) + ") "
            "IN (SELECT team_id from GT where GT.game_id = Game.game_id)"
        )
    if pn > 0:
        filter.append(
            "(" + ",".join(["%s" for _ in range(pn)]) + ") "
            "IN (SELECT team_id from PG where PG.game_id = Game.game_id)"
        )

    # TODO: may be faster if using INTERSECT instead of many conditions
    if len(filter) > 0:
        query += " WHERE "
        query += " AND ".join(filter)
        query += ";"

    result = None
    with mysql_connection() as con, con.cursor() as cursor:
        print(query)
        cursor.execute(query, teams + players)
        result = cursor.fetchall()

    return [Match(
                match_id=i[0],
                team1_id=i[1],
                team2_id=i[2],
                season=i[3],
                date=i[4],
            ) for i in result]



def search_matches_for_player(
        player_id: str
        ) -> list[Match]:
    with mysql_connection() as con, con.cursor() as cursor:
        find_games = f"""select game_id, team1_id, team2_id, home_away, seasone, game_date
                         from Game join PG using(game_id)
                         where player_id = {player_id} ;"""
        cursor.execute(find_games)
        result = cursor.fetchall()
        retVal = []
        for i in result:
            print(i)
            retVal.append(Match(match_id=i[0], team1_id=i[1], team2_id=i[2], date=i[5]))
        return retVal  


def search_matches_for_team(
        team_id: int,
        fuzzy=True
        ) -> list[Match]:
    with mysql_connection() as con, con.cursor() as cursor:
        find_games = f"""select game_id, team1_id, team2_id, home_away, seasone, game_date
                         from Game join GT using(game_id)
                         where game_id = {team_id} 
                         order by game_date desc; """
        cursor.execute(find_games)
        result = cursor.fetchall()
        retVal = []
        for i in result:
            print(i)
            retVal.append(Match(match_id=i[0], team1_id=i[1], team2_id=i[2], date=i[5]))
        return retVal  

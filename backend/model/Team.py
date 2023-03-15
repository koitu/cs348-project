from errors import BadRequest, TeamAlreadyExistsError, TeamNotFoundError
from utils import mysql_connection


class Team:
    def __init__(
        self,
        team_id: int = None,
        abbrv: str = None,
        team_name: str = None,
        logo: str = None,
        since: int = None,

        players: list[str] = None,
        location: str = None,
    ):
        self.team_id = team_id
        self.abbrv = abbrv
        self.team_name = team_name
        self.logo = logo
        self.since = since

        self.players = players
        self.location = location

        if logo is None:
            self.logo = "/static/default_team_logo.png"
        if players is None:
            self.players = []

    def to_dict(self) -> dict:
        return {
            'team_id': self.team_id,
            'abbrv': self.abbrv,
            'team_name': self.team_name,
            'logo': self.logo,
            'since': self.since,

            'players': self.players,
            'location': self.location,
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

            self.team_id,       \
                self.abbrv,     \
                self.team_name, \
                self.logo,      \
                self.since = result[0]

    def create(self) -> None:
        if self.team_name is None:
            raise BadRequest("Team name is a required field")
        if self.start_date is None:
            raise BadRequest("Start date is a required field")

        # TODO
        # perform SQL query that may raise TeamAlreadyExistsError
        # after SQL team creation get the team_id and set self.team_id
        pass

    def update(self) -> None:
        self.check_team_id()

        # TODO
        # perform SQL query to update team
        # if the team does not exist then raise TeamNotFoundError
        # permission checking will be handled by caller
        pass

    def delete(self) -> None:
        self.check_team_id()

        # TODO
        # perform SQL query to delete team
        # if the team does not exist then raise TeamNotFoundError
        # permission checking will be handled by caller
        pass

def search_teams_played(player_id: str, fuzzy=True) -> list[Team]:
    with mysql_connection() as con, con.cursor() as cursor:
        find_teams = f"""select team_id, abbrv, team_name, logo_url 
                         from Team join PT using(team_id)
                         where player_id like '%{player_id}%'
                         order by sesone desc """
        cursor.execute(find_teams)
        result = cursor.fetchall()
        retVal = []
        for i in result:
            print(i)
            retVal.append(Team( team_id= i[0],
                                team_name= i[2],
                                abbrv= i[1],
                                logo= i[3]))
        return retVal 

def search_teams(team_name: str, fuzzy=True) -> list[Team]:
    
    with mysql_connection() as con, con.cursor() as cursor:
        find_teams = f"""select team_id, abbrv, team_name, logo_url 
                         from Team 
                         where team_name like '%{team_name}%'
                         order by team_name asc
                         limit 10"""
        cursor.execute(find_teams)
        result = cursor.fetchall()
        retVal = []
        for i in result:
            print(i)
            retVal.append(Team( team_id= i[0],
                                team_name= i[2],
                                abbrv= i[1],
                                logo= i[3]))
        return retVal 

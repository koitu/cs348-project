from errors import BadRequest, TeamAlreadyExistsError, TeamNotFoundError


class Team:
    def __init__(
        self,
        team_id: int = None,
        team_name: str = None,
        start_date: str = None,
        logo: str = None,
        players: list[str] = None,
        league: str = None,
        location: str = None,
    ):
        self.team_id = team_id
        self.team_name = team_name
        self.start_date = start_date
        self.logo = logo
        self.players = players
        self.league = league
        self.location = location

        if logo is None:
            self.logo = "/static/default_team_logo.png"
        if players is None:
            self.players = []

    def to_dict(self) -> dict:
        return {
            'team_id': self.team_id,
            'team_name': self.team_name,
            'start_date': self.start_date,
            'logo': self.logo,
            'players': self.players,
            'league': self.league,
            'location': self.location,
        }

    def valid(self) -> bool:
        # check that the User is a valid User
        # TODO
        pass

    def check_team_id(self) -> None:
        if self.team_id is None:
            raise BadRequest("Please specify the team to retrieve")
        if type(self.team_id) is not int:
            raise BadRequest("team_id is required to be an integer")

    def get(self) -> None:
        self.check_team_id()

        # TODO
        # perform SQL query to fill in the rest of the details
        # if the team does not exist then raise TeamNotFoundError
        pass

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


def search_teams(team_name: str, fuzzy=True) -> list[Team]:
    # TODO
    pass

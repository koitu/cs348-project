# Team class should mimic a team tuple in the database relational model
class Team:
    def __init__(
        self,
        name: str,
        logo: str,
        players: list[str] | None,
        league: str,
        location: str,
    ):
        self.name = name
        self.logo = logo
        self.players = players
        self.league = league
        self.location = location

        if players is None:
            self.players = []

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'logo': self.logo,
            'players': self.players,
            'league': self.league,
            'location': self.location,
        }

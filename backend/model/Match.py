# Match class should mimic a match tuple in the database relational model
class Match:
    def __init__(
        self,
        team1: str,
        team2: str,
        team1_score: int,
        team2_score: int,
        date: str,
        location: str,
        # TODO
    ):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.date = date
        self.location = location

    def to_dict(self) -> dict:
        return {
            'team1': self.team1,
            'team2': self.team2,
            'team1_score': self.team1_score,
            'team2_score': self.team2_score,
            'date': self.date,
            'location': self.location
        }

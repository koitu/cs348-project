from errors import BadRequest, MatchAlreadyExistsError, MatchNotFoundError


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
        # check that the Match is a valid Match
        # TODO
        pass

    def check_match_id(self) -> None:
        if self.match_id is None:
            raise BadRequest("Please specify the match to retrieve")
        if self.match_id is not int:
            raise BadRequest("match_id is required to be an integer")

    def get(self) -> None:
        self.check_match_id()

        # TODO
        # perform SQL query to fill in the rest of the details
        # if the match does not exist then raise MatchNotFoundError
        pass

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
        team_id: int,
        other_team_id: int,
        # desc date order
        fuzzy=True
        ) -> list[Match]:
    # TODO
    pass

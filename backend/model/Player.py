from errors import BadRequest, PlayerAlreadyExistsError, PlayerNotFoundError


class Player:
    def __init__(
        self,
        player_id: int = None,
        player_name: str = None,
        birthday: str = None,
        picture: str = None,
        nationality: str = None,
        position: str = None,
    ):
        self.player_id = player_id
        self.player_name = player_name
        self.birthday = birthday
        self.picture = picture
        self.nationality = nationality
        self.position = position

    def to_dict(self) -> dict:
        return {
            'player_id': self.player_id,
            'player_name': self.player_name,
            'birthday': self.birthday,
            'picture': self.picture,
            'nationality': self.nationality,
            'position': self.position,
        }

    def check_player_id(self) -> None:
        if self.player_id is None:
            raise BadRequest("Please specify the player to retrieve")
        if self.player_id is not int:
            raise BadRequest("player_id is required to be an integer")

    def get(self) -> None:
        self.check_player_id()

        # perform SQL query to fill in the rest of the details
        # if the player does not exist then raise PlayerNotFoundError
        pass

    def create(self) -> None:
        if self.player_name is None:
            raise BadRequest("Player name is a required field")

        # perform SQL query that may raise PlayerAlreadyExistsError
        # after SQL player creation get the player_id and set self.player_id
        pass

    def update(self) -> None:
        self.check_player_id()

        # perform SQL query to update player
        # if the player does not exist then raise PlayerNotFoundError
        # permission checking will be handled by caller
        pass

    def delete(self) -> None:
        self.check_player_id()

        # perform SQL query to delete player
        # if the player does not exist then raise PlayerNotFoundError
        # permission checking will be handled by caller
        pass


def search_players(
        player_name: str,
        nationality: str,
        fuzzy=True
        ) -> list[Player]:
    pass

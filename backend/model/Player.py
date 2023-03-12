from errors import BadRequest, PlayerAlreadyExistsError, PlayerNotFoundError
from utils import mysql_connection


class Player:
    def __init__(
        self,
        player_id: int = None,
        player_name: str = None,
        birthday: str = None,
        weight: int = None,
        height: int = None,
        nationality: str = None,
        picture: str = None,
        number: int = None,
        position: str = None,
    ):
        self.player_id = player_id
        self.player_name = player_name
        self.birthday = birthday
        self.weight = weight
        self.height = height
        self.nationality = nationality
        self.picture = picture
        self.number = number
        self.position = position

        if picture is None:
            self.profile_pic = "/static/default_player_pic.png"

    def to_dict(self) -> dict:
        return {
            'player_id': self.player_id,
            'player_name': self.player_name,
            'birthday': self.birthday,
            'weight': self.weight,
            'height': self.height,
            'nationality': self.nationality,
            'picture': self.picture,
            'number': self.number,
            'position': self.position,
        }

    def valid(self) -> bool:
        return all(
            x is not None for x in [
                self.player_id,
                self.player_name,
            ])

    def check_player_id(self) -> None:
        if self.player_id is None:
            raise BadRequest("Please specify the player to retrieve")
        if not self.player_id.isdigit():
            raise BadRequest("player_id is required to be an integer")

    def get(self) -> None:
        self.check_player_id()

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "SELECT * "
                "FROM Player "
                "WHERE player_id = %s"
            )
            cursor.execute(query, (self.player_id,))
            result = cursor.fetchall()
            if len(result) == 0:
                raise PlayerNotFoundError(self.player_id)

            self.player_id,       \
                self.player_name, \
                self.birthday,    \
                self.weight,      \
                self.height,      \
                self.nationality, \
                self.picture,     \
                self.number,      \
                self.position = result[0]

    def create(self) -> None:
        if self.player_name is None:
            raise BadRequest("Player name is a required field")

        # TODO
        # perform SQL query that may raise PlayerAlreadyExistsError
        # after SQL player creation get the player_id and set self.player_id
        pass

    def update(self) -> None:
        self.check_player_id()

        # TODO
        # perform SQL query to update player
        # if the player does not exist then raise PlayerNotFoundError
        # permission checking will be handled by caller
        pass

    def delete(self) -> None:
        self.check_player_id()

        # TODO
        # perform SQL query to delete player
        # if the player does not exist then raise PlayerNotFoundError
        # permission checking will be handled by caller
        pass


def search_players(
        player_name: str,
        fuzzy=True
        ) -> list[Player]:

    with mysql_connection() as con, con.cursor() as cursor:
        # TODO: proper escaping for player_name
        find_player = f"""select *
                         from Player
                         where player_name like '%{player_name}%'
                         order by player_name asc
                         limit 10"""
        cursor.execute(find_player)
        result = cursor.fetchall()
        retVal = []
        for i in result:
            print(i)
            retVal.append(Player(i[0], i[1], i[2], i[3], i[5], i[8]))
        return retVal
from errors import BadRequest, PlayerAlreadyExistsError, PlayerNotFoundError
from utils import mysql_connection


class Player:
    def __init__(
        self,
        player_id: int = None,
        player_name: str = None,
        birthday: str = None,
        picture: str = None,
        nationality: str = None,
        position: str = None,
        # player picture
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

    def valid(self) -> bool:
        # check that the Player is a valid Player
        # TODO
        pass

    def check_player_id(self) -> None:
        if self.player_id is None:
            raise BadRequest("Please specify the player to retrieve")
        # if type(self.player_id) is not int:
        if not self.player_id.isdigit():
            raise BadRequest("player_id is required to be an integer")

    def get(self) -> None:
        with mysql_connection() as con, con.cursor() as cursor:
            find_player = "select * from Player where player_id=%s"
            cursor.execute(find_player, (self.player_id,))
            result = cursor.fetchall()[0]

            self.player_id,       \
                self.player_name, \
                self.birthday,    \
                self.weight,      \
                self.height,      \
                self.nationality, \
                self.pic_url,     \
                self.primary_num, \
                self.primary_pos = result

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
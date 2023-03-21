from errors import BadRequest, PlayerExistsError, PlayerNotFoundError
from utils import mysql_connection

from mysql.connector import errorcode, IntegrityError


class Player:
    player_id = None
    player_name = None
    birthday = None
    weight = None
    height = None
    nationality = None
    picture = None
    number = None
    position = None

    def set(self, values: tuple = ()):
        assert(len(values) == 9)
        self.player_id, \
            self.player_name, \
            self.birthday, \
            self.weight, \
            self.height, \
            self.nationality, \
            self.picture, \
            self.number, \
            self.position = values

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
        self.set((
            player_id,
            player_name,
            birthday,
            weight,
            height,
            nationality,
            picture,
            number,
            position,
            ))

        if picture is None:
            self.profile_pic = "/static/default_player_pic.png"

    def to_tuple(self) -> tuple:
        return (
            self.player_id,
            self.player_name,
            self.birthday,
            self.weight,
            self.height,
            self.nationality,
            self.picture,
            self.number,
            self.position,
        )

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

    def get(self) -> None:
        if self.player_id is None:
            raise BadRequest("Please specify the player to retrieve")
        if not self.player_id.isdigit():
            raise BadRequest("player_id is required to be an integer")

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

            self.set(result[0])

    def create(self) -> None:
        if self.player_name is None:
            raise BadRequest("Player name is a required field")

        player_id = self.player_id
        with mysql_connection() as con, con.cursor() as cursor:
            con.start_transaction()

            try:
                query = (
                    "INSERT INTO Player "
                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )
                cursor.execute(query, self.to_tuple())
                if player_id is None:
                    player_id = cursor.lastrowid

            except IntegrityError as err:
                con.rollback()

                if err.errno == errorcode.ER_DUP_ENTRY:
                    # if the error is a primary key violation
                    raise PlayerExistsError(self.player_id)
                else:
                    # else rethrow error
                    raise err
            else:
                con.commit()
                self.player_id = player_id

    def update(self) -> None:
        # save updated values to tuple
        new = self.to_tuple()

        # get old values into tuple (get() also checks that player exists)
        self.get()
        merge = self.to_tuple()

        # overwrite old values with new values
        for i, x in enumerate(new):
            if x is not None:
                merge[i] = x
        self.set(merge)

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "UPDATE Player SET "
                "player_name = %s "
                "birth_date = %s "
                "weight = %s "
                "height = %s "
                "nationality = %s "
                "pic_url = %s "
                "primary_num = %s "
                "primary_pos = %s "
                "WHERE player_id = %s"
            )
            cursor.execute(query, self.to_tuple()[1:] + (self.player_id,))

    def delete(self) -> None:
        # check that player exists before deleting
        self.get()

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "DELETE FROM Player "
                "WHERE player_id = %s"
            )
            cursor.execute(query, (self.player_id,))


# TODO finding list of players that belong to team x will be handled by search_players
def search_players(
        player_name: str,
        fuzzy=True
        ) -> list[Player]:

    with mysql_connection() as con, con.cursor() as cursor:
        # query = (
        #     "SELECT player_id "
        #     "FROM PT "
        #     "WHERE team_id = %s"
        # )
        # cursor.execute(query, (self.team_id,))
        # result = cursor.fetchall()
        # self.players = [x[0] for x in result]

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
            retVal.append(Player(*i))
        return retVal

from errors import BadRequest, UserAlreadyExistsError, UserNotFoundError
from utils import mysql_connection


class User:
    def __init__(
        self,
        account_id: int = None,
        username: str = None,
        email: str = None,
        password: str = None,
        fullname: str = None,
        profile_pic: str = None,
        is_admin: bool = None,
    ):
        self.account_id = account_id
        self.username = username
        self.email = email
        self.password = password
        self.fullname = fullname
        self.profile_pic = profile_pic
        self._is_admin = is_admin

        if profile_pic is None:
            self.profile_pic = "/static/default_profile_pic.png"

    def to_dict(self) -> dict:
        return {
            'account_id': self.account_id,
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'profile_pic': self.profile_pic,
            'is_admin': self._is_admin,
        }

    def valid(self) -> bool:
        return all(
            x is not None for x in [
                self.account_id,
                self.username,
                self.email,
                self.password,
                self.fullname,
            ])

    def check_account_id(self) -> None:
        if self.account_id is None:
            raise BadRequest("Please specify the account to retrieve")
        if not self.account_id.isdigit():
            raise BadRequest("account_id is required to be an integer")

    def is_admin(self, force_check=False) -> bool:
        self.check_account_id()

        # TODO: this caches the is_admin parameter which is probably a bad idea
        if force_check or self._is_admin is None:
            with mysql_connection() as con, con.cursor() as cursor:
                query = (
                    "SELECT * "
                    "FROM Admin "
                    "WHERE account_id = %s"
                )
                cursor.execute(query, (self.account_id,))
                result = cursor.fetchall()

                self._is_admin = len(result) != 0
        return self._is_admin

    def get(self) -> None:
        self.is_admin()  # set the is_admin_parameter and test account_id

        with mysql_connection() as con, con.cursor() as cursor:
            query = (
                "SELECT account_id, username, email, fullname, pic_url "
                "FROM Account NATURAL JOIN User "
                "where account_id = %s"
            )
            cursor.execute(query, (self.account_id,))
            result = cursor.fetchall()
            if len(result) == 0:
                raise UserNotFoundError(self.account_id)

            self.account_id,      \
                self.username,    \
                self.email,       \
                self.fullname,    \
                self.profile_pic = result[0]

    def create(self) -> None:
        if self.username is None:
            raise BadRequest("Username is a required field")
        if self.email is None:
            raise BadRequest("Email is a required field")
        if self.password is None:
            raise BadRequest("Password is a required field")
        if self.fullname is None:
            raise BadRequest("Full name is a required field")

        # TODO
        # perform SQL query that may raise a UserAlreadyExistsError
        # after SQL user creation get the account_id and set self.account_id
        pass

    def update(self) -> None:
        self.check_account_id()

        # TODO
        # perform SQL query to update user
        # if the user does not exist then raise UserNotFoundError
        # permission checking will be handled by caller
        pass

    def delete(self) -> None:
        self.check_account_id()

        # TODO
        # perform SQL query to delete user
        # if the user does not exist then raise UserNotFoundError
        # permission checking will be handled by caller
        pass


def search_users(username: str, fuzzy=True) -> list[User]:
    # perform a SQL fuzzy search for a certain username
    # TODO
    pass

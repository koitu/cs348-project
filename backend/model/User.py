from errors import (
    BadRequest,
    UserNotFoundError,
    UserExistsError,
    EmailExistsError,
    UsernameExistsError,
)
from utils import mysql_connection

from mysql.connector import errorcode, IntegrityError


class User:
    account_id = None
    username = None
    email = None
    fullname = None
    profile_pic = None

    def set(self, values: tuple = ()):
        assert(len(values) == 5)
        self.account_id, \
            self.username, \
            self.email, \
            self.fullname, \
            self.profile_pic = values

    def __init__(
        self,
        account_id: int = None,
        username: str = None,
        email: str = None,
        fullname: str = None,
        profile_pic: str = None,

        password: str = None,
        is_admin: bool = None,
    ):
        self.set((
            account_id,
            username,
            email,
            fullname,
            profile_pic
            ))

        if profile_pic is None:
            self.profile_pic = "/static/default_profile_pic.png"

        self.password = password
        self._is_admin = is_admin

    def to_tuple(self) -> tuple:
        return (
            self.account_id,
            self.username,
            self.email,
            self.fullname,
            self.profile_pic,
            self._is_admin,
        )

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

    def is_admin(self, force_check=True) -> bool:
        self.check_account_id()

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
        self.is_admin()  # test self.account_id and set self._is_admin

        with mysql_connection() as con, con.cursor() as cursor:
            # requires left join since an admin may not have entry in the User
            query = (
                "SELECT account_id, username, email, fullname, pic_url "
                "FROM Account LEFT JOIN User using(account_id) "
                "where account_id = %s"
            )
            cursor.execute(query, (self.account_id,))
            result = cursor.fetchall()
            if len(result) == 0:
                raise UserNotFoundError(self.account_id)

            self.set(result[0])

    def create(self) -> None:
        if self.username is None:
            raise BadRequest("Username is a required field")
        if self.email is None:
            raise BadRequest("Email is a required field")
        if self.password is None:
            raise BadRequest("Password is a required field")
        if self.fullname is None and not self._is_admin:
            raise BadRequest("Full name is a required field")

        account_id = self.account_id
        with mysql_connection() as con, con.cursor() as cursor:
            con.start_transaction()
            try:
                query = (
                    "INSERT INTO Account "
                    "VALUES (%s, %s, %s, %s)"
                )
                cursor.execute(query, (
                    account_id,
                    self.username,
                    self.email,
                    self.password,
                ))
                if account_id is None:
                    account_id = cursor.lastrowid

                if self._is_admin:
                    query = (
                        "INSERT INTO Admin "
                        "(account_id) "
                        "VALUES (%s)"
                    )
                    cursor.execute(query, (
                        account_id,
                    ))

                if self.fullname is not None:
                    query = (
                        "INSERT INTO User "
                        "(account_id, full_name, pic_url) "
                        "VALUES (%s, %s, %s)"
                    )
                    cursor.execute(query, (
                        account_id,
                        self.fullname,
                        self.profile_pic,
                    ))
            except IntegrityError as err:
                con.rollback()

                if err.errno == errorcode.ER_DUP_ENTRY:
                    # if the error is a primary key violation
                    raise UserExistsError(self.account_id)

                elif err.errno == errorcode.ER_DUP_UNIQUE:
                    # if the error is a unique key violation
                    cursor.execute(
                        "SELECT * FROM Account WHERE username = %s",
                        (self.username,)
                    )
                    result = cursor.fetchall()
                    # two possible unique key violations: username or email
                    if len(result) != 0:
                        raise UsernameExistsError(self.username)
                    else:
                        raise EmailExistsError(self.email)
                else:
                    # else rethrow error
                    raise err
            else:
                con.commit()
                self.account_id = account_id

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

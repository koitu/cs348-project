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
        assert(len(values) == 6)
        self.account_id, \
            self.username, \
            self.email, \
            self.password, \
            self.fullname, \
            self.profile_pic = values

    def __init__(
        self,
        account_id: str = None,
        username: str = None,
        email: str = None,
        fullname: str = None,
        profile_pic: str = None,

        password: str = None,
        is_admin: bool = None,
    ):
        self.set((
            str(account_id),
            username,
            email,
            password,
            fullname,
            profile_pic
            ))

        if profile_pic is None:
            self.profile_pic = "/static/default_profile_pic.png"

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
                "SELECT account_id, username, email, "
                "acc_pass, full_name, pic_url "
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

        with mysql_connection() as con, con.cursor() as cursor:
            con.start_transaction()
            try:
                query = (
                    "INSERT INTO Account "
                    "VALUES (NULL, %s, %s, %s)"
                )
                cursor.execute(query, (
                    self.username,
                    self.email,
                    self.password,
                ))
                account_id = cursor.lastrowid

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

                if self._is_admin:
                    query = (
                        "INSERT INTO Admin "
                        "(account_id) "
                        "VALUES (%s)"
                    )
                    cursor.execute(query, (
                        account_id,
                    ))

            except IntegrityError as err:
                con.rollback()

                # TODO
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

            except Exception as err:
                con.rollback()
                raise err

            else:
                con.commit()
                self.account_id = account_id

    def update(self) -> None:
        # save updated values to tuple
        new = self.to_tuple()

        # get old values into tuple
        self.get()
        merge = self.to_tuple()

        # overwrite old values with new values
        for i, x in enumerate(new):
            if x is not None:
                merge[i] = x
        self.set(merge)

        with mysql_connection() as con, con.cursor() as cursor:
            con.start_transaction()
            try:
                query = (
                    "UPDATE Account SET "
                    "username = %s, "
                    "email = %s, "
                    "acc_pass = %s "
                    "WHERE account_id = %s"
                )
                cursor.execute(query, (
                    self.username,
                    self.email,
                    self.password,
                    self.account_id,
                ))

                if self.fullname is not None:
                    query = (
                        "UPDATE User SET "
                        "full_name = %s "
                        "pic_url = %s "
                        "WHERE account_id = %s"
                    )
                    cursor.execute(query, (
                        self.fullname,
                        self.profile_pic,
                        self.account_id,
                    ))

            except Exception as err:
                con.rollback()
                raise err

            else:
                con.commit()

    def delete(self) -> None:
        # check that player exists before attempting to delete
        self.get()

        with mysql_connection() as con, con.cursor() as cursor:
            con.start_transaction()
            try:
                query = (
                    "DELETE FROM Account "
                    "WHERE account_id = %s"
                )
                cursor.execute(query, (self.account_id,))

                if self.fullname is not None:
                    query = (
                        "DELETE FROM User "
                        "WHERE account_id = %s"
                    )
                    cursor.execute(query, (self.account_id,))

                if self._is_admin:
                    query = (
                        "DELETE FROM Admin "
                        "WHERE account_id = %s "
                    )
                    cursor.execute(query, (self.account_id,))

            except Exception as err:
                con.rollback()
                raise err

            else:
                con.commit()


def search_users(
        username: str = None,
        fullname: str = None,
        ) -> list[User]:
    query = (
        "SELECT account_id "
        "FROM Account "
    )
    filter = []
    args = []

    if username is not None:
        filter.append(
            "username LIKE %s"
        )
        args.append(username + "%")

    if fullname is not None:
        filter.append(
            "full_name LIKE %s"
        )
        args.append(fullname + "%")

    if len(filter) > 0:
        query += " WHERE "
        query += " AND ".join(filter)
    query += " LIMIT 10 "

    with mysql_connection() as con, con.cursor() as cursor:
        print("query:", query)
        print("args:", args)
        cursor.execute(query, args)
        result = cursor.fetchall()

        users = [User(account_id=r[0]) for r in result]
        for u in users:
            u.get()
        return users


# no security, just checks if (username,password) pair exists in db
def login(
        username: str = None,
        password: str = None,
        ):
    if username is None or password is None:
        return None

    with mysql_connection() as con, con.cursor() as cursor:
        query = (
            "SELECT account_id "
            "FROM Account "
            "WHERE username = %s AND acc_pass = %s"
        )
        cursor.execute(query, (username, password))
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        return result[0][0]

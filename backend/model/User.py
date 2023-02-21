# User class should mimic a user tuple in the database relational model
class User:
    def __init__(
        self,
        userid: int,
        name: str,
        avatar: str,
        username: str,
        password: str,
    ):
        self.userid = userid
        self.name = name
        self.avatar = avatar
        self.username = username
        self.password = password

    def to_dict(self) -> dict:
        return {
            'userid': self.userid,
            'name': self.name,
            'avatar': self.avatar,
            'username': self.username,
        }

    # makes request to database to get the rest of the user details
    def get(self):
        # if the user does not exist then throw some exception (need to catch in user.py)
        pass

    #  creates the user in the database
    def create(self):
        pass

    #  creates the user in the database
    def update(self):
        pass

    #  delete the user from the database
    def delete(self):
        pass

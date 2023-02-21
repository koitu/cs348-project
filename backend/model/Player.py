# Player class should mimic a player tuple in the database relational model
class Player:
    def __init__(
        self,
        name: str,
        picture: str,
        bday: str,
        height: int,
        weight: int,
        position: str,
        schools: list[str] | None,
    ):
        self.name = name
        self.bday = bday
        self.picture = picture
        self.height = height
        self.weight = weight
        self.position = position
        self.schools = schools

        if schools is None:
            self.schools = []

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'bday': self.bday,
            'picture': self.picture,
            'height': self.height,
            'weight': self.weight,
            'position': self.position,
            'schools': self.schools
        }

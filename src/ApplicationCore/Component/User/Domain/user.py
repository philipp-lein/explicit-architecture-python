class User(object):
    def __init__(self, username: str):
        self.username = username

    def to_dict(self) -> dict:
        return {"username": self.username}
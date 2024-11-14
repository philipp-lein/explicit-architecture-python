class User(object):
    def __init__(self, username: str):
        self.username = username

    @staticmethod
    def create_user(username: str) -> "User":
        user = User(username)
        return user

    def to_dict(self) -> dict:
        return {"username": self.username}
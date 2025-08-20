from user import User


class Privileges:
    def __init__(self):
        self.privileges = ["can delete post", "can add post", "can be user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege}")


class Admin(User):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.privileges = Privileges()

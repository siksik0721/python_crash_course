class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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

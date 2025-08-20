class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


user = User("철수", "김", 20)
user.describe_user()
user.greet_user()

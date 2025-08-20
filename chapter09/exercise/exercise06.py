class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} opens.")


class IceCreamStand(Restaurant):
    def __init__(self, name, *flavors):
        super().__init__(name, "Ice Cream")
        self.flavors = flavors

    def show_flavors(self):
        print(f"{self.restaurant_name} has the following flavors.")
        for flavor in self.flavors:
            print(f"\t{flavor}")


ice_cream_stand = IceCreamStand("Ice Cream Stand", "Vanila", "Choco", "Strawberry")
ice_cream_stand.show_flavors()

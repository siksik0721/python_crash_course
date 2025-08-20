class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} opens.")


burger_king = Restaurant("Burger King", "Hamburger")
burger_king.describe_restaurant()

pizza_hut = Restaurant("Pizza Hut", "Pizza")
pizza_hut.describe_restaurant()

outback = Restaurant("Outback Steakhouse", "Steak")
outback.describe_restaurant()

from car_all import Car, ElectricCar

my_mustang = Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

import car_all

my_mustang = car_all.Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
my_leaf = car_all.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

from car import Car
from electric_car import ElectricCar

my_mustang = Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

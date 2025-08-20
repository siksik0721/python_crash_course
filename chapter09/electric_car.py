"""전기차를 표현하는 클래스 집합"""

from car import Car


class Battery:
    """전기차의 배터리를 표현하는 클래스"""

    def __init__(self, battery_size=40):
        """배터리 속성을 초기화합니다"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """이 배터리로 주행할 수 있는 거리를 알려줍니다"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """전기차에만 해당하는 클래스"""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화합니다
        그리고 전기차에만 해당하는 속성을 초기화합니다
        """
        super().__init__(make, model, year)
        self.battery = Battery()

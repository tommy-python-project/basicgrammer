"""
应对多重继承
优先使用对象组合，而不是类继承 - 组合优于继承是重要的面向对象设计原则。
"""

# 不推荐的继承方式
# class Engine:
#     def start(self):
#         print("Engine started")
#
# class Car(Engine): # 错误： Car 不是 Engine 的一种
#     def drive(self):
#         self.start()
#         print("Car driving")


# 推荐的组合方式
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # 组合：Car 有一个 Engine

    def drive(self):
        self.engine.start()
        print("Car driving")


# 更复杂的组合示例
class Battery:
    def __init__(self,capacity):
        self.capacity = capacity

    def charge(self):
        print(f"Charging {self.capacity} kWh battery")

class GPS:
    def navigate(self,destination):
        print(f"Navigating to {destination}")

class EntertainmentSystem:
    def play_music(self):
        print("Playing music")


class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery = Battery(battery_capacity)
        self.gps = GPS()
        self.entertainment = EntertainmentSystem()

    def drive(self):
        self.battery.charge()
        print("Electric car driving")

    def navigate_to(self, destination):
        self.gps.navigate(destination)

    def play_entertainment(self):
        self.entertainment.play_music()

# 使用组合
tesla = ElectricCar(75)
tesla.drive()
tesla.navigate_to("Beijing")
tesla.play_entertainment()
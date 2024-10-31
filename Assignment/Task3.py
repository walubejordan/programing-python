class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type 
        
    def start(self):
        print("Start vehicle")
        
    def show_info(self):
        print(f"vehicle_type: {self.vehicle_type}")
        
class Car(Vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors
        
    def show_info(self):
        super().show_info()
        print(f"number_of_door: {self.number_of_doors}")
    
class ElectricCar(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity = battery_capacity
    
    def show_info(self):
        super().show_info()
        print(f"battery_capacity: {self.battery_capacity}kWh")
        
#example
car1 = ElectricCar("Tesla", 4, 80)
car1.start()
car1.show_info()

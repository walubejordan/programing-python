class Applience:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
        
    def show_info(self):
        print(f"brand: {self.brand}, power: {self.power}")
        
class WashingMachine(Applience):
    def __init__(self, brand, power, drum_size):
        super().__init__(brand, power)
        self.drum_size = drum_size
        
    def show_info(self):
        super().show_info()
        print(f"drum_size: {self.drum_size}kg")
        
#example
applience1 = WashingMachine("Hisense", 10, 8)
applience1.show_info()
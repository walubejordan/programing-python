class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def show_info(self):
        print(f"brand: {self.brand}, model: {self.model}")
        
               
#child class
class Smartphone(Device):
    def __init__(self, brand, model, storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity
        
    def show_info(self):
        super().show_info()
        print(f"storage_capacity: {self.storage_capacity}GB")
        
#Examples
phone1 = Smartphone("Samsung", "Galaxy note10 plus", 256)
phone1.show_info()
phone2 = Smartphone("Iphone", "14pro max", 128)
phone2.show_info()

        
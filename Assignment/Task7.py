class Device:
    def info(self):
        print("Device information.")
        
class Computer(Device):
    def info(self):
        print("Computer information.")
        
class Laptop(Computer):
    def info(self):
        print("Laptop information.")
        super().info()
        
#Example
device = Laptop()
device.info()
        

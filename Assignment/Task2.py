class Camera:
    def take_photo(self):
        print("Taking a photo")
        
class Phone:
    def make_a_call(self):
        print("Making a call")
        
class Smartphone(Camera,Phone):
    pass

#example
phone1 = Smartphone()
phone1.take_photo()
phone1.make_a_call()
        
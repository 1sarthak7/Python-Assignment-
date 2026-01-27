class vehicle:
    def carsound(self):
        return "Vroom Vroom"
class bike(vehicle):
    def bikesound(self):
        return "ting ting"
class truck(vehicle):
    def trucksound(self):
        return "Honk Honk"
    
v = vehicle()
b = bike()
t = truck() 

print("car sound : ", v.carsound())
print("bike sound : ",b.bikesound())
print("Truck Sound : ",t.trucksound())

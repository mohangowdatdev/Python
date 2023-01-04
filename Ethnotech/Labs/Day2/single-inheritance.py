class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle Class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car Class")


car = Car()
car.vehicle_info()
car.car_info()

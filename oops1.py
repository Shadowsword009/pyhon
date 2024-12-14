class Car:
    def __init__(self,brand,fuel_type):
        self.brand=brand
        self.fuel_type=fuel_type

    def car_details(self,mileage:float):
        print(f"this is {self.brand} car and is {self.fuel_type} and mileage is {mileage}")

car1 = Car( brand="benz",fuel_type="diesel")
car2 = Car( brand="porshe",fuel_type="petrol")

car1.car_details(16)
car2.car_details(8)


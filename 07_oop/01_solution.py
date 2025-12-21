class Car:
    Total_Cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.Total_Cars += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are a popular mode of transportation."
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_evcar = ElectricCar("Mahindra", "BE6", "79KWh")

# print(isinstance(my_evcar, ElectricCar))
# print(isinstance(my_evcar, Car))

# print(my_evcar.get_brand())
# print(my_evcar.full_name())
# print(my_evcar.fuel_type())

Seltos = Car("Kia", "Seltos")
# print(Seltos.get_brand())
# print(Seltos.full_name())
# print(Seltos.fuel_type())

Safari = Car("Tata", "Safari")
# print(Safari.get_brand())
# print(Safari.full_name())
# print(Safari.fuel_type())

# print("Total Cars:", Car.Total_Cars)

my_car = Car("Toyota", "Camry")
# my_car.model = "Fortuner"
# print(my_car.model)

# print(my_car.general_description())
# print(Car.general_description())

class Battery:
    def battery_info(self):
        return "This car has a battery."

class Engine:
    def engine_info(self):
        return "This car has an engine."

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_electric_car = ElectricCarTwo("Hyundai", "Ioniq 5")
print(my_electric_car.engine_info())
print(my_electric_car.battery_info())
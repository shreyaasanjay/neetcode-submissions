class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
       pass

class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        Vehicle = Car()
        return Vehicle
    

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        Vehicle = Bike()
        return Vehicle

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        Vehicle = Truck()
        return Vehicle

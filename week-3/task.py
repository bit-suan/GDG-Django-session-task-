class Vehicles:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def describe(self):
        return f"This is a {self.make} {self.model}"

class Car(Vehicles):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):
        return f"This is a {self.get_make()} {self.get_model()} car with {self.num_doors} doors."

class Bike(Vehicles):
    def __init__(self, make, model, has_pedals):
        super().__init__(make, model)
        self.has_pedals = has_pedals

    def describe(self):
        return f"This is a {self.get_make()} {self.get_model()} bike that {'has' if self.has_pedals else 'does not have'} pedals."

def vehicle_description(vehicle: Vehicles):
    print(vehicle.describe())

# Example 
car = Car("Toyota", "Corolla", 4)
bike = Bike("Giant", "Escape 3", True)

vehicle_description(car)  
vehicle_description(bike)

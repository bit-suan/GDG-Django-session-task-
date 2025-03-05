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
    def __init__(self, make, model, num_doors,engine, year):
        super().__init__(make, model)
        self.num_doors = num_doors
        self.engine = engine
        self.year = year

    def describe(self):
        return f"This is a {self.year} {self.get_make()} {self.get_model()} with {self.num_doors} doors and a {self.engine} engine."


class Bike(Vehicles):
    def __init__(self, make, model, has_pedals, frame_material, gear_type):
        super().__init__(make, model)
        self.has_pedals = has_pedals
        self.frame_material = frame_material
        self.gear_type = gear_type

    def describe(self):
        return f"This is a modern {self.get_make()} {self.get_model()} bike with a {self.frame_material} frame, {self.gear_type} gears, and {'pedals' if self.has_pedals else 'no pedals'}."

def vehicle_description(vehicle: Vehicles):
    print(vehicle.describe())

# Example 
car = Car("Mercedes-Benz", "G-Wagon", 4, "V8 Turbo", 2025)
bike = Bike("Trek", "Domane SL 7", True, "Carbon Fiber", "Electronic")

vehicle_description(car)  
vehicle_description(bike)

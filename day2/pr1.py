class Vehicle:
    def __init__(self,vehicle_id , brand , model , rental_price_per_day , is_rented= False):
        self.vehicle_id= vehicle_id 
        self.brand= brand
        self.model= model 
        self.is_rented= is_rented
        self.rental_price_per_day=rental_price_per_day 

    def rent(self):
        if self.is_rented:
            print("this car is already rented")
        else:
            self.is_rented = True
    def return_vehicle(self) :
        self.is_rented =False

    def calculate_rental_cost(self,days) :
        return self.rental_price_per_day * days
    
    def get_details(self):
        status = "rented" if self.is_rented else "available"
        return f"vehicle brand: {self.brand}, vehicle model: {self.model}  ID: {self.vehicle_id} , ${self.rental_price_per_day}/day , status: {status}"

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, num_doors):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.num_doors = num_doors
        self.mult = 1.0 

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.mult
    
    def get_details(self):
        status = "rented" if self.is_rented else "available"
        return f"car: {self.brand}, {self.model}  ID: {self.vehicle_id} , ${self.rental_price_per_day}/day , {self.num_doors} doors"
    
    
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, engine_cc):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.engine_cc = engine_cc
        self.mult= 0.7

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.mult
    
    def get_details(self):
        status = "rented" if self.is_rented else "available"
        return f"car: {self.brand}, {self.model}  ID: {self.vehicle_id} , ${self.rental_price_per_day}/day , {self.engine_cc}"
    
    
class Truck (Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day,cargo_capacity_tons):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.cargo_capacity_tons= cargo_capacity_tons
        self.mult= 1.5

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.mult
    
    def get_details(self):
        status = "rented" if self.is_rented else "available"
        return f"car: {self.brand}, {self.model}  ID: {self.vehicle_id} , ${self.rental_price_per_day}/day , {self.cargo_capacity_tons}"
    

car = Car("V001", "Toyota", "Camry", 50, 4)
motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, 750)
truck = Truck("V003", "Ford", "F-150", 80, 2.5)

car.rent()
print(car.is_rented)

cost = car.calculate_rental_cost(5)
print(f"Rental cost for 5 days: ${cost}")

print(motorcycle.get_details())
"""create a class "Car" with two instance members i.e. "model(string)" and "isauto(boolean)"
have getter methods also.
create 5 to 6 objects by passing model name and True or False for "isauto".
create a list and store all the objects inside it.
now create one more list and in that list store all the objects from first list where "isauto" is True.
Print both the lists."""

class Car:
    def __init__(self, model, isauto):
        self.model = model
        self.isauto = isauto

    def get_model(self):
        return self.model

    def get_isauto(self):
        return self.isauto

    def __str__(self):
        return f"Model: {self.model}, Automatic: {self.isauto}"


car1 = Car("Honda", True)
car2 = Car("Alto", False)
car3 = Car("Hyundai", True)
car4 = Car("Tata", False)
car5 = Car("Toyota", True)
car6 = Car("Kwid", False)

all_cars = [car1, car2, car3, car4, car5, car6]

auto_cars = [car for car in all_cars if car.get_isauto()]

print("All Cars:")
for car in all_cars:
    print(car)

print("\nAutomatic Cars:")
for car in auto_cars:
    print(car)

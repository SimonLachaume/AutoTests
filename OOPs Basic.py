class Car():

    def __init__(self, model, year, engine_volume, price, run):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.run = run
        self.wheels = 4

    def description_car(self):

        description = "Модель автомобиля: " + self.model + ", " + str(self.year) + " года выпуска, объем двигателя: " + str(self.engine_volume) + "л. Стоимость: " + str(self.price) + ", пробег: " + str(self.run) + ", кол-во колес: " + str(self.wheels)
        print(description)

    def update_wheel(self, amount):
        self.wheels = amount


passenger_car = Car("Audi А6", 1998, 4, 3000000, 16000)
passenger_car.description_car()

class Truck(Car):
    def __init__(self, model, year, engine_volume, price, run):
        super().__init__(model, year, engine_volume, price, run)

truck = Truck("KAMAZ", 1980, 14, 2000000, 200000)
truck.update_wheel(8)
truck.description_car()


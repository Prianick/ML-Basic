import homework_05

plane = homework_05.plane.Plane(100)
plane.load_cargo(100)

car = homework_05.car.Car(100, 10, 10)
car.set_engine(homework_05.engine.Engine(2.0, 4))
car.move(500)

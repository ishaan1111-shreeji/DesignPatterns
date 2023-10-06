# the below program demonstrates, multiple System of Car meachnism
# like Ignition,Engine,Fuel_check,HandLights,foglights,to work together.
# All above system are managed and controlled by facade i.e Car below.


class _IgnitionSystem(object):
    @staticmethod
    def produce_spark():
        return True


class _Engine(object):
    def __init__(self):
        self.revs_per_min = 0

    def turnon(self):
        self.revs_per_min = 2000

    def turnoff(self):
        self.revs_per_min = 0


# class _FuelTank(object):
#     def __init__(self, level=50):
#         self.level = level
#
#     # The @property is a built-in decorator for the property() function in Python.
#     # It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.
#     @property
#     def level(self):
#         return self.level
#
#     @level.setter
#     def level(self, level):
#         self._level = level


class _DashBoardLight(object):
    def __init__(self, is_on=False):
        self._is_on = is_on

    def __str__(self):
        return self.__class__.__name__

    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, status):
        self._is_on = status

    def status_check(self):
        if self._is_on:
            print("{}:ON".format(str(self)))
        else:
            print("{}:OFF".format(str(self)))


class _HandBrakeLight(_DashBoardLight):
    pass


class _FogLampLight(_DashBoardLight):
    pass


class _Dashboard(object):
    def __init__(self):
        self.lights = {"handbreak": _HandBrakeLight(), "fog": _FogLampLight()}

    def show(self):
        for light in self.lights.values():
            light.status_check()


# we create Facade to maintain above complex classes
class Car(object):
    def __init__(self):
        self.ignition_system = _IgnitionSystem()
        self.engine = _Engine()
        # self.fuel_tank = _FuelTank()
        self.dashboard = _Dashboard()

    @property
    def km_per_litre(self):
        return 17.0

    # def consume_fuel(self, km):
    #     litres = min(self.fuel_tank.level, km / self.km_per_litre)
    #     self.fuel_tank.level -= litres

    def start(self):
        print("\nStarting.....")
        self.dashboard.show()
        if self.ignition_system.produce_spark():
            self.engine.turnon()
        else:
            print("Cant Start.Fault ignition sys")

    # def has_enough_fuel(self, km, km_per_litre):
    #     litres_needed = km / km_per_litre
    #     if self.fuel_tank.level > litres_needed:
    #         return True
    #     else:
    #         return False


    def drive(self, km=100):
        print("\n")
    #     if self.engine.revs_per_min > 0:
    #         # while self.has_enough_fuel(km, self.km_per_litre):
            #     self.consume_fuel(km)
            #     print("Drove {}km".format(km))
            #     print("{:.2f}l of fuel still left".format(self.fuel_tank.level))

    def park(self):
        print("\nParking...")
        self.dashboard.lights["handbreak"].is_on = True
        self.dashboard.show()
        self.engine.turnoff()

    def switch_fog_lights(self, status):
        print("\nSwitching {} fog lights...".format(status))
        boolean = True if status == "ON" else False
        self.dashboard.lights["fog"].is_on = boolean
        self.dashboard.show()

    def fill_up_tank(self):
        print("\nFuel tank filled up!")
        # self.fuel_tank.level = 100
def main():
   car = Car()
   car.start()
   # car.drive()
   car.switch_fog_lights("ON")
   car.switch_fog_lights("OFF")
   car.park()
   car.fill_up_tank()
   car.drive()
   car.start()
   car.drive()

if __name__ == "__main__":
    main()

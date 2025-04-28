
class Superhero:
    def __init__(self, name, power):
        self._name = name          
        self._power = power

    def show_power(self):
        print(f"{self._name} has the power of {self._power}!")


class FlyingHero(Superhero):
    def __init__(self, name, power, flight_speed):
        super().__init__(name, power)
        self.flight_speed = flight_speed

    def show_power(self):
        print(f"{self._name} can fly at {self.flight_speed} km/h with {self._power}!")


hero1 = Superhero("ShadowStrike", "Invisibility")
hero2 = FlyingHero("SkyBlaze", "Fire Control", 700)


hero1.show_power()
hero2.show_power()

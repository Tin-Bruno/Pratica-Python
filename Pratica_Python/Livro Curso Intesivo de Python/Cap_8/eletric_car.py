"""Importando classes."""

from car import Car


class Battery():
    """Uma tentativa simples de definir uma bateria."""

    def __init__(self, battery_size=70):
        """Inicializa a capacidade da bateria."""

        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""

        print("\tThis car has a "
              + str(self.battery_size)
              + "-kWh battery.")

    def get_range(self):
        """Mostra a distancia da bateria."""

        miles = 0

        if self.battery_size == 70:
            miles = 1000
        elif self.battery_size == 85:
            miles = 1200

        message = "\tThis car can go approximately " + str(miles)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Da um upgrade na bateria."""

        if self.battery_size >= 0:
            self.battery_size = 85


class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """inicializa os atributos específicos de um carro elétrico."""

        super().__init__(make, model, year)
        self.battery = Battery()

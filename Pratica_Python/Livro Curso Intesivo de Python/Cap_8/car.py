"""Pratica sobre classes"""


class Car():
    """Uma simples classe que representa um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Descreve o nome completo do carro."""

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""

        print("\tThis car: "
              + self.make.title()
              + " has "
              + str(self.odometer_reading)
              + " miles on it.")

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\nYou can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""

        self.odometer_reading += miles

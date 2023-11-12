"""Pratica sobre classes"""


class Restaurant():
    """Uma simples classe que representa um restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Descreve o restaurante"""

        print("\nName of the restaurant: " + self.restaurant_name)
        print("Cuisine type of the restaurant: " + self.cuisine_type)

    def open_restaurant(self):
        """Informa uma message de aberto para o restaurante"""

        print("\nOpening the restaurant...")

    def read_number_served(self):
        """Lé o número de serviços do restaurante"""

        print("\nNumber of served: " + str(self.number_served))

    def update_number_served(self, clients_served):
        """Atualiza o número de serviços do restaurante"""

        if clients_served >= self.number_served:
            self.number_served = clients_served
        else:
            print("You can't serve less than "
                  + str(self.number_served)
                  + " clients")

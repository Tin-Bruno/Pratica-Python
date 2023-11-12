from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Representa uma sorveteria."""

    def flavors_name(self):
        """Descreve os sabores do sorvete."""

        flavors = ["Chocolate", "Limão", "Morango"]
        print("\nThe Flavors to IceCreams is : " + str(flavors))

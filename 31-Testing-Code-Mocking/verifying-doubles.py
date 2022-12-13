from unittest.mock import MagicMock


class BurritoRow:
    restaurant = "Chipotle"

    @classmethod
    def steak_special(cls):
        return cls("steak", "white", 0)

    def __init__(self, protein, rice, guacamole):
        self.protein = protein
        self.rice = rice
        self.guacamole = guacamole

    def add_guac(self):
        self.guacamole += 1


lunch = BurritoRow.steak_special()
print(lunch.protein)
lunch.add_guac()
print(lunch.guacamole)

class_mock = MagicMock(spec=BurritoRow)
print(class_mock.restaurant)
print(class_mock.steak_special())
print(class_mock.steak_special().protein)

instance_mock = MagicMock(spec=BurritoRow.steak_special())
print(instance_mock.protein)
print(instance_mock.guacamole)
instance_mock.add_guac()

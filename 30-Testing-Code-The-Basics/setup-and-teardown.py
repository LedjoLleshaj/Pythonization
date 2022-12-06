import unittest


class Adress:
    def __init__(self, city, state):
        self.city = city
        self.state = state


class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Restaurant:
    def __init__(self, adress, owner):
        self.adress = adress
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age

    def summary(self):
        return f"{self.owner.name} is {self.owner_age} years old and owns a restaurant in {self.adress.city}"


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test
        and creates the objects that are needed
        """
        address = Adress("Berlin", "Berlin")
        owner = Owner("Max", 30)
        self.restaurant = Restaurant(address, owner)

    def tearDown(self):
        """This method is called after each test"""
        pass

    def test_owner_age(self):
        self.assertEqual(self.restaurant.owner_age, 30)

    def test_owner_name(self):
        self.assertEqual(self.restaurant.owner.name, "Max")


if __name__ == "__main__":
    unittest.main()

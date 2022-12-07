# a mock object simulates the behavior of a real object
# it is used to test the interaction between two objects

from unittest.mock import Mock

# create a mock object
pizza = Mock()
print(pizza)
print(type(pizza))

pizza.configure_mock(
    size="medium", price=12.99, toppings=["pepperoni", "sausage", "mushrooms"]
)

# mock objects have attributes that can be set
# pizza.size = "large"
# pizza.price = 15.99
# pizza.toppings = ["pepperoni", "sausage", "mushrooms"]

print(pizza.size)
print(pizza.price)

# mock objects have methods that can be called


print(pizza.non_existent_attribute.returns.another.mock.object)

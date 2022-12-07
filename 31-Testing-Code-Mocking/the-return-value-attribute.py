from unittest.mock import Mock

mock = Mock(return_value=3)
# mock.return_value = 3
print(mock())

stuntman = Mock()
stuntman.jump_off_building.return_value = "I'm flying!"
stuntman.light_on_fire.return_value = "I'm on fire!"

print(stuntman.jump_off_building())
print(stuntman.light_on_fire())

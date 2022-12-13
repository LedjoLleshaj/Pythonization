from unittest.mock import MagicMock, Mock

# magic mock supports also the magic methods while mock does not

plain_mock = Mock()
magic_mock = MagicMock()

# print(len(plain_mock)) # TypeError: object of type 'Mock' has no len() #Because it does not support magic methods
print(len(magic_mock))  # 0

print(magic_mock[3])

magic_mock.__len__.return_value = 5
print(len(magic_mock))  # 5

if magic_mock:
    print("magic is True")

magic_mock.__bool__.return_value = False

if magic_mock:
    print("magic_mock is True")
else:
    print("Not really..")

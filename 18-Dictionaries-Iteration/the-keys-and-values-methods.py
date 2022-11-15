cryptocurrency = {
    "Bitcoin": 16000,
    "Ethereum": 700,
    "Ripple": 0.5,
    "Litecoin": 200,
}

print(cryptocurrency.keys())
print(cryptocurrency.values())

for currency in cryptocurrency.keys():
    print(currency)

for price in cryptocurrency.values():
    print(price)

# being explicit is better
# we can use the .keys() method to iterate over the keys
# or we can use the .values() method to iterate over the values

print("Bitcoin" in cryptocurrency.keys()) #is better than print("Bitcoin" in cryptocurrency)
print(200 in cryptocurrency.values()) 

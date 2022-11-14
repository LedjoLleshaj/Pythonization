# we can access dictionary values by key or the get method
flight_prices = {
    "New York": 200,
    "Paris": 100,
    "London": 150
}
print(flight_prices["New York"]) # 200
# print(flight_prices["Rome"]) # KeyError: 'Rome'
# keys are case sensitive in dictionaries
gym_membership_packages = {
    29.99: ["Basic"],
    39.99: ["Standard", "Unlimited"],
    49.99: ["Premium", "Unlimited", "Personal Trainer"]
}

# get method returns the second argument if the key is not found
print(gym_membership_packages.get(29.99, ["Basic Dumbells"])) # ['Basic']
print(gym_membership_packages.get(19.99, ["Basic Dumbells"])) # ['Basic Dumbells']
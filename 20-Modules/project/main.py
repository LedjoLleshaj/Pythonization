# import feature.copyright
# import feature.subfeature.calculator
# print(feature.copyright.date_of_copy)
# print(feature.subfeature.calculator.add(1,2))

# from feature import subfeature
# from feature.subfeature import calculator
# print(calculator.add(1,2))

# from feature.subfeature.calculator import add
# print(add(1,2))

# since we are importing the calculator module from the subfeature module
# and we used the . notation to import the calculator module
# we can ow import directly the add function from the calculator module

import feature.subfeature
print(feature.subfeature.add(1,3))

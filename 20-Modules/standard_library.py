# python always imports some default modules that are called Standard library
# these modules are always available in python
# we can import them and use the functions defined in them
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.whitespace)
print(string.printable)
print(string.capwords("hello world"))

# string module link in github is here: https://github.com/python/cpython/blob/main/Lib/string.py

import math

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
print(math.sqrt(2))
print(math.sin(math.pi/2))
print(math.cos(math.pi/2))
print(math.tan(math.pi/2))
print(math.asin(1))
print(math.acos(0))
print(math.atan(1))
print(math.sinh(1))
print(math.cosh(1))
print(math.tanh(1))
print(math.asinh(1))
print(math.acosh(1))
print(math.atanh(0.5))
print(math.degrees(math.pi/2))
print(math.radians(90))
print(math.factorial(5))
print(math.gcd(12, 18))
print(math.isfinite(1))
print(math.isfinite(math.inf))
print(math.isfinite(math.nan))
print(math.isinf(1))
print(math.isinf(math.inf))
print(math.isinf(math.nan))
print(math.isnan(1))
print(math.isnan(math.inf))
print(math.isnan(math.nan))
print(math.isclose(1, 1.0000000000000001))
print(math.isclose(1, 1.0000000000000002))
print(math.ceil(1.1))
print(math.ceil(1.9))
print(math.floor(1.1))
print(math.floor(1.9))
print(math.trunc(1.1))
print(math.trunc(1.9))
print(math.copysign(1, -1))
print(math.copysign(1, 1))
print(math.fabs(-1))

import this # zen of python by Tim Peters
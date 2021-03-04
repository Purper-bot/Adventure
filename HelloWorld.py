import math
import os
import sys

import requests


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Daan"))
# r = requests.get("https://coreyms.com")
# print(r.status_code)

name = input("Your name?")
print("Hello,", name)

### Python Package Manager ###

# PIP 

import numpy  # python -m pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array*2)

import pandas # python -m pip install pandas

# PIP list # python -m pip list

# PIP uninstall pandas # python -m pip uninstall pandas

# PIP Show numpy ## python3 -m pip show numpy

import requests  ## python -m pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151") #sirve para hacer peticiones a un API
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))
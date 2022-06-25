# imports
import math

# function to convert random floats to integers
def floatConverter(generatedFloats):
    converted = []
    for num in generatedFloats:
        numInt = math.trunc(num)
        converted.append(numInt)
    return converted
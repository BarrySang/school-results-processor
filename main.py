# imports
import csv
import numpy
import float_converter as fc
import random_floats as rf

# ids
ids = list(range(1, 101))
print(ids)
# results
mathematics = fc.floatConverter(rf.randomFloats())
languages = fc.floatConverter(rf.randomFloats())
sciences = fc.floatConverter(rf.randomFloats())
humanities = fc.floatConverter(rf.randomFloats())

# open file to store results
resultsFile = open("results.csv", "w")
fileWriter = csv.writer(resultsFile)

# write titles
fileWriter.writerow(["ID", "MATHEMATICS", "LANGUAGES", "SCIENCES", "HUMANITIES"])

# enter ids and results
for id, mathematics, languages, sciences, humanities in zip(ids, mathematics, languages, sciences, humanities):
    fileWriter.writerow([id, mathematics, languages, sciences, humanities])
resultsFile.close()

from SpellChecker import SpellChecker
import sys

model = sys.argv[1]
testcorpus = sys.argv[2]
output = sys.argv[3]

if len(sys.argv)==5:
    algorithm = sys.argv[4]
else:
    algorithm = 'GIS'
sc = SpellChecker()
sc.checker(testcorpus, algorithm, model, output)

from SpellCheckerTrainer import SpellCheckerTrainer
import sys


corpus = sys.argv[1]
model = sys.argv[2]
if len(sys.argv) == 5:
    algorithm = sys.argv[3]
    iterations = int(sys.argv[4])
else:
    algorithm = 'GIS'
    iterations = 30

spt = SpellCheckerTrainer()
spt.trainingClassifiers(corpus, model, algorithm, iterations)


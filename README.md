Spell-Checker
=============

Problem:
Developing an approach to detect and correct errors arising from homophone confusion. The homophones under cnsideration are:
to too
their they're
your you're
its it's
lose loose
----------------------------------------------------------------------------------


The spell checker has been implemented as 5 binary maxent classifiers.

To train these classifiers:

python TrainSpellCheck.py corpus_file model_file [algorithm] [iterations]

Algorithm and iterations are not mandatory. default values : GIS and 30 respectively.
*Provide both values or none

To test a trained set of classifiers:

python TestSpellCheck.py model_file test_corpus_file output_file [algorithm]

*Algorithm needs to be provided to choose classifers other than GIS. These need to be pre trined though.


Here:

corpus_file : Single file containing all the text
model_file : Used to uniquely identify you set of models
test_corpus_file : Data on which the SpellChecker needs to be tested
output_file : Where the result of the SpellChecker is stored

Pre trained GIS model files for the SpellChecker are included in the model folder
to use them... algorithm = GIS and model_file = model

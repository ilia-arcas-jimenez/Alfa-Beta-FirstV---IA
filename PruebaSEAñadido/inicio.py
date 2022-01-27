import LucyNueva
import Neutro
#import Lucy1

import random
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
analizador = SentimentIntensityAnalyzer()
import tflearn
import json
import numpy
import pickle
import tensorflow

def JuanCalos3():
    sentences = input(">>:   ")
    scores = analizador.polarity_scores(sentences)
    scoAvg = (scores['compound'])
    inp = sentences
    if scoAvg == 0:
        valor = LucyNueva.LucyN(inp)
        print("El valor es: ", valor)
    elif scoAvg > 0:
        valor = LucyNueva.LucyN(inp)
        valor2 = Neutro.Lucy(inp) 
        print("El valor es: ", valor, valor2)
    elif scoAvg < 0:
        valor = LucyNueva.LucyN(inp)
        valor2 = Neutro.Lucy(inp)
        print("El valor es: ", valor, valor2)
    JuanCalos3()




JuanCalos3()
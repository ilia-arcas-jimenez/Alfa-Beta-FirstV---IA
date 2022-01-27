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
import random
import pickle
import tensorflow
#-------------------------------------------------------------------------------------------#
archivo2 = open("F:\desktop\importante\PROYECTOS DE PROGRAMACION\Python\sentimientos\PruebasSEAñadido\contenido.json")
datos2 = json.load(archivo2)
palabras2=[]
tags=[]
auxX2=[]
auxY2=[]
for contenido in datos2["contenido"]:
    for patrones in contenido["patrones"]:
        auxPalabra2 = nltk.word_tokenize(patrones)
        palabras2.extend(auxPalabra2)
        auxX2.append(auxPalabra2)
        auxY2.append(contenido["tag"])
        if contenido["tag"] not in tags:
            tags.append(contenido["tag"])

palabras2 = [stemmer.stem(w.lower()) for w in palabras2 if w!="?"]
palabras2 = sorted(list(set(palabras2)))
tags = sorted(tags)
aprendizaje2=[]
salida2=[]

salidaVacia2 = [0 for _ in range(len(tags))]
for x, documento in enumerate(auxX2):
    corchete2=[]
    auxPalabra2= [stemmer.stem(w.lower()) for w in documento]
    for w in palabras2:
        if w in auxPalabra2:
            corchete2.append(1)
        else:
            corchete2.append(0)
    filaSalida2 = salidaVacia2[:]
    filaSalida2[tags.index(auxY2[1])]=1
    aprendizaje2.append(corchete2)
    salida2.append(filaSalida2)

aprendizaje2 = numpy.array(aprendizaje2)
salida2 = numpy.array(salida2)
#-------------------------------------------------------------------------------------------#
red2 = tflearn.input_data(shape=[None,len(aprendizaje2[0])])
red2 = tflearn.fully_connected(red2,10)
red2 = tflearn.fully_connected(red2,10)
red2 = tflearn.fully_connected(red2,len(salida2[0]),activation="softmax")
red2 = tflearn.regression(red2)
modelo2 = tflearn.DNN(red2)
modelo2 .fit(aprendizaje2,salida2,n_epoch=1000,batch_size=10,show_metric=False)
modelo2 .save("modelo.tflearn")
#-------------------------------------------------------------------------------------------#
def Lucy(entrada):
    corchete = [0 for _ in range(len(palabras))]
    entradaProcesada = nltk.word_tokenize(entrada)
    entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
    for palabraInidvidual in entradaProcesada:
        for i,palabra in enumerate(palabras):
            if palabra == palabraInidvidual:
                corchete[i] = 1
    resultados = modelo.predict([numpy.array(corchete)])
    resultadosIndices = numpy.argmax(resultados)
    tag = tags[resultadosIndices]
    for tagAux in datos["contenido"]:
        if tagAux["tag"] == tag:
            respuesta = tagAux["respuestas"]
    return (random.choice(respuesta))
if __name__ == "__main__":
    Lucy(input(">>> "))

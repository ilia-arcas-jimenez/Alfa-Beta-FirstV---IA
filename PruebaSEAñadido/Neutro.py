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
archivo = open("F:\desktop\importante\PROYECTOS DE PROGRAMACION\Python\sentimientos\PruebasSEAñadido\contenido.json")
datos = json.load(archivo)

palabras=[]
tags=[]
auxX=[]
auxY=[]
for contenido in datos["contenido"]:
    for patrones in contenido["patrones"]:
        auxPalabra = nltk.word_tokenize(patrones)
        palabras.extend(auxPalabra)
        auxX.append(auxPalabra)
        auxY.append(contenido["tag"])
        if contenido["tag"] not in tags:
            tags.append(contenido["tag"])
palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
palabras = sorted(list(set(palabras)))
tags = sorted(tags)
aprendizaje=[]
salida=[]
salidaVacia = [0 for _ in range(len(tags))]
for x, documento in enumerate(auxX):
    corchete=[]
    auxPalabra= [stemmer.stem(w.lower()) for w in documento]
    for w in palabras:
        if w in auxPalabra:
            corchete.append(3)
        else:
            corchete.append(2)
    filaSalida = salidaVacia[:]
    filaSalida[tags.index(auxY[0])]=0
    aprendizaje.append(corchete)
    salida.append(filaSalida)

aprendizaje = numpy.array(aprendizaje)
salida = numpy.array(salida)
#-------------------------------------------------------------------------------------------#
red = tflearn.input_data(shape=[None,len(aprendizaje[0])])
red = tflearn.fully_connected(red,10)
red = tflearn.fully_connected(red,10)
red = tflearn.fully_connected(red,len(salida[0]),activation="softmax")
red = tflearn.regression(red)
modelo = tflearn.DNN(red)
modelo .fit(aprendizaje,salida,n_epoch=1000,batch_size=10,show_metric=False)
modelo .save("modelo2.tflearn")
#-------------------------------------------------------------------------------------------#
def Lucy(entrada):
    sentences = entrada
    scores = analizador.polarity_scores(sentences)
    scoAvg = (scores['compound'])
    if scoAvg > 0:
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/PruebasSEAñadido/Plus1.json",) as archivo:
            datosP = json.load(archivo)
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
        for tagAux in datosP["contenido"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuestas"]
        return (random.choice(respuesta))
    elif scoAvg < 0:
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/PruebasSEAñadido/Plus2.json",) as archivo2:
            datosN = json.load(archivo2)
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
        for tagAux in datosN["contenido"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuestas"]
        return (random.choice(respuesta))
if __name__ == "__main__":
    Lucy(input(">>> "))
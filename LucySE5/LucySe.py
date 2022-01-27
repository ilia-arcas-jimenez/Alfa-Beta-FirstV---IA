import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analizador = SentimentIntensityAnalyzer()
from nltk import sentiment
from nltk import word_tokenize
import tflearn
import json
import numpy
import random
import tensorflow
import time
import os

#--------------------------------#
entrada = ("bad boy memeguta")
sentences = entrada
scores = analizador.polarity_scores(sentences)
scoAvg = (scores['compound'])
if scoAvg == 0:
    with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE5/contenidoNeutro.json", ) as archivo:
        datosNeutros = json.load(archivo)
elif scoAvg > 0:
    with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE5/contenidoPositivo.json", ) as archivo:
        datosPositivos = json.load(archivo)
else:
    with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE5/contenidoNegativo.json", ) as archivo:
        datosNegativos = json.load(archivo)


palabras=[]
tags=[]
auxX=[]
auxY=[]
if scoAvg == 0: 
    for contenido in datosNeutros["contenido"]:
        for patrones in contenido["patrones"]:
            auxPalabra = nltk.word_tokenize(patrones)
            palabras.extend(auxPalabra)
            auxX.append(auxPalabra)
            auxY.append(contenido["tag"])
            if contenido["tag"] not in tags:
                tags.append(contenido["tag"])
elif scoAvg > 0:
    for contenido in datosPositivos["contenido"]:
        for patrones in contenido["patrones"]:
            auxPalabra = nltk.word_tokenize(patrones)
            palabras.extend(auxPalabra)
            auxX.append(auxPalabra)
            auxY.append(contenido["tag"])
            if contenido["tag"] not in tags:
                tags.append(contenido["tag"])
else:
    for contenido in datosNegativos["contenido"]:
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
            corchete.append(1)
        else:
            corchete.append(0)
    filaSalida = salidaVacia[:]
    filaSalida[tags.index(auxY[x])]=1
    aprendizaje.append(corchete)
    salida.append(filaSalida)
aprendizaje = numpy.array(aprendizaje)
salida = numpy.array(salida)


red = tflearn.input_data(shape=[None,len(aprendizaje[0])])
red = tflearn.fully_connected(red,10)
red = tflearn.fully_connected(red,10)
red = tflearn.fully_connected(red,len(salida[0]),activation="softmax")
red = tflearn.regression(red)
modelo = tflearn.DNN(red)

modelo .fit(aprendizaje,salida,n_epoch=1000,batch_size=10,show_metric=True)
modelo .save("modelo.tflearn")

def Lucy():
    entrada = input(">>>: ")
    sentences = entrada
    scores = analizador.polarity_scores(sentences)
    scoAvg = (scores['compound'])
    if scoAvg == 0:
        
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE4/contenidoNeutro.json",) as archivo:
            datosNeutros = json.load(archivo)
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
        for tagAux in datosNeutros["contenido"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuestas"]
        print("Lucy: ",random.choice(respuesta))
        return Lucy()
    elif scoAvg > 0:
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE4/contenidoPositivo.json",) as archivo:
            datosPositivos = json.load(archivo)
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
        for tagAux in datosPositivos["contenido"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuestas"]
        print("Lucy: ",random.choice(respuesta))
        #print ("esto esta arreglandose")
        return Lucy()



    else:
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE4/contenidoNegativo.json",) as archivo:
            datosNegativos = json.load(archivo)
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
        for tagAux in datosNegativos["contenido"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuestas"]
        print("Lucy: ",random.choice(respuesta))
        #print ("esto esta arreglandose")
        return Lucy()
#-----------------------------------------------------------------
#        tag = "aprendiendo"
#        pa1 = entrada
#        re1 = entrada
#
#        my_details_append = {"tag":tag,"patrones":[pa1],"respuesta":[re1]}
#        
#        archivo = open('ContenidoNegativo.json', )
#        data = json.load(archivo)
#            
#
#        
#        for contenido in archivo["contenido"]:
#            for tags in contenido["tag"]:    
#                for patrones in tags["patrones"]:
#                    if patrones['entrada'] == patron:
#
#                        print ("Lucy: ",random.choice(respuesta))
#                        return Lucy()
#        
#        data ['contenido'].append(my_details_append)
#        archivo.close()
#        archivo = open('contenidoNegativo.json', 'w')
#        archivo.write(str(data).replace("'","\""))
#        archivo.close()
#        #json.dump(data, "test.json")
#        return Lucy()
#----------------------------------------------------------------
Lucy()


import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
nltk.download('vader_lexicon')
nltk.download('punkt')
analizador = SentimentIntensityAnalyzer()
import tflearn
import json
import numpy
import random
import pickle
import tensorflow




entrada = input()
sentences = entrada
scores = analizador.polarity_scores(sentences)
print (scores)

if (scores['compound']) > 0:
    with open("contenidoPositivo.json") as archivo:
        datosPositivos = json.load(archivo)
    
    palabras=[]
    tags=[]
    auxX=[]
    auxY=[]
    
    for contenido in datosPositivos["contenido"]:
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
    modelo .fit(aprendizaje,salida,n_epoch=1000,batch_size=11,show_metric=True)
    modelo .save("modelo.tflearn")
    
    def LucySe():
        while True:
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
    LucySe()

else:
    with open("contenidoNegativo.json") as archivo:
        datosNegativos = json.load(archivo)
        
    palabras=[]
    tags=[]
    auxX=[]
    auxY=[]
    
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
    modelo .fit(aprendizaje,salida,n_epoch=1000,batch_size=11,show_metric=True)
    modelo .save("modelo.tflearn")
    
    def LucySe():
        while True:
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
            continue    
    
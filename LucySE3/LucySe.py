#import nltk
#nltk.download('vader_lexicon')
#nltk.download('punkt')
#from nltk.stem.lancaster import LancasterStemmer
#stemmer = LancasterStemmer()
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#analizador = SentimentIntensityAnalyzer()
#from nltk import sentiment
#from nltk import word_tokenize
#import tflearn
#import json
#import numpy
#import random
#import pickle
#import tensorflow
#import time
#import os
#
#
##def getByAddress(address):
##    return [x for x in globals().values() if id(x)==address]
##
##
##
###entrada = "bad boy memeguta"
###sentences = entrada
###sentences = "Love" # input(">> ")
###scores = analizador.polarity_scores(sentences)
###scoAvg = (scores['compound'])
##
##
##
###print("\n\nscores:")
###print(scores)
###print()
###print("scoAvg")
###print(scoAvg)
###if scoAvg == 0:
###    print("Neutro")
###elif scoAvg > 0:
###    with open("contenidoPositivo.json",) as archivo:
###        datosPositivos = json.load(archivo)
###else:
###    with open("contenidoNegativo.json",) as archivo:
###        datosNegativos = json.load(archivo)
###
### archivo = open("contenido.json")
### datos = json.load(archivo)
##palabras=[]
##tags=[]
##auxX=[]
##auxY=[]
##
###
###if scoAvg > 0: datosResul = id(datosPositivos["contenido"])
###if scoAvg < 0: datosResul = id(datosNegativos["contenido"])
###result = getByAddress(datosResul)
##
###print("\ndatosResul:")
###print(datosResul)
###print()
###print("result:")
###print(result)
##
###for contenido in result:
###    for patrones in contenido["patrones"]:
###        auxPalabra = nltk.word_tokenize(patrones)
###        palabras.extend(auxPalabra)
###        auxX.append(auxPalabra)
###        auxY.append(contenido["tag"])
###
###        if contenido["tag"] not in tags:
###            tags.append(contenido["tag"])
###
###
###palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
###palabras = sorted(list(set(palabras)))
###tags = sorted(tags)
###aprendizaje=[]
###salida=[]
###salidaVacia = [0 for _ in range(len(tags))]
###for x, documento in enumerate(auxX):
###    corchete=[]
###    auxPalabra= [stemmer.stem(w.lower()) for w in documento]
###    for w in palabras:
###        if w in auxPalabra:
###            corchete.append(1)
###        else:
###            corchete.append(0)
###    filaSalida = salidaVacia[:]
###    filaSalida[tags.index(auxY[x])]=1
###    aprendizaje.append(corchete)
###    salida.append(filaSalida)
###aprendizaje = numpy.array(aprendizaje)
###salida = numpy.array(salida)
###
##print("\n\naprendizaje:")
###print(aprendizaje)
###print("\n")
##aprendizaje=[] 
##salida=[]
##corchete=[]
##
##
##
##
##
### aprendizaje = [] (está vacío)
##
##red = tflearn.input_data(shape=[None,len(aprendizaje)])
##red = tflearn.fully_connected(red,10)
##red = tflearn.fully_connected(red,10)
##red = tflearn.fully_connected(red,len(salida),activation="softmax")
##red = tflearn.regression(red)
##modelo = tflearn.DNN(red)
##modelo .fit(aprendizaje,salida,n_epoch=1000,batch_size=11,show_metric=True)
##modelo .save("modelo.tflearn")
##def Lucy():
##    for contenido in result:
##        for patrones in contenido["patrones"]:
##            auxPalabra = nltk.word_tokenize(patrones)
##            palabras.extend(auxPalabra)
##            auxX.append(auxPalabra)
##            auxY.append(contenido["tag"])
##    
##            if contenido["tag"] not in tags:
##                tags.append(contenido["tag"])
##
##
##    palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
##    palabras = sorted(list(set(palabras)))
##    tags = sorted(tags)
##    
##   
##    salidaVacia = [0 for _ in range(len(tags))]
##    for x, documento in enumerate(auxX):
##        
##        auxPalabra= [stemmer.stem(w.lower()) for w in documento]
##        for w in palabras:
##            if w in auxPalabra:
##                corchete.append(1)
##            else:
##                corchete.append(0)
##        filaSalida = salidaVacia[:]
##        filaSalida[tags.index(auxY[x])]=1
##        aprendizaje.append(corchete)
##        salida.append(filaSalida)
##    aprendizaje = numpy.array(aprendizaje)
##    salida = numpy.array(salida)
##    while True:
##        entrada = input()
##        entrada = sentences
##        scores = analizador.polarity_scores(sentences)
##        scoAvg = (scores['compound'])
##        
##        corchete = [0 for _ in range(len(palabras))]
##        entradaProcesada = nltk.word_tokenize(entrada)
##        entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
##        for palabraInidvidual in entradaProcesada:
##            for i,palabra in enumerate(palabras):
##                if palabra == palabraInidvidual:
##                    corchete[i] = 1
##        resultados = modelo.predict([numpy.array(corchete)])
##        resultadosIndices = numpy.argmax(resultados)
##        tag = tags[resultadosIndices]
##        
##        if scoAvg > 0: datosResul = id(datosPositivos["contenidoPositivo"])
##        if scoAvg < 0: datosResul = id(datosNegativos["contenidoNegativo"])
##        result = getByAddress(datosResul)
##        
##        if (scoAvg) > 0:
##            for tagAux in result:
##                if tagAux["tag"] == tag:
##                    respuesta = tagAux["respuestas"]
##                print("Lucy: ",random.choice(respuesta))
#
#entrada = input(">>>: ")
#sentences = entrada
#scores = analizador.polarity_scores(sentences)
#scoAvg = (scores['compound'])
#
#if scoAvg == 0:
#    print("Neutro")
#elif scoAvg > 0:
#    with open("contenidoPositivo.json",) as archivo:
#        datosPositivos = json.load(archivo)
#else:
#    with open("contenidoNegativo.json",) as archivo:
#        datosNegativos = json.load(archivo)
#
#palabras=[]
#tags=[]
#auxX=[]
#auxY=[]
#if scoAvg == 0:
#    print("Neutro")
#elif scoAvg > 0:
#    for contenido in datosPositivos["contenido"]:
#        for patrones in datosPositivos["patrones"]:
#            auxPalabra = nltk.word_tokenize(patrones)
#            palabras.extend(auxPalabra)
#            auxX.append(auxPalabra)
#            auxY.append(contenidoPositivo["tag"])
#    
#            if datosPositivos["tag"] not in tags:
#                tags.append(datosPositivos["tag"])
#else:
#    for contenido in datosNegativos["contenido"]:
#        for patrones in contenido["patrones"]:
#            auxPalabra = nltk.word_tokenize(patrones)
#            palabras.extend(auxPalabra)
#            auxX.append(auxPalabra)
#            auxY.append(contenido["tag"])
#    
#            if contenido["tag"] not in tags:
#                tags.append(contenido["tag"])
#
#palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
#palabras = sorted(list(set(palabras)))
#tags = sorted(tags)
#aprendizaje=[]
#salida=[]
#
#salidaVacia = [0 for _ in range(len(tags))]
#for x, documento in enumerate(auxX):
#    corchete=[]
#    auxPalabra= [stemmer.stem(w.lower()) for w in documento]
#    for w in palabras:
#        if w in auxPalabra:
#            corchete.append(1)
#        else:
#            corchete.append(0)
#    filaSalida = salidaVacia[:]
#    filaSalida[tags.index(auxY[x])]=1
#    aprendizaje.append(corchete)
#    salida.append(filaSalida)
#
#aprendizaje = numpy.array(aprendizaje)
#salida = numpy.array(salida)
#
#
#red = tflearn.input_data(shape=[None,len(aprendizaje[0])])
#red = tflearn.fully_connected(red,10)
#red = tflearn.fully_connected(red,10)
#red = tflearn.fully_connected(red,len(salida[0]),activation="softmax")
#red = tflearn.regression(red)
#
#modelo = tflearn.DNN(red)
#modelo .fit(aprendizaje,salida,n_epoch=1000,batch_size=11,show_metric=True)
#modelo .save("modelo.tflearn")
##entrada = None
#def Lucy():
#    entrada = input(">>>: ")
#    sentences = entrada
#    scores = analizador.polarity_scores(sentences)
#    scoAvg = (scores['compound'])
#    if scoAvg == 0:
#        print("Neutro")
#    elif scoAvg > 0:
#    
#        with open("contenidoPositivo.json",) as archivo:
#            datosPositivos = json.load(archivo)
#        corchete = [0 for _ in range(len(palabras))]
#        entradaProcesada = nltk.word_tokenize(entrada)
#        entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
#        for palabraInidvidual in entradaProcesada:
#            for i,palabra in enumerate(palabras):
#                if palabra == palabraInidvidual:
#                    corchete[i] = 1
#        resultados = modelo.predict([numpy.array(corchete)])
#        resultadosIndices = numpy.argmax(resultados)
#        tag = tags[resultadosIndices]
#        for tagAux in datosPositivos["contenido"]:
#            if tagAux["tag"] == tag:
#                respuesta = tagAux["respuestas"]
#    
#        print("Lucy: ",random.choice(respuesta))
#        return Lucy()
#    else:
#        
#        with open("contenidoNegativo.json",) as archivo:
#            datosNegativos = json.load(archivo)
##          entrada = input(">>>: ")
#        corchete = [0 for _ in range(len(palabras))]
#        entradaProcesada = nltk.word_tokenize(entrada)
#        entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
#        for palabraInidvidual in entradaProcesada:
#            for i,palabra in enumerate(palabras):
#                if palabra == palabraInidvidual:
#                    corchete[i] = 1
#        resultados = modelo.predict([numpy.array(corchete)])
#        resultadosIndices = numpy.argmax(resultados)
#        tag = tags[resultadosIndices]
#
#        for tagAux in datosNegativos["contenido"]:
#            if tagAux["tag"] == tag:
#                respuesta = tagAux["respuestas"]
#        
#        print("Lucy: ",random.choice(respuesta))
#        return Lucy()
#Lucy()



#def getByAddress(address):
#    return [x for x in globals().values() if id(x)==address]
#
#
#
##entrada = "bad boy memeguta"
##sentences = entrada
##sentences = "Love" # input(">> ")
##scores = analizador.polarity_scores(sentences)
##scoAvg = (scores['compound'])
#
#
#
##print("\n\nscores:")
##print(scores)
##print()
##print("scoAvg")
##print(scoAvg)
##if scoAvg == 0:
##    print("Neutro")
##elif scoAvg > 0:
##    with open("contenidoPositivo.json",) as archivo:
##        datosPositivos = json.load(archivo)
##else:
##    with open("contenidoNegativo.json",) as archivo:
##        datosNegativos = json.load(archivo)
##
## archivo = open("contenido.json")
## datos = json.load(archivo)
#palabras=[]
#tags=[]
#auxX=[]
#auxY=[]
#
##
##if scoAvg > 0: datosResul = id(datosPositivos["contenido"])
##if scoAvg < 0: datosResul = id(datosNegativos["contenido"])
##result = getByAddress(datosResul)
#
##print("\ndatosResul:")
##print(datosResul)
##print()
##print("result:")
##print(result)
#
##for contenido in result:
##    for patrones in contenido["patrones"]:
##        auxPalabra = nltk.word_tokenize(patrones)
##        palabras.extend(auxPalabra)
##        auxX.append(auxPalabra)
##        auxY.append(contenido["tag"])
##
##        if contenido["tag"] not in tags:
##            tags.append(contenido["tag"])
##
##
##palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
##palabras = sorted(list(set(palabras)))
##tags = sorted(tags)
##aprendizaje=[]
##salida=[]
##salidaVacia = [0 for _ in range(len(tags))]
##for x, documento in enumerate(auxX):
##    corchete=[]
##    auxPalabra= [stemmer.stem(w.lower()) for w in documento]
##    for w in palabras:
##        if w in auxPalabra:
##            corchete.append(1)
##        else:
##            corchete.append(0)
##    filaSalida = salidaVacia[:]
##    filaSalida[tags.index(auxY[x])]=1
##    aprendizaje.append(corchete)
##    salida.append(filaSalida)
##aprendizaje = numpy.array(aprendizaje)
##salida = numpy.array(salida)
##
#print("\n\naprendizaje:")
##print(aprendizaje)
##print("\n")
#aprendizaje=[] 
#salida=[]
#corchete=[]
#
#
#
#
#
## aprendizaje = [] (está vacío)
#
#red = tflearn.input_data(shape=[None,len(aprendizaje)])
#red = tflearn.fully_connected(red,10)
#red = tflearn.fully_connected(red,10)
#red = tflearn.fully_connected(red,len(salida),activation="softmax")
#red = tflearn.regression(red)
#modelo = tflearn.DNN(red)
#modelo .fit(aprendizaje,salida,n_epoch=1000,batch_size=11,show_metric=True)
#modelo .save("modelo.tflearn")
#def Lucy():
#    for contenido in result:
#        for patrones in contenido["patrones"]:
#            auxPalabra = nltk.word_tokenize(patrones)
#            palabras.extend(auxPalabra)
#            auxX.append(auxPalabra)
#            auxY.append(contenido["tag"])
#    
#            if contenido["tag"] not in tags:
#                tags.append(contenido["tag"])
#
#
#    palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
#    palabras = sorted(list(set(palabras)))
#    tags = sorted(tags)
#    
#   
#    salidaVacia = [0 for _ in range(len(tags))]
#    for x, documento in enumerate(auxX):
#        
#        auxPalabra= [stemmer.stem(w.lower()) for w in documento]
#        for w in palabras:
#            if w in auxPalabra:
#                corchete.append(1)
#            else:
#                corchete.append(0)
#        filaSalida = salidaVacia[:]
#        filaSalida[tags.index(auxY[x])]=1
#        aprendizaje.append(corchete)
#        salida.append(filaSalida)
#    aprendizaje = numpy.array(aprendizaje)
#    salida = numpy.array(salida)
#    while True:
#        entrada = input()
#        entrada = sentences
#        scores = analizador.polarity_scores(sentences)
#        scoAvg = (scores['compound'])
#        
#        corchete = [0 for _ in range(len(palabras))]
#        entradaProcesada = nltk.word_tokenize(entrada)
#        entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
#        for palabraInidvidual in entradaProcesada:
#            for i,palabra in enumerate(palabras):
#                if palabra == palabraInidvidual:
#                    corchete[i] = 1
#        resultados = modelo.predict([numpy.array(corchete)])
#        resultadosIndices = numpy.argmax(resultados)
#        tag = tags[resultadosIndices]
#        
#        if scoAvg > 0: datosResul = id(datosPositivos["contenidoPositivo"])
#        if scoAvg < 0: datosResul = id(datosNegativos["contenidoNegativo"])
#        result = getByAddress(datosResul)
#        
#        if (scoAvg) > 0:
#            for tagAux in result:
#                if tagAux["tag"] == tag:
#                    respuesta = tagAux["respuestas"]
#                print("Lucy: ",random.choice(respuesta))
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
import pickle
import tensorflow
import time
import os


#os.system("cls")

#while True:
entrada = input(">>>: ")
#
#    os.system("cls")
#    #########################################
#
#    print(entrada+"?\n\nI say " + lolxD.saySomething()+"\n\n")
#
#
#
#    #########################################
#
#
sentences = entrada
scores = analizador.polarity_scores(sentences)
scoAvg = (scores['compound'])
if scoAvg == 0:
    with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE3/contenidoNeutro.json", ) as archivo:
        datosNeutros = json.load(archivo)
elif scoAvg > 0:
    with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE3/contenidoPositivo.json", ) as archivo:
        datosPositivos = json.load(archivo)
else:
    with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE3/contenidoNegativo.json", ) as archivo:
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
#entrada = None
def Lucy():
    entrada = input(">>>: ")
    sentences = entrada
    gulaf = ("gusa gusa")
    scores = analizador.polarity_scores(sentences)
    scoAvg = (scores['compound'])
    if entrada == gulaf:
        print ("gulaf gulaf uwu")
        return Lucy()
    if scoAvg == 0:
        
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE3/contenidoNeutro.json",) as archivo:
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
        print("Lucy: "+random.choice(respuesta))
        #print ("Hola, este sentimiento es neutro , no esta acabado xd")
        return Lucy()
    elif scoAvg > 0:
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE3/contenidoPositivo.json",) as archivo:
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
        return Lucy()



    else:
        with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE3/contenidoNegativo.json",) as archivo:
            datosNegativos = json.load(archivo)
#           entrada = input(">>>: ")
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
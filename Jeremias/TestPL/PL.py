import os
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
#import pickle
import tensorflow
import requests as req
from influxdb import InfluxDBClient
from flask import Flask, render_template, request


with open("E:/Bellum/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/contenido.json") as archivo:
    datos = json.load(archivo)


palabras = []
tags = []
auxX = []
auxY = []


for contenido in datos["contenido"]:
    for patrones in contenido["patrones"]:
        auxPalabra = nltk.word_tokenize(patrones)
        palabras.extend(auxPalabra)
        auxX.append(auxPalabra)
        auxY.append(contenido["tag"])

        if contenido["tag"] not in tags:
            tags.append(contenido["tag"])

palabras = [stemmer.stem(w.lower()) for w in palabras if w != "?"]
palabras = sorted(list(set(palabras)))
tags = sorted(tags)
aprendizaje = []
salida = []

salidaVacia = [0 for _ in range(len(tags))]
for x, documento in enumerate(auxX):
    corchete = []
    auxPalabra = [stemmer.stem(w.lower()) for w in documento]
    for w in palabras:
        if w in auxPalabra:
            corchete.append(1)
        else:
            corchete.append(0)
    filaSalida = salidaVacia[:]
    filaSalida[tags.index(auxY[x])] = 1
    aprendizaje.append(corchete)
    salida.append(filaSalida)


aprendizaje = numpy.array(aprendizaje)
salida = numpy.array(salida)


red = tflearn.input_data(shape=[None, len(aprendizaje[0])])
red = tflearn.fully_connected(red, 10)
red = tflearn.fully_connected(red, 10)
red = tflearn.fully_connected(red, len(salida[0]), activation="softmax")
red = tflearn.regression(red)


modelo = tflearn.DNN(red)
modelo .fit(aprendizaje, salida, n_epoch=1000, batch_size=11, show_metric=True)
modelo .save("modelo.tflearn")


contador = 0
def Jeremias():
    global contador
    contador = contador + 1
    entrada = input(">>>>>>>:")
    archivo = open('E:/Bellum/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/contenido.json', )
    data = json.load(archivo)
    exist = 0
    for contenido in data["contenido"]:
        for tags in contenido["tag"]:    
            for patrones in tags["patrones"]:
                if patrones['entrada'] == patron:
    #for contenido in data['contenido']:
    #    for tags in contenido['tag']:
    #        for patrones in tags['patrones']:
    #            if entrada['patrones'] == patron:
                    exist = 1
                    print ("este patrones ya existe")
            if exist == 0:
                print ("ESTO ES QUE NO EXISTE")
        #else:
        #    exist = 0

        
        #    data ['contenido'].append(my_details_append)
        #archivo.close()
        #archivo = open('test.json', 'w')
        #archivo.write(str(data).replace("'","\""))
        #archivo.close()
        #json.dump(data, "test.json")
        #else:
        #    with open('test.json', 'a') as json_file:
        #        json.dump(my_details, json_file)


        #AA = open('E:/Bellum/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/contenido.json')
        #archivo = json.load(AA)
        #
        #for contenido in archivo["contenido"]:
        #    #for tags in contenido["tag"]:    
        #        for patrones in contenido["patrones"]:
        #            if patrones['entrada'] == patron:
"""
                hola = entrada
                respP = req.get("http://localhost:6080/get?msg="+ hola)      
                respN = req.get("http://localhost:6081/get?msg="+ hola) 
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

                sentences = entrada
                scores = analizador.polarity_scores(sentences)
                scoAvg = (scores['compound'])
                NN = random.choice(respuesta)
                P = random.choice(respuesta), respP.text
                N = random.choice(respuesta), respN.text
                if scoAvg == 0:
                    turno = contador
                    if os.path.exists('test1.json'):
                        archivo = open('test1.json', )
                        data = json.load(archivo)
                        existenciaKawaixddd = 0
                        for turnos in data['succesion']:
                            if turnos['turno'] == turno:
                                existenciaKawaixddd = 1
                                print ("Este turno ya esta registrado")
                            else:
                                existenciaKawaixddd = 0
                        SUCCESIONES = {"turno":contador,
                            "tag":[tag],
                            "patron":[entrada],
                            "respuesta":[NN]
                            }
                        if existenciaKawaixddd == 0:
                            data ['succesion'].append(SUCCESIONES)
                        archivo.close()
                        archivo = open('test1.json', 'w')
                        archivo.write(str(data).replace("'","\""))
                        archivo.close() 
                    print ("Jeremias:", random.choice(respuesta))
                elif scoAvg >= 0:
                    turno = contador
                    if os.path.exists('test1.json'):
                        archivo = open('test1.json', )
                        data = json.load(archivo)
                        existenciaKawaixddd = 0
                        for turnos in data['succesion']:
                            if turnos['turno'] == turno:
                                existenciaKawaixddd = 1
                                print ("Este turno positivo ya esta registrado")
                            else:
                                existenciaKawaixddd = 0
                        SUCCESIONES = {"turno":contador,
                            "tag":[tag],
                            "patron":[entrada],
                            "respuesta":[random.choice(respuesta), respP.text]
                            }
                        if existenciaKawaixddd == 0:
                            data ['succesion'].append(SUCCESIONES)
                        archivo.close()
                        archivo = open('test1.json', 'w')
                        archivo.write(str(data).replace("'","\""))
                        archivo.close() 
                    print ("Jeremias:", random.choice(respuesta), respP.text)        
                elif scoAvg <= 0:
                    turno = contador

                    if os.path.exists('test1.json'):
                        archivo = open('test1.json', )
                        data = json.load(archivo)
                        existenciaKawaixddd = 0
                        for turnos in data['succesion']:
                            if turnos['turno'] == turno:
                                existenciaKawaixddd = 1
                                print ("Este turno negativo ya esta registrado")
                            else:
                                existenciaKawaixddd = 0
                        SUCCESIONES = {"turno":contador,
                            "tag":[tag],
                            "patron":[entrada],
                            "respuesta":[random.choice(respuesta), respN.text]
                            }
                        if existenciaKawaixddd == 0:
                            data ['succesion'].append(SUCCESIONES)
                        archivo.close()
                        archivo = open('test1.json', 'w')
                        archivo.write(str(data).replace("'","\""))
                        archivo.close() 
                    print ("Jeremias:", random.choice(respuesta), respN.text)
                else:
                    contador = 0
"""
                    
            
                #else:
                #    AB = open('E:/Bellum/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/testPL/test1.json')
                #    archivo1 = json.load(AB)
                #    contador2 = contador - 1
                #    for succesion in archivo1["succesion"]:
                #        for turnos in succesion["contador2"]:    
                #            for tags in turnos["tag"]:
                #                if tags["tag"] == ('saludo'):
                #                    AC = open('E:/Bellum/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/contenido.json')
                #                    archivo3 = json.load(AC)
                #                    for contenido in archivo3["contenido"]:
                #                        for tags in contenido["tag"]:    
                #                            for respuestas in tags["respuestas"]:
                #                                exritura = 0
                #                                RespuestanNueva = [entrada]
                #                                if escritura == 0:
                #                                    data ['respuestas'].append(RespuestanNueva)
                #                                archivo3.close()
                #                                archivo4 = open('E:/Bellum/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/contenido.json', 'w')
                #                                archivo4.write(str(data).replace("'","\""))
                #                                archivo4.close()
    #Jeremias()
Jeremias()

#SUCCESIONES = {"turno":contador,
#    "tag":[tag],
#    "patron":[entrada],
#    "respuesta":[NN, P, N]
#}
#if os.path.exists('test1.json'):
#    archivo = open('test1.json', )
#    data = json.load(archivo)
#    existenciaKawaixddd = 0
#    for turnos in data['succesion']:
#        if turnos['turno'] == turno:
#            existenciaKawaixddd = 1
#            print ("Este turno ya esta registrado")
#        else:
#            existenciaKawaixddd = 0
#    
#    if existenciaKawaixddd == 0:
#        data ['succesion'].append(my_details_append)
#    archivo.close()
#    archivo = open('test1.json', 'w')
#    archivo.write(str(data).replace("'","\""))
#    archivo.close()




        #json.dump(data, "test.json")
    #else:
    #    with open('test.json', 'a') as json_file:
    #        json.dump(my_details, json_file)
    #



#for i in range(0,19):
    
    #tag = input ("tag>>>>:")
    #pa1 = input ("patron1>>>>:")
    #pa2 = input ("patron2>>>>:")
    #pa3 = input ("patron3>>>>:")
    #pa4 = input ("patron4>>>>:")
    #pa5 = input ("patron5>>>>:")
    #pa6 = input ("patron6>>>>:")
        
    #re1 = input ("respuesta1>>>>:")
    #re2 = input ("respuesta2>>>>:")
    #re3 = input ("respuesta3>>>>:")
    #re4 = input ("respuesta4>>>>:")
    #re5 = input ("respuesta5>>>>:")
    #re6 = input ("respuesta6>>>>:")
#        
#    my_details = {
#        "contenido":[
#            {"tag":tag,
#            "patrones":[pa1,pa2,pa3,pa4,pa5,pa6],
#            "respuesta":[re1,re2,re3,re4,re5,re6]
#    }
#    ]   
#    }
#        
#    my_details_append = {   
#            "tag":tag,
#            "patrones":[pa1,pa2,pa3,pa4,pa5,pa6],
#            "respuesta":[re1,re2,re3,re4,re5,re6]
#    }
#
#
#
#
#
#archivo1 = open('test1.json', )
#info = json.load(archivo1)
#contador = contador - 1
#for succesion in archivo1["succesion"]:
#    for turnos in succesion["turno"]:    
#       if turnos['contador'] == turno:
#           contador = contador + 1
#           Jeremias()
#       else:
#       for patrones in tags["patrones"]:
#       if patrones['entrada'] == patron:
#       Jeremias()
#
#
#
#
#
#
#
#
#
#
#
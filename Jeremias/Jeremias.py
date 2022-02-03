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
global contador
contador = 0
#palabras=[]
#tags=[]
#auxX=[]
#auxY=[]
#
#for contenido in datos["contenido"]:
#    for patrones in contenido["patrones"]:
#        auxPalabra = nltk.word_tokenize(patrones)
#        palabras.extend(auxPalabra)
#        auxX.append(auxPalabra)
#        auxY.append(contenido["tag"])
#
#        if contenido["tag"] not in tags:
#            tags.append(contenido["tag"])
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
#
#
##import time,unittest
##from selenium import webdriver
## 
##pagina = webdriver.Firefox()
##pagina.get("http://localhost:6080")
##while True:
##    sent = pagina.find_element_by_name("textInput")
##    pin.clear()
##    pin.send_keys(entrada)
##    acceder = pagina.find_element_by_name("enviar")
##    acceder.click()
##    chico_malo=pagina.find_elements_by_xpath("//img[@src='access-denied.png']")
##    if len(chico_malo) == 1:
##        pagina.back()
##        numero+=1
##    else:
##        print(numero)
##        pagina.quit()
##

with open("F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/contenido.json") as archivo:
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


def Jeremias():
    entrada = input(">>>:")
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

    #NN = (random.choice(respuesta))
    #P = (random.choice(respuesta), respP.text)
    #N = (random.choice(respuesta), respN.text)

    if scoAvg == 0:
        #return
        print (tag)
        print ("Jeremias:", (random.choice(respuesta)))
        Jeremias()
    elif scoAvg >= 0:
        #return
        print (tag) 
        print ("Jeremias:", random.choice(respuesta), respP.text)
        Jeremias()
    else:
        #return 
        print (tag)
        print ("Jeremias:", random.choice(respuesta), respN.text)
        Jeremias()
Jeremias()

#app = Flask(__name__, template_folder='F:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/Jeremias/templates',
#                   static_folder='../chatbot/static', static_url_path='/static')
#
#@app.route("/get")
#def getBotResponse():
#    userText = ''
#    userText = request.args.get('msg')
#    if userText == "":
#        return str("No te entiendo")
#
#    return Jeremias(userText)
#
#@app.route('/')
#def principal():
#    return render_template('IAweb.html')
#if __name__ == "__main__":
#    app.debug=False
#    app.run(host="localhost", port=6082)
#------------------------------------------------------
#global numero
#numero = 0
#
#def contador(num):
#    num=num+1
#    return num
#
#while True:
#    contador(numero)
#    print(numero)
#--------------------------------------------------------


"""
Composicion de Frases
0-Analisis de Texto-Usuario compuesto 


1-Saludos
Saludar y preguntar como se esta
Saludo basico

2-Preguntas y respuestas
Preguntas de SI o NO
Preguntas de elaboracion
MIRAR PUNTO 0

3-Composicion de nuevas informaciones
Informacion nueva que sera clasificada segun su tag como nueva respuesta

4-Ironia y Sarcasmo
Expresiones sarcasticas

5-Aprender otros idiomas
    1.Castellano
"""

"""
1-Nacer
2-Aprender
3-Comprender
4-Practicar
5-Usar 
"""

"""
como te llamas?
Me llamo Jeremias
"""
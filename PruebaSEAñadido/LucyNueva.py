import tensorflow as tf
import random
import json
import pickle
import numpy as np 
import nltk 
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
lemmatizer = WordNetLemmatizer()
contenidos = json.load(open('F:\desktop\importante\PROYECTOS DE PROGRAMACION\Python\sentimientos\PruebasSEAñadido\contenido.json'))

words = []
tags= []
documents = []
ignore_letters = ['?', '!', '.', ',']

for contenido in contenidos['contenido']:
    for patrones in contenido['patrones']:
        word_list = nltk.word_tokenize(patrones)
        words.extend(word_list)
        documents.append((word_list, contenido['tag']))
        if contenido['tag'] not in tags:
            tags.append(contenido['tag'])
words =[lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
tags= sorted(set(tags))  
aprendizaje =[]
output_vacio = [0] * len(tags) 
for document in documents:
    mochila = []
    word_patroness = document[0]
    word_patroness = [lemmatizer.lemmatize(word.lower()) for word in word_patroness]  
    for word in words:
        if word in words:
            mochila.append(1) if word in word_patroness else mochila.append(0)
    output_row = list(output_vacio)
    output_row[tags.index(document[1])] = 1
    aprendizaje.append([mochila, output_row])


random.shuffle(aprendizaje)
aprendizaje = np.array(aprendizaje)

aprendizaje_x = list(aprendizaje[:, 0])
aprendizaje_y = list(aprendizaje[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(aprendizaje_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(aprendizaje_y[0]), activation='softmax'))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(np.array(aprendizaje_x), np.array(aprendizaje_y), epochs=1000, batch_size=10, verbose=1)
model.save('modeloNuevo.tflearn')

model.call = tf.function(model.call)

model = load_model('modeloNuevo.tflearn')

def limpiar_frases(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
def mochila_palabras(sentence):
    sentences_words = limpiar_frases(sentence)
    mochila = [0] * len(words)
    for w in sentences_words:
        for i, word in enumerate(words):
            if word == w:
                mochila[i] = 1
def predict_class(sentence):
        sentences_words = limpiar_frases(sentence)
        bow = mochila_palabras(sentence)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        resultado = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        resultado.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'contenido': classes[r[0]], 'probability': str(r[1])})
        return return_list
def get_response(intents_list, intents_json):
    tag = intents_list[0]['contenido']
    list_of_intents = intents_json['contenido']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['respuesta'])
            break
    return result

def LucyN(menssage):
    ints = predict_class(menssage)
    res = get_response(ints, contenidos)
    return res
if __name__ == "__main__":
    LucyN(input(">>> "))
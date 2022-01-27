import random
import json
import time


with open ("E:/desktop/importante/PROYECTOS DE PROGRAMACION/Python/sentimientos/LucySE3/dictionary.json") as archivo:
    content = json.load(archivo)


#    for contenido in content("contenido"):
#        p
        
def saySomething():
        return content[random.randrange(0, 300000, 1)]

if __name__=="__main__":
    while True:
        print(saySomething())
        time.sleep(1)

import json
import os
print("Comienzo")
for i in range(0,19):
    
    tag = input ("tag>>>>:")
    pa1 = input ("patron1>>>>:")
    pa2 = input ("patron2>>>>:")
    pa3 = input ("patron3>>>>:")
    pa4 = input ("patron4>>>>:")
    pa5 = input ("patron5>>>>:")
    pa6 = input ("patron6>>>>:")
        
    re1 = input ("respuesta1>>>>:")
    re2 = input ("respuesta2>>>>:")
    re3 = input ("respuesta3>>>>:")
    re4 = input ("respuesta4>>>>:")
    re5 = input ("respuesta5>>>>:")
    re6 = input ("respuesta6>>>>:")
        
    my_details = {
        "contenido":[
            {"tag":tag,
            "patrones":[pa1,pa2,pa3,pa4,pa5,pa6],
            "respuesta":[re1,re2,re3,re4,re5,re6]
    }
    ]   
    }
        
    my_details_append = {   
            "tag":tag,
            "patrones":[pa1,pa2,pa3,pa4,pa5,pa6],
            "respuesta":[re1,re2,re3,re4,re5,re6]
    }
       
        
        
        
        
    if os.path.exists('test.json'):
        archivo = open('test.json', )
        data = json.load(archivo)
        exist = 0
        for tags in data[
            'contenido'
        ]:
            if tags['tag'] == tag:
                exist = 1
                print ("este tag ya existe")
            #else:
            #    exist = 0
        
        if exist == 0:
            data [
                'contenido'
            ].append(my_details_append)
        archivo.close()
        archivo = open('test.json', 'w')
        archivo.write(str(data).replace("'","\""))
        archivo.close()
        #json.dump(data, "test.json")
    else:
        with open('test.json', 'a') as json_file:
            json.dump(my_details, json_file)
    

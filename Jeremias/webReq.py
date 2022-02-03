#import time,unittest
#from selenium import webdriver
#entrada = input(">>>>: ") 
#service = Service(executable_path="C:/Users/iliam/Downloads/chromedriver_win32")
#pagina = webdriver.Chrome(service=service)
#pagina.get("http://localhost:6080")
#while True:
#    sent = pagina.find_element_by_name("textInput")
#    sent.clear()
#    sent.send_keys(entrada)
#    acceder = pagina.find_element_by_name("buttonInput")
#    acceder.click()
#    respuesta = pagina.find_element_by_name("botText")
#    pagina.quit()
#hola = input(">>:")
import requests as req
while True:
    hola = input(">>:")
    resp = req.get("http://localhost:6080/get?msg="+ hola)
    print(resp.text)






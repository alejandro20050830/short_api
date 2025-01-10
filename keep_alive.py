from threading import Thread
import requests
import time


def cargar_pagina():
    urls=["https://uniswap-k2xr.onrender.com","https://tecnomundoweb.onrender.com"]
    while True:
        for url in urls:
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
    
                print("alive")
            else:
    
                print(respuesta.text)
    
        time.sleep(30)


def keep_alive():

    t1 = Thread(target=cargar_pagina)

    t1.start()


keep_alive()

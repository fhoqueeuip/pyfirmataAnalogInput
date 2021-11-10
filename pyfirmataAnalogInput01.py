#==============================================================#
#Este código es básico para la comunicación con la tarjeta Arduino
#mediante pyfirmata
#
# En este codigo hay 2 opciones descritas para leer el valor del pin deseado
#El codigo StandardFirmata debe estar instalado previamente
#en la tarjeta arduino
#
#By Francisco Hoquee
#ver: 001
#2021
#==============================================================#

import pyfirmata
import csv
import time
import datetime



#==============================================================#
port = 'com3' #Se selecciona el com que este usando el arduino en la computadora
board = pyfirmata.Arduino(port)
#==============================================================#

#============================================================== 
#Este fragmento se requiere para empiece a obtener lecturas de
#los pines del arduino.
it = pyfirmata.util.Iterator(board)
it.start()
#==============================================================#

#==============================================================#
#Define el pin
#Veo dos formas de hacerlo
#opcion 1
#analogIn0 = board.analog[0]
#analogIn0.enable_reporting()   #se requiere para obtener lectura (opcion 1)
#opcion 2
analogIn0 = board.get_pin('a:0:i')
#==============================================================#

while True:
    #repite el ciclo
    lecture = analogIn0.read() #se Requiere para las dos opciones
    print(lecture)
    print(type(lecture)) #los valores optenidos son de la clase float
  time.sleep(0.5)
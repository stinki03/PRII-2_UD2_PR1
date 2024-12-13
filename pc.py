import datetime
import socket
import time
import binascii
import sys
HOST = sys.argv[1]
PORT = sys.argv[2]
contador = 0
while True:
    contador = contador +1
    t1 = datetime.datetime.now()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    #    print(f"Connected")
        #Enviamos cadena de tiempo a unai
        tiempo = t1.strftime("%H:%M:%S.%f")[:-3]
        cadena = str(tiempo) + " + " +  str(contador)
    #    print(f"enviado {cadena}")        
        s.sendto(cadena.encode(),(HOST,int(PORT)))

        #Recibimos cadena de texto
        data,server = s.recvfrom(1024)
        t3 = datetime.datetime.now()
        print(f"Connected")
        
        
        t2 = datetime.datetime.now()

        Delay1 = t3 - t1
        Delay2= t2-t1
        print(f"Delay t3-t1 {Delay1}   Delay T2-t1 {Delay2}" )
        time.sleep(float(sys.argv[3]))

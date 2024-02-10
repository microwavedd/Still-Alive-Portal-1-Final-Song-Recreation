import time
import sys

def mostrar_mensaje(mensaje):
    sys.stdout.write('\r' + mensaje)
    sys.stdout.flush()

print("hola", end='')
time.sleep(1)
mostrar_mensaje("adios")
time.sleep(1)

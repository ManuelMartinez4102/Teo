import random
import pickle
import math
import matplotlib.pyplot as plt
from collections import Counter



def recopilar_mensajes():
  # Simulacion de un mensaje mandado de un usuario
  mensajes = ["Hola", "bien", "vale", "okay", "weeeee", "veeeee"]
  mensaje = random.choice(mensajes)
  mensajes_recopilados = {
      "mensaje": mensaje

  }
  return mensajes_recopilados

#"Transmicion de los mensajes"

def transmicion_de_mensaje(mensajes_recopilados):
    mensaje_codificado = ''.join(format(ord(c), '08b') for c in mensajes_recopilados["mensaje"])
    mensaje_transmitidos = {
        "mensaje": mensaje_codificado
    }
    print( mensaje_transmitidos)
    return mensaje_transmitidos

#Canal.


def fibra_optica(mensaje_transmitidos):
    mensaje_codificado = mensaje_transmitidos["mensaje"]
    mensaje_con_ruido = mensaje_transmitidos.copy()

    #los datos de la fibra optica
    velocidad_ms = 940000
    longitud_m = 2000
    tiempo = longitud_m / velocidad_ms

    #meter los de la cosa de entropia

    valores_random = [0,1, 2, 2, 3, 5, 7, 10, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    #valores_random = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    num_random = random.choice(valores_random)
    #donde puede caer
    porcentaje_ruido = [0, 5, 7, 1, 9, 10, 2, 12]

   #algo que digo el profe de un contador de veces
    contador = Counter(valores_random)

    #los calculos
    total_eventos = len(valores_random)
    probabilidades = [contador[valor] / total_eventos for valor in porcentaje_ruido]
    entropiaH = [-p * math.log2(p) if p > 0 else 0 for p in probabilidades]
    entropia = -sum(p * math.log2(p) for p in probabilidades if p > 0)


    #ya solo es implementar un ruido

    if num_random in porcentaje_ruido:
        for i in range(len(mensaje_codificado)):
            if random.random() < num_random:
                mensaje_con_ruido["mensaje"] = mensaje_con_ruido["mensaje"][:i] + ('0' if mensaje_codificado[i] == '1' else '1') + mensaje_con_ruido["mensaje"][i+1:]
            #else:
             # print("no entro al ruido")
    return tiempo, probabilidades, entropiaH, entropia, porcentaje_ruido , mensaje_con_ruido




#El que recibe con poco ruido
def receptor(mensaje_con_ruido):
    mensaje_codificado_con_ruido = mensaje_con_ruido["mensaje"]
    print(mensaje_con_ruido )
    cadena_binaria = mensaje_con_ruido["mensaje"]
    bytes_binarios = [cadena_binaria[i:i+8] for i in range(0, len(cadena_binaria), 8)]
    cadena_ascii = ""

    for byte in bytes_binarios:
      valor_decimal = int(byte, 2)
      print(valor_decimal)
      caracter_ascii = chr(valor_decimal)
      cadena_ascii += caracter_ascii

    print(cadena_ascii)
    datos_decodificados1 = {
        
        "El mensaje final": cadena_ascii
    }
    return datos_decodificados1

#Simulamos la llegada del  mensaje
print("mensaje original")
mensaje_a_mandar = recopilar_mensajes()
print(mensaje_a_mandar)
print("✔✔")

# las funciones

mensaje_transmitido = transmicion_de_mensaje(mensaje_a_mandar)
tiempo, probabilidades, entropiaH, entropia, porcentaje_ruido , mensaje_con_ruido= fibra_optica(mensaje_transmitido)
print("con ruido")
datos_decodificados1= receptor(mensaje_con_ruido)

print(f"\nEl tiempo de llegada del mensaje es de : {tiempo} segundos\n")


print()
print()

res4 = input("Quieres ver las probabilidades con sus entropias en H? 1 si , 2 no : ")
res4 = int(res4)
if res4 == 1:
  print()
  print("probavilidades")
  for i, probabilidad in enumerate(probabilidades, 1):
    print(f"probabililidad {i}: {probabilidad} ")
  print()
  print("entropias")
  for i, entro in enumerate(entropiaH, 1):
    print(f"Entropia {i}: {entro} bits")
  print(f"Entropía Total: {entropia:.10f} bits\n")

#Resultados

print(f"Datos originales:",mensaje_a_mandar)
print()
print(f"Datos transmitidos:", mensaje_transmitido)
print()
print(f"Datos con ruido:", mensaje_con_ruido)
print()
print(f"mensaje que llego :",datos_decodificados1)

#bien "01100010011010010110010101101110"
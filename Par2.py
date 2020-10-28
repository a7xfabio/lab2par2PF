#Este codigo realiza el procesamiento de dos archivos diferentes, por el cual se pide encontrar
#la cantidad de palabra, caracteres, letras, lineas y caracteres especiales.
from time import time
#La libreria time se utiliza para llevar el tiempo de ejecucion del codigo

def menu():   #Se crea la funcion del Menu de 3 opciones.
    print("Seleccione entre estos archivos palabras_ingles o deutsch")
    print("1. Procesamiento del archivo palabras_ingles")
    print("2. Procesamiento del archivo deutsch")
    print("3. Salir")
    while True: 
        #Se crea un blucle para que el menu no desaparezca a menos que se seleccione la opcion 3.
        try:
            seleccion=int(input("selecciona 1 , 2  o  3: "))
            if seleccion==1:
                archivo1()
                break
            elif seleccion==2:
                archivo2()
                break
            elif seleccion==3:
                break
            else: 
                 #Se crea parametros para caracteres que no son validos como otros numeros o letras.
                print("Caracter Invalido. Presione 1 , 2 o 3!")
                menu()
        except ValueError:
            print("Caracter Invalido. Presione 1 , 2 o 3!")
    exit
# Funcion "archivo1" que llama la opcion 1:
def archivo1():
    #Manda abrir el archivo txt para su procesamiento
    with open ('palabras_ingles.txt') as palabras_ingles:
        contenido_archivo = palabras_ingles.read()
    #Extructura de codigo que manda a llamar a los caracteres y caracteres especiales:
    z=str(contenido_archivo)
    s=z
    caracteres=0
    caracteres_especiales=0
    x=len(s)
    for i in range(0,x,1):
        if ((ord(s[i]) >= 97) and (ord(s[i]) <= 122)):
            caracteres=caracteres+1
        elif ((ord(s[i]) >= 65) and (ord(s[i]) <= 90)):
            caracteres_especiales+=1
        #codigo que separa el archivo para encontrar las palabras
        else:
            palabras = contenido_archivo.split()
            num_palabras = len(palabras)
    #Abrimos el archivo con otro nombre 
    archivo_pi = open("palabras_ingles.txt", "r")
    #Readlines recoge todas las lineas del archivo txt
    print("Lineas: " + str(len(archivo_pi.readlines())))
    print("caracteres: %d \ncaracteres especiales: %d " %(caracteres,caracteres_especiales))
    print ("Palabras:  " + str(num_palabras))
    print ('Duracion: {} segundos'.format(time() - inicio))
    anykey=input("Presiona Enter para regresar al inicio") 
    menu()
# Funcion "archivo12" que llama la opcion 2:
def archivo2():
    #Manda abrir el archivo txt para su procesamiento
    with open ('deutsch.txt') as deutsch:
        contenido_archivo = deutsch.read()
    #Extructura de codigo que manda a llamar a los caracteres y caracteres especiales:
    z=str(contenido_archivo)
    s=z
    caracteres=0
    caracteres_especiales=0
    x=len(s)
    for i in range(0,x,1):
        if ((ord(s[i]) >= 97) and (ord(s[i]) <= 122)):
            caracteres=caracteres+1
        elif ((ord(s[i]) >= 65) and (ord(s[i]) <= 90)):
            caracteres_especiales+=1
        #codigo que separa el archivo para encontrar las palabras
        else:
            palabras = contenido_archivo.split()
            num_palabras = len(palabras) 
    #Abrimos el archivo con otro nombre 
    archivo_ae = open("deutsch.txt", "r")
    print("Lineas: " + str(len(archivo_ae.readlines())))
    print("caracteres: %d \n caracteres especiales: %d" %(caracteres,caracteres_especiales,))
    print ("Palabras:  " + str(num_palabras))
    print ('Duracion: {} segundos'.format(time() - inicio))
    anykey=input("Presiona Enter para regresar al inicio") 
    menu()
#Primera rutina
inicio = time()
menu()

        
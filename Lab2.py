#Este codigo realiza el procesamiento de dos archivos diferentes, por el cual se pide encontrar
#la cantidad de palabra, caracteres, letras, lineas y caracteres especiales.

#Librerias a utilizar re y time 
#La libreria re se ocupa para realizar operaciones con expresiones regulares
#La libreria time se utiliza para llevar el tiempo de ejecucion del codigo
import re
from time import time

#El archivo1 = palabras_ingles.txt
#El archivo2 = american_english.txt

def menu():   #Se crea la funcion del Menu de 3 opciones.
    print("Seleccione entre estos archivos palabras_ingles o american_english")
    print("1. Procesamiento del archivo palabras_ingles")
    print("2. Procesamiento del archivo american_english")
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



# Funcion "archivo2" que llama la opcion 2:
#archivo = nombre del archivo
def archivo2():
    archivo = 'american_english.txt'  

    try:
        with open ("american_english.txt", "r") as american_english: 
             #Se manda a llamar al archivo de texto y se le asigna una variable.
            contenido_archivo = american_english.read()
            
    except FileNotFoundError:
        msg = "El archivo" + archivo + "no existe"
         # SI el archivo no existe, manda un mensaje de alerta.
        print(msg)

    else:   
        #Da comienzo a las diferentes peticiones del usuario:
        palabras = contenido_archivo.split()
        num_palabras = len(palabras)

        #Parametro que manda a llamar la cantidad de palabras
        print ("El archivo " + archivo + "  contiene  " + str(num_palabras) + " palabras") 

        #Apertura del archivo de texto.
        #archivo_ae hace referencia al txt "american_english"
        archivo_ae = open("american_english.txt", 'r') 

        # Parametro que manda a llamar la cantidad de lineas del texto
        print("El archivo tiene " + str(len(archivo_ae.readlines())) + " lineas")
        archivo_ae.close()

        cont = 0 
        for lineas in contenido_archivo:
            contar_caracteres=re.findall("(\S)", lineas.strip())
            if contar_caracteres:
                cont += len(contar_caracteres)
        cantidad_caracteres = len(contenido_archivo)
        # Parametro que manda a llamar a los caracteres del archivo:
        print("el archivo tiene", cantidad_caracteres , "caracteres con espacio") 
        print("el archivo tiene" , cont , "caracteres sin espacios")

        #transf_archivo hace referencia a la trasnformacion del contenido del archivo a una lista
        transf_archivo= list(contenido_archivo)
        contador = 0
        for mayus in transf_archivo:
            if mayus.isupper():
                contador += 1
                #Parametro que manda a llamar a los caracteres especiales:
        print("El archivo contiene " + str(contador) + " caracteres especiales") 
        print ('Duracion: {} segundos'.format(time() - inicio))

        #Parametro que indica el fin del proceso y da la opcion de regresar al menu principal.
    anykey=input("Presiona Enter para regresar al inicio") 
    menu()

# Funcion "archivo1" que llama la opcion 1:
def archivo1():
    archivo = 'palabras_ingles.txt'  

    try:
        with open ("palabras_ingles.txt", "r") as palabras_ingles: 
             #Se manda a llamar al archivo de texto y se le asigna una variable.
            contenido_archivo = palabras_ingles.read()
            
    except FileNotFoundError:
        msg = "El archivo" + archivo + "no existe"
         # SI el archivo no existe, manda un mensaje de alerta.
        print(msg)

    else:   
        #Da comienzo a las diferentes peticiones del usuario:
        palabras = contenido_archivo.split()
        num_palabras = len(palabras)

        #Parametro que manda a llamar la cantidad de palabras
        print ("El archivo " + archivo + "  contiene  " + str(num_palabras) + " palabras") 

        #Abrimos nuevamente el archivo de texto.
        #archivo_pi hace referencia al txt palabras_ingles.
        archivo_pi = open("palabras_ingles.txt", 'r') 

        # Parametro que manda a llamar la cantidad de lineas del texto
        print("El archivo tiene " + str(len(archivo_pi.readlines())) + " lineas")
        archivo_pi.close()

        cont = 0 
        for lineas in contenido_archivo:
            contar_caracteres=re.findall("(\S)", lineas.strip())
            if contar_caracteres:
                cont += len(contar_caracteres)
        cantidad_caracteres = len(contenido_archivo)
        # Parametro que manda a llamar a los caracteres del archivo:
        print("el archivo tiene", cantidad_caracteres , "caracteres con espacio") 
        print("el archivo tiene" , cont , "caracteres sin espacios")

        #transf_archivo hace referencia a la trasnformacion del contenido del archivo a una lista
        transf_archivo= list(contenido_archivo)
        contador = 0
        for mayus in transf_archivo:
            if mayus.isupper():
                contador += 1
                #Parametro que manda a llamar a los caracteres especiales:
        print("El archivo contiene " + str(contador) + " caracteres especiales") 
        print ('Duracion: {} segundos'.format(time() - inicio))

        #Parametro que indica el fin del proceso y da la opcion de regresar al menu principal.
    anykey=input("Presiona Enter para regresar al inicio") 
    menu()
    
#Primera Rutina
inicio = time()
menu()

import datetime
import os
import time
import msvcrt

fecha_hoy = datetime.datetime.now()                                       # Tomamos la fecha de hoy para el nombre del archivo
formato_personalizado = "%Y-%m-%d %H %M"                             # Agregamos formato a la fecha

fecha_hora = fecha_hoy.strftime(formato_personalizado)       # Creamos una fecha personalizada 

directorio_actual = os.getcwd()                                         # Obtén la ruta del directorio actual

archivos_en_directorio = os.listdir(directorio_actual)                  # Lista todos los archivos en el directorio actual                  

archivos_de_texto = [archivo for archivo in archivos_en_directorio if archivo.endswith(".txt")]     # Filtra los archivos de texto




def limpiar_consola():
    os.system("cls")

def nueva_hoja():

    nombre_hoja = input("Digita un nombre para esta hoja,para usar nombre por defecto presiona enter: ")

    if nombre_hoja == "":
        nombre_hoja = str(fecha_hora)

    notas_del_dia = input(">>> ")                                       # Almacenamos todo el texto en la variable notas del dia
    
    with open(nombre_hoja +".txt","w") as archivo:                    # Creamos el archivo en la ruta actual con la fecha de "hoy"
        archivo.write(notas_del_dia)                                    # Escribimos en el archivo las notas del dia

    print("Archivo guardado exitosamente!".center(100,"-") + "\n")      # Enviamos un mensaje de error

    time.sleep(2)                                                       # Esperamos 2 segundos para que el usuario lea el mensaje 

    limpiar_consola()                                                   # limpiamos la consola 

def buscar_hoja():
    while True:  
        try:    
            fecha = input("Digite la fecha(año-mes-dia) o el nombre de la hoja que desea buscar: ") #Se Pide al usuario la fecha o nombre de la hoja 
        
            with open(fecha + ".txt","r") as archivo:
                print("-"*100)      #separador
                for lector in archivo:
                    print(lector)
                print("-"*100)      #separador
            
                input("Presione enter para salir al menu principal...")
                limpiar_consola()
                break

        except FileNotFoundError:               #si no se encuentra la hoja 
            print("La fecha o nombre de la hoja es incorrecta o no existe")     
        except Exception:
            print("Error desconocido!")

def mostrar_diario(archivos):
    limpiar_consola()          
    for archivo in archivos:    
        ruta_archivo = os.path.join(directorio_actual, archivo)
        with open(ruta_archivo, "r") as f:
            contenido = f.read()
            print(f"Contenido de '{archivo}':")
            print(contenido)
            print("=" * 40)  # Separador entre archivos
            print("Presiona una tecla para continuar...")
            msvcrt.getch()  # Espera hasta que el usuario presione una tecla
            limpiar_consola()

if __name__ == "__main__":                                              # Definimos el main del programa

                                                         
    while True:                                                         # bucle principal del programa

        print(" Bienvenido a tu diario ".center(100,"="),end="\n\n")    #
        print("1.Escribir nueva hoja".center(100," "))                  # Menu
        print("2.Buscar hoja".center(91," "))                      #
        print("3.Mostrar diario completo".center(103," "))              #
        print("4.Salir".center(85," "))
    
        response = int(input("Que deseas hacer: "))                     # Respuesta
        
        if response == 1:                                               # Si la respuesta del usuario es 1 
            nueva_hoja()            

        elif response == 2:                                             # Si la respuesta del usuario es 2 
            buscar_hoja()

        elif response == 3:                                             # Si la respuesta del usuario es 3
            mostrar_diario(archivos_de_texto)
            if archivos_en_directorio == ["main.py","readme.md"]:
                print("No hay archivo creados aun".center(100,"-"))
                time.sleep(2)
                limpiar_consola()
        elif response == 4:                                             # Si la respuesta del usuario es 4
            break
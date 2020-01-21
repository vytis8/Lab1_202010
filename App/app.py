import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst):
    input_file = csv.DictReader(open(file))
    for row in input_file:  
        lst.append(row)

def printMenu():
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- En construccion")
    print("0- Salir")


lista = []
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if len(inputs)>0:
        if int(inputs[0])==1:
            t1_start = process_time() #tiempo inicial
            print("Cargando archivo ....")
            loadCSVFile("Data/themoviedb/AllMoviesDetailsCleaned.csv", lista)
            t1_stop = process_time() #tiempo final
            print("Datos cargados, "+str(len(lista))+" elementos cargados")
            print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        elif int(inputs[0])==2:
            print("La lista tiene "+str(len(lista))+" elementos")
        elif int(inputs[0])==3:
            print("En construcción...")
        elif int(inputs[0])==0:
            sys.exit(0)

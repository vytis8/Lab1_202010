"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    """
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=sep)
        for row in spamreader: 
            lst.append(row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Cantidad de peliculas por titulo")
    print("4- Cantidad de peliculas con calificaciones positivas (>=6) de un director")
    print("0- Salir")

def countMoviesByName(movieMame, lst):
    """
    Retorna cuantas peliculas en su titulo incluyen una palabra clave  
    """
    if len(lista)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        moviesCount=0
        for mov in lst:
            if movieMame.lower() in mov[5].lower(): #comparar con el titulo (columna 5)
                moviesCount+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return moviesCount

def countGoodMoviesByDirector(lastName, lst):
    """
    Retorna la cantidad de peliculas con calificación >= 6 para un nombre de director dado
    """
    return 0


if __name__ == "__main__":
    lista = [] #instanciar una lista vacia
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/themoviesdb/SmallMoviesDetailsCleaned.csv", lista) #llamar funcion cargar datos
                print("Datos cargados, "+str(len(lista))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0:
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                movieName =input('Ingrese parte del titulo de la pelicula\n')
                moviesCount=countMoviesByName(movieName,lista)
                print("Peliculas que contienen '", movieName ,"' en el titulo: ",moviesCount)
            elif int(inputs[0])==4: #opcion 4
                lastName =input('Ingrese el apellido del director\n')
                moviesCount=countGoodMoviesByDirector(lastName,lista)
                print("Peliculas con calificación positiva de '", lastName ,"':",moviesCount," en construcción ...")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

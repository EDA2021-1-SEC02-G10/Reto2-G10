"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.DataStructures import listiterator as it 


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Cargar información en el catalogo")
    print("3- Consultar los Top x videos con más views")
    print("4- Consultar el video que más dias ha sido trending en un país")
    print("5- Consultar el video que más dias ha sido trending en una categoria")
    print("6- Consultar los x videos con mas likes en un país específico con un tag específico")
    print("0- Salir")

catalog = None

def initCatalog():
    #inicia el catalogo de videos
    return controller.initCatalog()

def loadData(catalog):
    #carga los videos en la estructura de datos
     controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
    #lab 7
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        answer = controller.loadData(catalog)
    #req 1
    elif int(inputs[0]) == 3:
        numero=int(input("Buscando los top ?:"))
        country=input("Cuál país quiere buscar?:")  
        category=int(input("Cuál categoria quiere buscar?:"))  
        rta=controller.llamar_video_mas_views(catalog,numero,country,category)
        iterador= it.newIterator(rta)
        i=0
        while it.hasNext(iterador) and i < numero:
            i+=1
            element=it.next(iterador)
            print(("Trending date: {}, title: {}, channel title: {}, publish time: {}, views: {}, likes: {}, dislikes: {}").format(element["trending_date"],element['title'],element['channel_title'],element['publish_time'],element['views'],element['likes'],element['dislikes']))
    #req 2
    elif int(inputs[0]) == 4:
        pais=input("Cúal país quiere buscar?:")
        rta=controller.llamar_video_mas_trending(catalog,pais)
        print(rta)
        #iterador= it.newIterator(rta)
        #element=it.next(iterador)
        #print(("Title: {} , Channel_title:{} , Country: {} , Numero dias: {}").format(rta['title'], rta['channel_title'], rta['country'], rta['trending_date']))
    #req 3
    elif int(inputs[0]) == 5:
        category_name=str(input("Cúal categoria quiere buscar?:"))
        rta=controller.llamar_trending_por_categoria(catalog,category_name)
        print(rta)
        #iterador= it.newIterator(rta)
        #element=it.next(iterador)
        #print(("Title: {} ,  Channel_title: {} , Category_id: {} , Numeros de dias: {}").format(element['title'], element['channel_title'], element['category_id'], element['trending_date']))
    #req 4        
    elif int(inputs[0]) == 6:
        pais=input("Cúal país quiere buscar?:")
        tag=input("Cual tag quiere buscar (introdzcalo entre comillas por favor)?:")
        numero=int(input("Cuantos videos quiere saber?:"))
        rta=controller.video_tag(catalog, pais, tag)
        iterador= it.newIterator(rta)
        i=1
        while it.hasNext(iterador) and i <= numero:
            element=it.next(iterador)
            print(("Title: {}, Channel_title: {}, publish_time: {}, views: {}, likes: {}, dislikes: {}, tags: {}").format(element['title'],element['channel_title'],element['publish_time'],element['views'], element['likes'], element['dislikes'],element['tags']))
    else:
        sys.exit(0)
sys.exit(0)
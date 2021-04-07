"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import time
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(tipo_lista):
    """
    #Llama la funcion de inicializacion del catalogo del modelo.
    """
    lista = "ARRAY_LIST"
    if tipo_lista == 1:
        lista = "SINGLE_LINKED"
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    # TODO: modificaciones para medir el tiempo y memoria
    delta_time = -1.0
    delta_memory = -1.0

    #inicializa el proceso para medir  memoria
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadvideos(catalog)
    #Toma el tiempo y memoria al inicio del proceso
    stop_memory = getMemory()
    stop_time = getTime()

    #finaliza el proceso para medir memoria
    tracemalloc.stop()

    #calcula la difernecia de tiempo y memoria
    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory


"""
def loadData(catalog):
    
    #Carga los datos de los archivos y cargar los datos en la
    #estructura de datos
    
    #loadvideos(catalog)
    #loadcategory-id(catalog)
    #sortvideos(catalog)
"""


def loadvideos(catalog):
    
    #Carga los libros del archivo.  Por cada video se toman sus autores y por
    #cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    #referencia al libro que se esta procesando.
    
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for book in input_file:
        model.addvideo(catalog, book)




# Funciones de ordenamiento
def tipo_de_orden(numero, catalog, size):
    rta = model.tipo_de_orden_model(numero, catalog, size)
    return rta
# Funciones de consulta sobre el catálogo

def VideosByViews(video1, video2):
    return model.cmpVideosByViews(video1, video2)

# requerimiento 1

def llamar_video_mas_views(catalog,numero,country,category):
    return model.llamar_views(catalog,numero,country,category)

# requerimiento 2

def llamar_video_mas_trending(catalog,pais):
    return model.llamar_trending(catalog,pais)


#req 3

def llamar_trending_por_categoria(catalog,category_name):
    return model.trending_por_categoria(catalog,category_name)

#Requerimiento 4
def video_tag(catalog, pais, tag, numero):
    return model.video_tag(catalog,pais,tag,numero)

# ======================================
# Funciones para medir tiempo y memoria
# ======================================


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {"video":None,
               "category":None,
               'title': None,
               "tags":None,}

    catalog['video'] = lt.newList('SINGLE_LINKED', compare_tags)

    catalog["category"] = mp.newMap(345000,
                                maptype='CHAINING',
                                loadfactor=6,
                                comparefunction=comparecategory)
    catalog['country'] = mp.newMap(345000,
                                maptype='CHAINING',
                                loadfactor=6,
                                comparefunction=comparecountry)
    catalog['tags'] = mp.newMap(345000,
                                maptype='CHAINING',
                                loadfactor=6,
                                comparefunction=compare_tags)
    catalog['title'] = mp.newMap(345000,
                                maptype='CHAINING',
                                loadfactor=6,
                                comparefunction=comparetitle)
    return catalog

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['video'], video)
    mp.put(catalog['category'], video['title'], video)

"""
def addvideo (catalogo, video1):
    pos = lt.isPresent(catalogo["title"],video1["title"])
    if pos:
        video1 = lt.getElement(catalogo["video"],(pos))
        video1['trending_date'] += 1
    else:
        lt.addLast(catalogo["title"],video1["title"])
        video1['trending_date'] = 1
  
    #req 2
    pais = video1["country"]
    if pais in (catalogo["country"]):
        lt.addLast(catalogo["country"][pais],video1)
    else:
        catalogo["country"][pais] = lt.newList("ARRAY_LIST",cmpfunction=None)
        lt.addLast(catalogo["country"][pais],video1)

    #req 3
    categoria = video1["category_id"]
    if categoria in (catalogo["category"]):
        lt.addLast(catalogo["category"][categoria],video1)
    else:
        catalogo["category"][categoria] = lt.newList("ARRAY_LIST",cmpfunction=None)
        lt.addLast(catalogo["category"][categoria],video1)
    
    #req 4
    tags = video1["tags"].split("|")
    for i in tags:
        if i in (catalogo["tags"]):
            if video1["country"] in catalogo["tags"]:
                lt.addLast(catalogo["tags"][i][video1["country"]],video1)
                pass
        else:
            catalogo["tags"][i]={}
            catalogo["tags"][i][video1["country"]] = lt.newList("ARRAY_LIST",cmpfunction=None)
            lt.addLast(catalogo["tags"][i][video1["country"]],video1)
    lt.addLast(catalogo["video"],video1)
"""
# Funciones para creacion de datos
def newtitle (title):
    title = {'title': "", "books": None,  "average_rating": 0}
    title['title'] = title
    title['books'] = lt.newList('ARRAY_LIST')
    return title


# Funciones de consulta
def cmpVideosByViews(video1, video2):

    rta = True
    if int(video1["views"]) > int(video1["views"]):
        rta = False
    return rta



#Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
#Args:
#video1: informacion del primer video que incluye su valor 'views'
#video2: informacion del segundo video que incluye su valor 'views'

# Funciones utilizadas para comparar elementos dentro de una lista

#lab 7

def compare_tags(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def comparetitle(keyname, title):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(title)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def comparecountry(keyname, country):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(country)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
def comparecategory(keyname, category):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(category)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
"""
def comparetittle (titulo1, titulo2):
    if (titulo1['title'] == titulo2['title']):
        return 0
    return -1

def comparecannel_tittle (cannel, cannel2):
    if (cannel['channel']== cannel2['channel']):
        return 0
    return -1

def comparepublish_time (time1, time2):
    if (time1['publish_time'] > time2['publish_time']):
        return 1
    elif (time1['publish_time'] < time2['publish_time']):
        return -1
    return 0

def compareviews (vistas1, vistas2):
    if (vistas1['views'] > vistas2['views']):
        return 1
    elif (vistas1['views'] < vistas2['views']):
        return -1
    return 0
def comparedislikes( dislikes1, dislikes2):
    if (dislikes1['dislikes'] > dislikes2['dislikes']):
        return 1
    elif (dislikes1['dislikes'] < dislikes1['dislikes']):
        return -1
    return 0
def comparecountry(country1,country2):
    if (country1['country']== country2['country']):
        return 0
    return -14

def comparethings(video1, video2):
    return(float(video1["views"])>float(video2["views"]))

def comparelikes(video1, video2):
    return(int(video1["likes"])>int(video2["likes"]))

def compare_trending(video1, video2):
    return(int(video1["trending_date"])>int(video2["trending_date"]))
"""
# Funciones de ordenamiento
def tipo_de_orden_model(numero, catalog, size):
    sub_list = lt.subList(catalog['video'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if numero == 2:
        sorted_list = sa.sort(sub_list, compareviews)
    elif numero == 1:
        sorted_list = isort.sort(sub_list, compareviews)
    elif numero == 3:
        sorted_list = ssort.sort(sub_list, compareviews)
    elif numero == 4:
        sorted_list = quick.sort(sub_list, compareviews)
    else:
        sorted_list = merge.sort(sub_list, compareviews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

#requerimiento 1
def llamar_views(catalog,numero,country,category):
    rta= sa.sort(catalog["video"],comparethings)
    best_video = lt.newList() 
    iterador = it.newIterator(rta)
    i=1
    while it.hasNext(iterador) and i <= numero:
        element=it.next(iterador)
        if country == element['country'] and category == int(element['category_id']):
            lt.addLast(best_video, element)
            i+=1
    return best_video
#requerimiento 2
def llamar_trending(catalog,pais):
    if (pais in catalog["country"]):
        ordenado = merge.sort(catalog["country"][pais],compare_trending)
        return ordenado
#req 3
def trending_por_categoria(catalog, category_name):
    if (category_name in catalog["category"]):
        ordered = merge.sort(catalog["category"][category_name],compare_trending)
        return ordered

#Requerimiento 4
def video_tag(catalog,pais,tag,numero):
    if tag in catalog["tags"]:
        if pais in catalog["tags"][tag]:
            ordenado=merge.sort(catalog["tags"][tag][pais],comparelikes)
            return ordenado
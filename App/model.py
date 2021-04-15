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
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.DataStructures import listiterator as it 
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

    catalog['video'] = lt.newList('SINGLE_LINKED', cmpfunction= None)

    catalog["titulos"] = lt.newList('SINGLE_LINKED', cmpfunction= None)

    catalog["category"] = mp.newMap(345000, #345000
                                maptype='PROBING',
                                loadfactor=0.8,
                                comparefunction=comparecategory)
    catalog['country'] = mp.newMap(345000, #345000
                                maptype='PROBING',
                                loadfactor=0.8,
                                comparefunction=comparecountry)
    catalog['tags'] = mp.newMap(345000, #345000
                                maptype='PROBING',
                                loadfactor=0.8,
                                comparefunction=comparecountry)
    catalog['title'] = mp.newMap(500000, #345000
                                maptype='PROBING',
                                loadfactor=0.8,
                                comparefunction=comparetitle)
    return catalog

# ==============================
# Funciones para crear datos
# ==============================

#req 1
def addvideocountry(catalog,video):
    categoria = int(video["category_id"])
    booleano = mp.contains(catalog["country"],video["country"])
    if booleano:
        getpais = mp.get(catalog["country"], video["country"])
        dic = me.getValue(getpais)
        if categoria in dic:
            lt.addLast(dic[categoria],video)
        else:
            dic[categoria]=lt.newList()
            lt.addLast(dic[categoria],video)
    else:
        mp.put(catalog["country"], video['country'], {})
        getpais = mp.get(catalog["country"], video["country"])
        dic = me.getValue(getpais)
        dic[categoria]=lt.newList()
        lt.addLast(dic[categoria],video)

def getvideocountry(catalog, numero, country, category):
    getpais = mp.get(catalog["country"], country)
    dic = me.getValue(getpais)
    getcategoria = dic[category]
    rta = merge.sort(getcategoria, comparethings)
    return rta

#req 2

def modificar_lista(catalog,video):

    pos = lt.isPresent(catalog["titulos"],video["title"])
    if pos:
        video1 = lt.getElement(catalog["video"],pos)
        video1['trending_date'] += 1
        
    else:
        video['trending_date'] = 1
        lt.addLast(catalog["video"],video)
        lt.addLast(catalog["titulos"],video["title"])

def addternding(catalog,video1):
    
    booleano = mp.contains(catalog["title"],video1["country"])
    if booleano:
        getpais = mp.get(catalog["title"], video1["country"])
        dic = me.getValue(getpais)
        video = dic["trending"]
        if int(video1["trending_date"]) > int(video["trending_date"]):
            video["trending"] = video1
            
    else:
        mp.put(catalog["title"], video1['country'], { "trending" : None})
        getpais = mp.get(catalog["title"], video1["country"])
        dic = me.getValue(getpais)
        dic["trending"] = video1

def mapcountry(catalog):
    lista = catalog["video"]
    iterador=it.newIterator(lista)
    while it.hasNext(iterador):
        video1 = it.next(iterador)
        addternding(catalog,video1)

def getvideotrending(catalog,pais):
    getpais = mp.get(catalog["title"], pais)
    dic = me.getValue(getpais)
    rta = dic["trending"]
    return rta

# req 3
def addternding(catalog,video1):
    
    booleano = mp.contains(catalog["category"],video1["category_id"])
    if booleano:
        getpais = mp.get(catalog["category"], video1["category_id"])
        dic = me.getValue(getpais)
        video = dic["trending"]
        if int(video1["trending_date"]) > int(video["trending_date"]):
            video["trending"] = video1
            
    else:
        mp.put(catalog["category"], video1['category_id'], { "trending" : None})
        getpais = mp.get(catalog["category"], video1["category_id"])
        dic = me.getValue(getpais)
        dic["trending"] = video1

def getvideocategory(catalog,pais):
    getpais = mp.get(catalog["category"], pais)
    dic = me.getValue(getpais)
    rta = dic["trending"]
    return rta
    
#req 4
def addvideotag(catalog,video):
    tags = video["tags"].split("|")
    booleano = mp.contains(catalog["tags"],video["country"])
    if booleano:
        getpais = mp.get(catalog["tags"], video["country"])
        dic = me.getValue(getpais)
        for i in tags:
            if i in (dic):
                lt.addLast(dic[i],video)
            else:
                dic[i]=lt.newList()
                lt.addLast(dic[i],video)
    else:
        mp.put(catalog["tags"], video['country'], {})
        getpais = mp.get(catalog["tags"], video["country"])
        dic = me.getValue(getpais)
        for i in tags:
            dic[i]=lt.newList()
            lt.addLast(dic[i],video)

def getvideotag(catalog, country, tag):
    getpais = mp.get(catalog["tags"], country)
    dic = me.getValue(getpais)
    getcategoria = dic[tag]
    rta = merge.sort(getcategoria, comparethings)
    return rta

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

#lab 7
def compareid(id, entry):
    identry = me.getKey(entry)
    if ((id) == int(identry)):
        return 0
    elif ((id) > int(identry)):
        return 1
    else:
        return -1
def compare_tags(tag, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(tag) == int(identry)):
        return 0
    elif (int(tag) > int(identry)):
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

def comparethings(video1, video2):
    return(float(video1["views"])>float(video2["views"]))

def compare_trending(video1, video2):
    return(int(video1["trending_date"])>int(video2["trending_date"]))

def comparetittle (titulo1, titulo2):
    if (titulo1['title'] == titulo2['title']):
        return 0
    return -1
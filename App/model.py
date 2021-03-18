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

    catalog['video'] = lt.newList(tipolista,
                                  cmpfunction=comparetittle)
    catalog['category'] = {}
    catalog['country'] = {}
    catalog['tags'] = {}
    catalog['title'] = lt.newList(tipolista,
                                  cmpfunction=None)

    return catalog

# Funciones para agregar informacion al catalogo
def addvideo (catalogo, video1):
    pos = lt.isPresent(catalogo["title"],video1["title"])
    if pos:
        video1 = lt.getElement(catalogo["video"],(pos))
        video1['trending_date'] += 1
    else:
        lt.addLast(catalogo["title"],video1["title"])
        mp.put(catalog["title"], video1["title"], video1)

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
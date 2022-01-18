"""
Objetivo 👈
Para resolver este challenge, deberás crear un proyecto que consuma datos desde
3 fuentes distintas para popular una base de datos SQL con información cultural
sobre bibliotecas, museos y salas de cines argentinos.

Requerimientos funcionales 🔎
Tu proyecto deberá cumplir con una serie de requerimientos funcionales que giran
en torno a cuatro ejes centrales: los archivos fuente, el procesamiento de datos, la
creación de tablas en la base de datos y la actualización de la base de datos.
Veamos cada uno de ellos en detalle.
"""

"""
Obtener los 3 archivos de fuente utilizando la librería requests y
almacenarse en forma local (Ten en cuenta que las urls pueden cambiar en
un futuro):
o Datos Argentina - Museos
o Datos Argentina - Salas de Cine
o Datos Argentina - Bibliotecas Populares
"""

"""
Organizar los archivos en rutas siguiendo la siguiente estructura:
“categoría\año-mes\categoria-dia-mes-año.csv”
○ Por ejemplo: “museos\2021-noviembre\museos-03-11-2021”
○ Si el archivo existe debe reemplazarse. La fecha de la nomenclatura
es la fecha de descarga.
"""
import requests

import datetime
import csv
import os
import copy

def get_data_to_csv(category, url, print_data=False):
    """
    get data from URL, add category to 'categoria' key
    and save to csv in local directory: ./category/YYYY-MM/category-DD-MM-YYYY.csv
    datetime for save csv: now()
    save all keys in columns
    """
    data = requests.get(url).json()
    for item in data['result']['records']:
        item['categoria'] = category
        if print_data:
            for key, value in item.items():
                print(key, ':', value)
            print('\n')

    now = datetime.datetime.now()

    # create directory if not exists
    if not os.path.exists(category+'/'+str(now.year)+'-'+str(now.month)):
        os.makedirs(category+'/'+str(now.year)+'-'+str(now.month))
        writeMode = 'a'
    else:
        writeMode = 'w'


    with open(category+'/'+str(now.year)+'-'+str(now.month)+'/'+category+'-'+str(now.day)+'-'
            +str(now.month)+'-'+str(now.year)+'.csv', writeMode, encoding='utf-8') as csvfile:
        columns = list(data['result']['records'][0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for item in data['result']['records']:
            writer.writerow(item)

   
   
# museos: https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d
get_data_to_csv('museos', 
    'https://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d')

# salas_cine: https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae
get_data_to_csv("salas_cine", 
'https://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae')

# bibliotecas: https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7
get_data_to_csv('bibliotecas','https://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7')


"""
pip install SQLAlchemy
pip install psycopg2
"""

"""
# SQLAlchemy for connecting to a postgreSQL database
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')

# sin usar SQLAlchemy
import psycopg2
conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
conn = psycopg2.connect(conn_string)
"""

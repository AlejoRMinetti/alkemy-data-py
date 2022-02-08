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
from calendar import month
import logging

import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd


def create_table(df, category, engine, show_query=False):
    """
    create table in database
    """
    logging.basicConfig(filename='Data.log', level=logging.DEBUG)
    logging.info('Creating table: '+category+'_'+str(df.iloc[0]['categoria']))
    df.to_sql(category, engine, if_exists='replace', index=False)

    if show_query:
        print(df.head())
        print(category+' table created, show query of 3 rows:')
        for query in engine.execute('SELECT * FROM '+category+' LIMIT 3'):
            print(query)
        print('\n')


if __name__ == '__main__':
    ## save data from url to csv:
    
    ## TODO: clean dataframe, create multiple df for each entity, create tables in database
    # remove empty columns
    df_museos.dropna(axis=1, how='all', inplace=True)
    df_salas_cine.dropna(axis=1, how='all', inplace=True)
    df_bibliotecas.dropna(axis=1, how='all', inplace=True)
    # remove 'Categoría' column if exists
    if 'Categoría' in df_museos.columns:
        df_museos.drop('Categoría', axis=1, inplace=True)
    if 'Categoría' in df_salas_cine.columns:
        df_salas_cine.drop('Categoría', axis=1, inplace=True)
    if 'Categoría' in df_bibliotecas.columns:
        df_bibliotecas.drop('Categoría', axis=1, inplace=True)



    # show info
    print('\n')
    print('Info of museos dataframe:')
    print(df_museos.info())
    print('\n')
    print('Info of salas_cine dataframe:')
    print(df_salas_cine.info())
    print('\n')
    print('Info of bibliotecas dataframe:')
    print(df_bibliotecas.info())
    print('\n')

    # connect to postgreSQL database using sqlalchemy
    engine = create_engine('postgresql+psycopg2://postgres:arm13@localhost:5433/prueba')
    
    # create tables on postgreSQL database from df_museos, df_salas_cine and df_bibliotecas
    create_table(df_museos, 'museos', engine, show_query=True)
    create_table(df_salas_cine, 'salas_cine', engine, show_query=True)
    create_table(df_bibliotecas, 'bibliotecas', engine, show_query=True)
    """ 
  
 """
from calendar import month
import requests
import logging

import datetime
import csv
import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd


def save_data_to_csv(category, url, print_data=False):
    """
    get data from URL, add category to 'categoria' key
    and save to csv in local directory: ./category/YYYY-MM/category-DD-MM-YYYY.csv
    datetime for save csv: now()
    save all keys in columns
    """
    # save loging info in file
    logging.basicConfig(filename='Data.log', level=logging.DEBUG)
    logging.info('Getting data from: '+url)

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
        logging.info('Creating directory: '+category+'/'+str(now.year)+'-'+str(now.month))
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
    logging.info('Data saved in: '+category+'/'+str(now.year)+'-'+str(now.month)+'/'+category+'-'+str(now.day)+'-'
            +str(now.month)+'-'+str(now.year)+'.csv')

def csv_to_dataframe(category, day, month, year, show_head=False, show_info=False, convert_dataType=True):
    """
    read csv from local directory: ./category/YYYY-MM/category-DD-MM-YYYY.csv
    and return pandas dataframe
    """
    logging.basicConfig(filename='Data.log', level=logging.DEBUG)
    logging.info('Reading csv file: '+category+'/'+str(year)+'-'+str(month)+'/'+category+'-'+str(day)+'-'
            +str(month)+'-'+str(year)+'.csv')

    df = pd.read_csv(category+'/'+str(year)+'-'+str(month)+'/'+category+'-'+str(day)+'-'
            +str(month)+'-'+str(year)+'.csv')

    if show_head:
        print('First data of: '+category+'-'+str(day)+'-'+str(month)+'-'+str(year)+'.csv'+'\n')
        print(df.head())
        print('\n')

    if show_info:
        print('Columns of: '+category+'-'+str(day)+'-'+str(month)+'-'+str(year)+'.csv'+'\n')
        print(df.info())
        print('\n')

    return df


if __name__ == '__main__':
    ## save data from url to csv:

    # museos: https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d
    save_data_to_csv('museos', 
        'https://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d')

    # salas_cine: https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae
    save_data_to_csv("salas_cine", 
    'https://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae')

    # bibliotecas: https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7
    save_data_to_csv('bibliotecas','https://datos.gob.ar/api/3/action/datastore_search?resource_id=cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7')
      
    ## read csv to dataframe:
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    df_museos = csv_to_dataframe('museos', day, month, year, show_head=True, show_info=True)
    df_salas_cine = csv_to_dataframe('salas_cine', day, month, year, show_head=True, show_info=True)
    df_bibliotecas = csv_to_dataframe('bibliotecas', day, month, year, show_head=True, show_info=True)


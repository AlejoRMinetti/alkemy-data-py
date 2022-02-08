
import logging
import pandas as pd

def log(msg, print=False):
    logging.info(msg)
    if print:
        print(msg)

def initial_data_prep(df, dropColumnAllNaN=True ,convert_dataType=True, printLoggin=False):
    logging.basicConfig(filename='Data.log', level=logging.DEBUG)
    log('initial preparation for '+df['categoria'][0], print=printLoggin)

    if printLoggin:
        df.info()

    if dropColumnAllNaN:
        df = df.dropna(how='all', axis=1, inplace=True)
        log("Data type convertion", print=printLoggin)

    if convert_dataType:
        df = df.convert_dtypes()
        log("Data type convertion", print=printLoggin)
    
    if printLoggin:
        df.info()

    return df


if __name__ == '__main__':
    pass
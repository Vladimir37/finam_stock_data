from pandas import read_csv, set_option
import requests
import datetime
import csv

def get_data(start_date, end_date, period, symbol_id, symbol_code):
    url_addr = 'http://195.128.78.52/table.csv?'
    url = "http://195.128.78.52/table.csv?market=5&em=86&code=GBPUSD&df=1&mf=11&yf=2014&from=01.12.2014&dt=6&mt=11&yt=2014&to=06.12.2014&p=2&f=GBPUSD_141201_141206&e=.csv&cn=GBPUSD&dtf=1&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=3&sep2=1&datf=5&at=1"

    data = read_csv(url, header=0, index_col=0, parse_dates={'Date&Time': [0, 1]}, sep=';').sort_index()
    data.columns = ['' + i for i in ['Open', 'High', 'Low', 'Close', 'Volume']]

    set_option('display.max_columns', 50)
    set_option('display.width', 500)

    print(data.get_values()[2][2])
    # print(data)


get_data(1,1,1,1,1)
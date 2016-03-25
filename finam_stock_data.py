import urllib
import sqlite3
from datetime import datetime
from pandas import read_csv, set_option

def get_data(start_date, end_date, period, symbol_code):
    url_addr = 'http://195.128.78.52/table.csv?'
    url = "http://195.128.78.52/table.csv?market=5&em=86&code=GBPUSD&df=1&mf=11&yf=2014&from=01.12.2014&dt=6&mt=11&yt=2014&to=06.12.2014&p=2&e=.csv&cn=GBPUSD&dtf=1&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=3&sep2=1&datf=5&at=1"
    periods = {
        'tick': 1,
        'min': 2,
        '5min': 3,
        '10min': 4,
        '15min': 5,
        '30min': 6,
        'hour': 7,
        'daily': 8,
        'week': 9,
        'month': 10
    }

    # symbol data from database
    connect = sqlite3.connect('symbols.sqlite')
    cursor = connect.cursor()
    target_code = (symbol_code,)
    cursor.execute('SELECT * FROM bases WHERE EmitentCode=?', target_code)
    print(cursor.fetchone())

    # creating request
    # params = urllib.parse.urlencode([('market', 5), ])
    #
    # data = read_csv(url, header=0, index_col=0, parse_dates={'Date&Time': [0, 1]}, sep=';').sort_index()
    # data.columns = ['' + i for i in ['Open', 'High', 'Low', 'Close', 'Volume']]
    #
    # set_option('display.max_columns', 50)
    # set_option('display.width', 500)
    #
    # # table = data.head(5).to_dict()['Open'][pandas.to_datetime('2014-12-01 00:01:00')]
    # table = data.head(5)
    # print(table.to_json())


get_data(1,1,1,'YHOO')
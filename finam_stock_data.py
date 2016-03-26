import urllib
import sqlite3
from datetime import datetime
from pandas import read_csv, set_option

def get_data(start_date, end_date, period, symbol_code):
    # converting date
    start_date = datetime.fromtimestamp(start_date)
    end_date = datetime.fromtimestamp(end_date)
    start_date_str = start_date.strftime('%d.%m.%Y')
    end_date_str = end_date.strftime('%d.%m.%Y')

    # converting period
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
    period = periods[period]

    url_addr = 'http://195.128.78.52/table.csv?'

    # symbol data from database
    connect = sqlite3.connect('symbols.sqlite')
    cursor = connect.cursor()
    target_code = (symbol_code,)
    cursor.execute('SELECT * FROM bases WHERE EmitentCode=?', target_code)
    search_result = cursor.fetchone()
    if not search_result:
        print('Not found')
        return False

    # creating request
    params = urllib.parse.urlencode([('market', 5), ('em', search_result[1]), ('code', search_result[3]),
                 ('df', start_date.day), ('mf', start_date.month - 1), ('yf', start_date.year),
                 ('from', start_date_str),
                 ('dt', end_date.day), ('mt', end_date.month - 1), ('yt', end_date.year),
                 ('to', end_date_str),
                 ('p', period), ('f', "table"), ('e', ".csv"), ('cn', search_result[1]),
                 ('dtf', 1), ('tmf', 3), ('MSOR', 1), ('mstime', "on"), ('mstimever', 1),
                 ('sep', 3), ('sep2', 1), ('datf', 5), ('at', 1)
                                     ])

    # requesting
    data = read_csv(url_addr + params, header=0, index_col=0, parse_dates={'Date&Time': [0, 1]}, sep=';').sort_index()
    data.columns = ['' + i for i in ['Open', 'High', 'Low', 'Close', 'Volume']]

    set_option('display.max_columns', 50)
    set_option('display.width', 500)

    return data.to_json()
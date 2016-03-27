# Finam_stock_data
[![PyPI version](https://badge.fury.io/py/finam_stock_data.svg)](https://badge.fury.io/py/finam_stock_data)

**Finam_stock_data** is Python 3 package for getting historical stock data from [Finam](http://www.finam.ru/). Finam_stock_data supports Stocks, Forex and Indices.

## Installing
Run in your console:
```
pip3 install finam_stock_data
```
or download `finam_stock_data.py` and `symbols.sqlite`. 

## Using
Add in your Python file:
```python
from finam_stock_data import get_data
```
Function calling:
```python
get_data(start_date, end_date, period, symbol_code):
```
Arguments:
* **start_date** - first day in UTS. Example: **1352678400**
* **end_date** - Last day in UTS. Example: **1352937600**
* **period** - period of japan candlestick. One of the following: **'tick', 'min', '5min', '10min', '15min', '30min', 'hour', 'daily', 'week', 'month'**.
* **symbol_code** - code of symbol. Examples: **'MSFT'**, **'YHOO'**, **'EURUSD'**.

Using example:
```python
get_data(1352678400, 1352937600, 'hour','MSFT')
```

Function `get_data` return JSON string. JSON has the following structure:
```json
{
  "Open": {
    "date_1": "value_1",
    "date_2": "value_2",
    "date_3": "value_3"
  },
  "High": {
    "date_1": "value_1",
    "date_2": "value_2",
    "date_3": "value_3"
  },
  "Low": {
    "date_1": "value_1",
    "date_2": "value_2",
    "date_3": "value_3"
  },
  "Close": {
    "date_1": "value_1",
    "date_2": "value_2",
    "date_3": "value_3"
  },
  "Volume": {
    "date_1": "value_1",
    "date_2": "value_2",
    "date_3": "value_3"
  }
}
```
Example response:
```json
{
  "Open":{
    "1352743200000":28.94,
    "1352746800000":28.755,
    "1352750400000":28.33,
    "1352754000000":28.285,
    "1352757600000":28.48,
    "1352761200000":28.43,
  },
  "High":{
    "1352743200000":29.0,
    "1352746800000":28.755,
    "1352750400000":28.33,
    "1352754000000":28.49,
    "1352757600000":28.53,
    "1352761200000":28.43,
  },
  "Low":{
    "1352743200000":28.6,
    "1352746800000":28.32,
    "1352750400000":28.25,
    "1352754000000":28.28,
    "1352757600000":28.41,
    "1352761200000":28.28,
  },
  "Close":{
    "1352743200000":28.76,
    "1352746800000":28.325,
    "1352750400000":28.285,
    "1352754000000":28.48,
    "1352757600000":28.43,
    "1352761200000":28.3,
  },
  "Volume":{
    "1352743200000":874079,
    "1352746800000":1615805,
    "1352750400000":1389951,
    "1352754000000":1078498,
    "1352757600000":679577,
    "1352761200000":946919,
  }
}
```

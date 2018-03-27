# -*- coding: utf-8 -*-

stocks = {}

secondary = {}


def loadStock(symbol):
    '''
    ask for a user input and then loads that csv file into stocks dictionary
    INPUT: str from keyboard
    OUTPUT: stocks dictionary, keys are stock symbols, values are dictionaries again with 
            keys: dates, values: open,high,low,close in that order
    '''
    import csv
    symbol = symbol.upper()
    with open ('/home/boti/botka/a_BOTI_a/study/sem4/python/finance/stockdata/'+symbol + ".csv",'r',encoding='utf8',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            date = line[0]                              #sets the dates as keys
            ohlc = line[1:5]                            #Open High Low Close as values
            secondary[date] = ohlc                           #pairs keys with values
        stocks[symbol]=secondary                             #to key BATS, adds the prev dict
    #print(stocks.keys())                               #prints the keys
    return

def test_loadStock():
    while True:
        n = str(input('stock symbol (quit with q) : '))
        if n == 'q':
            break
        try:
            loadStock(n)
        except FileNotFoundError:
            print("symbol doesn't exists")
    return 
        

# -*- coding: utf-8 -*-
'''
TODO: if loadPortoflio has one wrong line it loads the next if thats good
      but it should break the whole thing
      FIX THIS
TODO: 'kaki' symbol in portfolio1 doesn't raise exception. It goes to the portfolio, but not to the stocks
'''
class TransactionError(Exception):
    pass

class DateError(Exception):
    pass

stocks = {}
portfolio = {}
transactions = []

def normaliseDate(s):
    '''
    replaces a string to YYYY-MM-DD if ending is not in this format or int input -> DateError
    input: any string
    output: date in YYYY-MM-DD as string
    '''
    try:
        s = s.replace('/','-')          #replaces / and . to -
        s = s.replace('.','-')
        lst = s.split('-')
        for i in range(0,3):            #adds the leading 0 if len == 1
            if len(lst[1]) >2:          #if year is in the middle, ERROR
                raise DateError('wrong format :( ')
            if len(lst[i]) == 1:
                lst[i] = '0' + lst[i]
            if int(lst[i]) == False:    #if not numbers, ERROR
                raise DateError('wrong format :( ')
        if len(lst[0]) == 2:            #sets YYYY-MM-DD
            lst.reverse() 
        s = '-'.join(lst)  
        if len(s) != 10:                #if not proper lenght, ERROR
            raise DateError('wrong format :( ')
    except Exception:                   #if everything else, ERROR
        raise DateError('wrong format :( ')
    return s

def loadStock(symbol):
    '''
    ask for a user input and then loads that csv file into stocks dictionary
    INPUT: str from keyboard
    OUTPUT: stocks dictionary, keys are stock symbols, values are dictionaries again with 
            keys: dates, values: open,high,low,close in that order
    '''
    import csv
    secondary = {}
    symbol = symbol.upper()
    with open ('/home/boti/botka/a_BOTI_a/study/sem4/python/finance/stockdata/'+symbol + ".csv",'r',encoding='utf8',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            date = line[0]                                  #sets the dates as keys
            ohlc = line[1:5]                                #Open High Low Close as values
            secondary[date] = ohlc                          #pairs keys with values
        stocks[symbol]=secondary                            #to key BATS, adds the prev dict
    #print(stocks.keys())                                   #prints the keys
    return

def loadPortfolio(fname):
    '''
    reads a csv file and creates the portfolio dictionary. 
    INPUT: str from keyboard, if file not found -> error, if str is empty -> portfolio.csv opens
    OUTPUT: portfolio dictionary: keys: date, cash, symbols; values: date, cahs, ammount of shares realted to symbols
    '''
    portfolio.clear()       #https://www.tutorialspoint.com/python/dictionary_clear.htm
    import csv
    with open ("/home/boti/botka/a_BOTI_a/study/sem4/python/finance/"+fname+".csv",'r',encoding='utf8',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        date = normaliseDate(next(csv_reader)[0])
        cash = float(next(csv_reader)[0])
        portfolio['date'] = date
        portfolio['cash'] = cash
        try:
            for line in csv_reader:
                if line == '':
                    break
                else:                   
                    symb = str(line[0])
                    line[1] = int(line[1])
                    if type(line[1]) == int:
                        quant = int(line[1])
                        
                        portfolio[symb] = quant
                        loadStock(symb.upper()) 
                    else:
                        raise ValueError()                       
        except ValueError:
            print('share must be integer :( ')
        except FileNotFoundError:
            print("symbol doesn't exists :( ")               
    return


def main():
    try:
        fname = str(input('filename: '))
        if fname == '':
            fname = 'portfolio'
        loadPortfolio(fname)
    except FileNotFoundError:
        print('no such file :( ')
    return

main()

#print(stocks)
print(stocks.keys())
print(portfolio)
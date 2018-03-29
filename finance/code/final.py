# -*- coding: utf-8 -*-
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
    TODO: if it gets a non integer the next line doesn't reads in
    INPUT: str from keyboard, if file not found -> error, if str is empty -> portfolio.csv opens
    OUTPUT: portfolio dictionary: keys: date, cash, symbols; values: date, cahs, ammount of shares realted to symbols
    '''
    portfolio.clear()       #https://www.tutorialspoint.com/python/dictionary_clear.htm
    del transactions[:]
    #portfolio and tranactions cleared out
    import csv
    with open ("/home/boti/botka/a_BOTI_a/study/sem4/python/finance/"+fname+".csv",'r',encoding='utf8',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        date = normaliseDate(next(csv_reader)[0])
        cash = float(next(csv_reader)[0])
        portfolio['date'] = date                #reads the date
        portfolio['cash'] = cash                #reads the cash ammount
        try:
            for line in csv_reader:             #rads until empty line
                if line == '':
                    break
                else:                   
                    symb = str(line[0])         #name of the stock
                    line[1] = int(line[1])      #quantity of given stock as integer
                    if type(line[1]) == int:    #only accepts integers
                        quant = int(line[1])
                        '''if symbol does not have a .CSV file then it does not gets add to the portfolio
                           https://stackoverflow.com/questions/34000914/how-to-create-a-list-from-filenames-in-a-user-specified-directory-in-python
                        '''
                        import os
                        list1 = os.listdir("/home/boti/botka/a_BOTI_a/study/sem4/python/finance/stockdata")
                        if symb.upper()+'.csv' in list1:                        
                            portfolio[symb] = quant
                            loadStock(symb.upper())                         
                    #else:
                        #raise ValueError()      #not integer -> error                  
        except ValueError:
            print('share must be integer :( ')
        except FileNotFoundError:
            print("symbol doesn't exists :( ")               
    return

def valuatePortfolio(date=None, verbose=False):
    '''
    Valuates the portfolio at given date. No date -> date in portfolio
    '''
    '''
    TODO: write more efficient code
          raise exceptions using notes
          raise another exception if date in the wrong format
    ''' 
    #creating new dict with only the symbols for iteration
    port_symb = {x:portfolio[x] for x in portfolio if x!='date'}
    port_symb = {x:port_symb[x] for x in port_symb if x!='cash'}

    #now port_symb only contains owned stock symbols
    
    if date == None:                                    #converting into proper date format
        date = normaliseDate(portfolio['date'])
    else:
        date = normaliseDate(date)
        
    '''if date is earlier than date in portfolio: Error'''
    from datetime import datetime
    date = [int(x) for x in date.split('-')]            #converting dates into datetime format
    date_p = portfolio['date']
    date_p = [int(x) for x in date_p.split('-')]
    if datetime(date[0],date[1],date[2]) < datetime(date_p[0],date_p[1],date_p[2]):
        raise DateError
    else:                                   #converting back to noramliseDate() form
        date = [str(x) for x in date]
        date = normaliseDate("-".join(date))
        
    '''calculatin the profit'''
    value = 0
    cash = portfolio['cash']
    for keys in port_symb:
        #if the date is not a trading day -> Error
        if date not in stocks[keys].keys():
            print('here')
            raise DateError
        value = value + int(port_symb[keys]) * float((stocks[keys][date])[2])
    value = value + cash
    
    if verbose == False:
        print(value)
    else:
        print(' Your portfolio on {} \n [* share values based on the lowest pice on {}] \n'.format(date,date))
        print(" {0:<21} | {1:^8} | {2:^8} | {3:^10} |".format("Capital type", "Volume", "Val/Unit*","Value in £"))
        print( "-" * 23 + "+" + "-" * 10 + "+" + "-" * 11 + "+" + "-" * 13)
        if portfolio['cash'] != 0:
            print(" {0:<21} | {1:8} | {2:9.2f} | {3:10.2f} |".format('Cash',1,portfolio['cash'],portfolio['cash']))
        for p_symb, p_vol in port_symb.items():
            for s_key in stocks.keys():
                if s_key == p_symb:
                    print(" {0:<21} | {1:8} |{2:10.2f} | {3:10.2f} |".format(p_symb,p_vol,float((stocks[s_key][date])[2]),int(port_symb[p_symb]) * float((stocks[s_key][date])[2])))
                else:
                    continue
        print( "-" * 23 + "+" + "-" * 10 + "+" + "-" * 11 + "+" + "-" * 13)
        print(" {0:<21} {1:25} {2:10.2f} ".format('TOTAL VALUE',' ',value))
       
    return


def test_loadPortfolio():
    try:
        fname = str(input('filename: '))
        if fname == '':
            fname = 'portfolio'
        loadPortfolio(fname)
    except FileNotFoundError:
        print('no such file :( ')
    return

def main():
    test_loadPortfolio()
    #valuatePortfolio()
    valuatePortfolio(date='2012-01-03', verbose=True)
    
    return

main()

#print(stocks)
print(stocks.keys())
print(portfolio)

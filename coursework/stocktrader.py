# -*- coding: utf-8 -*-
"""
stocktrader -- A Python module for virtual stock trading
MATH20622 Programming with Python, The University of Manchester
          This module trades with stocks from a library with historical stock data 
          It uses a simple 'buy and sell as much as possible' strategy based on daily low and high prices
    
Full name: Botond Maros
StudentId: 9770387
Email: botond.maros@student.manchester.ac.uk
"""

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
    
    INPUT: any string
    
    OUTPUT: date in YYYY-MM-DD as string
    '''
    try:
        s = s.replace('/','-')          #replaces / and . to -
        s = s.replace('.','-')
        lst = s.split('-')
        for i in range(0,3):            #adds the leading 0 if len == 1
            if len(lst[1]) >2:          #if year is in the middle, ERROR
                raise DateError
            if len(lst[i]) == 1:
                lst[i] = '0' + lst[i]
            if int(lst[i]) == False:    #if not numbers, ERROR
                raise DateError
        if len(lst[0]) == 2:            #sets YYYY-MM-DD
            lst.reverse() 
        s = '-'.join(lst)  
        if len(s) != 10:                #if not proper lenght, ERROR
            raise DateError
    except Exception:                   #if everything else, ERROR
        raise DateError
    return s

def loadStock(symbol):
    '''
    loads 'SYMBOL'.csv file into stocks dictionary from current_dictionary/stockdata
    
    INPUT: str from function input
    
    OUTPUT: stocks dictionary, keys are stock symbols, values are dictionaries again with 
            keys: dates, values: open,high,low,close in that order
    '''
    import csv
    secondary = {}
    symbol = symbol.upper()
    with open ('stockdata/'+symbol + ".csv",'r',encoding='utf8',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            date = normaliseDate(line[0])                   #sets the dates as keys
            ohlc = line[1:5]                                #Open High Low Close as values
            secondary[date] = ohlc                          #pairs keys with values
        stocks[symbol]=secondary                            #to key BATS, adds the prev dict
    return

def loadPortfolio(fname=None):
    '''
    reads a csv file and creates the portfolio dictionary, updates the stocks dictionary with that symbol
    Acceptable file format: date in 1st row 1st column, cash in 2nd row 1st column, 
        owned stocks in next rows with name 1st column, volume in the 2nd
        
    ERRORS: date is in the wrong format -> DateError
            symbol not in the files -> FileNotFoundError
            volume is not integer -> ValueError
            
    INPUT: str from keyboard, if file not found -> error, if str is empty -> portfolio.csv opens
    
    OUTPUT: portfolio dictionary: keys: date, cash, symbols; values: date, cahs, ammount of shares realted to symbols
    '''
    portfolio.clear()       #https://www.tutorialspoint.com/python/dictionary_clear.htm
    del transactions[:]
    if fname == None:
            fname = 'portfolio.csv'
    #portfolio and tranactions cleared out
    import csv
    with open (fname,'r',encoding='utf8',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        date = normaliseDate(next(csv_reader)[0])
        cash = float(next(csv_reader)[0])
        portfolio['date'] = date                #reads the date
        portfolio['cash'] = cash                #reads the cash ammount
        for line in csv_reader:             #reads until empty line
            if line == '':
                break
            else:                   
                symb = str(line[0])         #name of the stock
                import os
                cwd = os.getcwd()
                list1 = os.listdir(cwd+"/stockdata")
                if symb.upper()+'.csv' not in list1:
                    raise FileNotFoundError
                else:
                    try:
                        line[1] = int(line[1])
                    except ValueError:
                        raise ValueError
                    if type(line[1]) == int:    #only accepts integers
                        quant = int(line[1])
                        #if symbol does not have a .CSV file then it does not gets add to the portfolio
                        portfolio[symb] = quant
                        loadStock(symb.upper())
                    
    return

def valuatePortfolio(date=None, verbose=False):
    '''
    Valuates the portfolio at given date. If no date provided it uses the date from portfolio
    If verbose is true it prints out a descriptive table correspondong to the owned assets and its values
    
    INPUT: date, verbose
    
    OUTPUT: value of the portfolio
    '''
    #creating new dict with only the symbols for iteration
    port_symb = {x:portfolio[x] for x in portfolio if x!='date'}
    port_symb = {x:port_symb[x] for x in port_symb if x!='cash'}
    #now port_symb only contains owned stock symbols
    if date == None:                                    #converting into proper date format
        date = normaliseDate(portfolio['date'])
    else:
        date = normaliseDate(date)           
    #if date is earlier than date in portfolio: Error
    from datetime import datetime
    date_f = [int(x) for x in date.split('-')]            #converting dates into datetime format
    date_p = portfolio['date']
    date_p = [int(x) for x in date_p.split('-')]
    if datetime(date_f[0],date_f[1],date_f[2]) < datetime(date_p[0],date_p[1],date_p[2]):
        raise DateError
    #calculatin the profit
    value = 0
    cash = portfolio['cash']
    for keys in port_symb:
        #if the date is not a trading day -> Error
        if date not in stocks[keys].keys():
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
        print(" {0:<21} {1:25} {2:10.2f} \n".format('TOTAL VALUE',' ',value))
    return value

def addTransaction(trans, verbose=False):
    '''
    addTransactions appends the trans dictionary to the transactions list
    if we sell every stock from our portfolio, that stocks gets deleted out of the portfolio
    the funtion trades at the given date with the given symbol and value from the trans dictionary
    it sells at high price and buys at low
    
    INPUT: trans - dictionary contaning date, symbol and value(can be negative, corresponding to a sell)
           verbose - if true, prints out a descriptive message about the transaction
    
    ERRORS: if we want to share a not owned stock, or more than we have -> TransactionError
            if we want to buy more share than we can afford -> TransactionError
            if date is not accepted by the normaliseDate -> DateError
    '''
    date = normaliseDate(trans['date'])
    symbol = trans['symbol']
    #if stockname not in stocks -> error
    if symbol not in stocks.keys():
        raise ValueError
    #if trans date < portfolio date: error as we cant go back to the past
    from datetime import datetime
    date_t = [int(x) for x in date.split('-')]
    date_p = portfolio['date']
    date_p = [int(x) for x in date_p.split('-')]
    if datetime(date_t[0],date_t[1],date_t[2]) < datetime(date_p[0],date_p[1],date_p[2]):
        raise DateError
    portfolio['date'] = date        #setting new date for the portfolio
    transactions.append(trans)
    #adding if there is a new symbol and postive
    if symbol not in portfolio.keys() and trans['volume']>0:
        portfolio[symbol] = trans['volume']
    elif symbol not in portfolio.keys() and trans['volume']<=0:
        raise TransactionError
    elif symbol in portfolio.keys() and trans['volume']>0:
        portfolio[symbol] += trans['volume']
    elif symbol in portfolio.keys() and trans['volume']<0:
        portfolio[symbol] -= abs(trans['volume'])
        #if we sell more than we have, ERROR
        if portfolio[symbol] < 0:
            raise TransactionError
    #CASH
    if trans['volume'] > 0:
        if float(stocks[symbol][date][1]) * trans['volume'] > portfolio['cash']:        #want to buy more than can afford -> error
            raise TransactionError
        else:
            portfolio['cash'] -= float(stocks[symbol][date][1]) * trans['volume']       #buying a share decreases the cash
    elif trans['volume'] < 0:
        portfolio['cash'] += float(stocks[symbol][date][2]) * abs(trans['volume'])      ##selling share increases cash
    #SHARES   
    if portfolio[symbol] == 0:
        del portfolio[symbol]
    #PRINTING
    if verbose == True:
        if trans['volume'] > 0:
            print('\n> {}: {} {} shares of {} for a total of £{:.2f} \n  Aviable cash: {:.2f} \n' \
                  .format(normaliseDate(trans['date']), 'Bought',int(trans['volume']),trans['symbol'],float(stocks[symbol][date][1]) * trans['volume'],portfolio['cash']))
        else:
            print('\n> {}: {} {} shares of {} for a total of £{:.2f} \n  Aviable cash: {:.2f} \n' \
                  .format(normaliseDate(trans['date']), 'Sold',abs(int(trans['volume'])),trans['symbol'],float(stocks[symbol][date][2]) * abs(trans['volume']),portfolio['cash']))
    return

def savePortfolio(fname=None):
    '''
    writes out the portfolio to a csv file with name filename fname
    it writes the file in a format that loadPortfolio can handle
    if fname is not provedid it saves the portfolio as portfolio.csv
    
    OUTPUT: fname.csv file
    '''
    if fname == None:           
        fname = 'portfolio.csv'
    portfolio2 = [[key,value] for key, value in portfolio.items()]
    del portfolio2[0][0]        #deleting 'date'
    del portfolio2[1][0]        #deleting 'cash'
    import csv
    with open (fname ,'w',encoding='utf8') as csv_file:
        writer = csv.writer(csv_file)
        for line in portfolio2:
            writer.writerow(line)    
    return

def sellAll(date=None,verbose=False):
    '''
    sells all the shares at a given date 
    If verbose=True all selling transactions are printed to the command line
    If date is not provided, the date of the portfolio is assume for the sell out
    
    INPUT: date, verbose (both optional)
    
    OUTPUT: depends on the verbose
    '''
    if date == None:            #normalising the date
        date = normaliseDate(portfolio['date'])
    else:
        date = normaliseDate(date)
    #creating a dictionary with only symbols and owned stock volumes
    portfolio2= {x:portfolio[x] for x in portfolio if x!='date'}
    portfolio2 = {x:portfolio2[x] for x in portfolio2 if x!='cash'}
    for keys, values in portfolio2.items():        #actually selling the shares
        addTransaction({'date':date,'symbol':keys, 'volume':-int(values)},verbose)
    return

def loadAllStocks():
    '''
    loads all stock from the stockdata folder to the stocks dictionary
    No INPUT, no OUTPUT
    '''
    import os
    cwd = os.getcwd()
    list1 = os.listdir(cwd+"/stockdata")
    list1 = [x.replace('.csv','') for x in list1]
    for i in list1:
        try:
            loadStock(i)
        except Exception:
            pass
    return

def tradeStrategy1(verbose=False):
    '''
    goes through all the days in the stocks dictionary and buys or sells stocks based on certain criteria
    BUY CRITERIA: goes through every stock and calculates which growth the biggest in the last 10 days by:
                  10*buying date's price/last 10 days average price
    if it decides which share to buy(only one) it buys all the affordable stocks
    after a buy it can only sell, based on another criteria
    SELL CRITERIA: after the buying date it will sell if the low price of the selling date/ high price of the buying date is
                   either less than 0.7 or more than 1.3
    it uses the function addTransaction for every buy and sell
    
    INPUT: it passivly uses all the loaded stocks, transactions list, portfolio
           actively uses verbose by passing it through the addTransaction(trans,verbose) function
           the addTransaction function's trans input is created while running, using the criteria
    
    OUTPUT: addTransactions output, based on the verbose
    '''
    for symbol in stocks:
        datelist = list(stocks[symbol].keys())
        break
    from datetime import datetime
    date_10 = [int(x) for x in datelist[9].split('-')]            #converting dates into datetime format
    date_p = portfolio['date']
    date_p = [int(x) for x in date_p.split('-')]
    if datetime(date_10[0],date_10[1],date_10[2]) > datetime(date_p[0],date_p[1],date_p[2]):
        #in this case we use the 10th trading day
        trade_index = 9-1
        #here we take out one as in the loop we add one back
        #we have to do this as in the loop if we sell we can only buy at the next day
    else:
        #in this case we use the portfolio date
        #here we take out one as in the loop we add one back
        #we have to do this as in the loop if we sell we can only buy at the next day
        trade_index = datelist.index(portfolio['date'])-1
    iterday = trade_index + 1
    while iterday < len(datelist):
        prices = []             #stores only the prices(quotients)
        pairs = []              #stores the symbols and quotients
        '''BUY'''
        trade_index += 1
        for symb in stocks.keys():
            #this calculates the max quotient for the given date
            highest = 0
            quotient_buy = 10*float(stocks[symb][datelist[trade_index]][1])/(float(stocks[symb][datelist[trade_index-9]][1])+float(stocks[symb][datelist[trade_index-8]][1])+ \
                                float(stocks[symb][datelist[trade_index-7]][1])+float(stocks[symb][datelist[trade_index-6]][1])+float(stocks[symb][datelist[trade_index-5]][1])+ \
                                float(stocks[symb][datelist[trade_index-4]][1])+float(stocks[symb][datelist[trade_index-3]][1])+float(stocks[symb][datelist[trade_index-2]][1])+ \
                                float(stocks[symb][datelist[trade_index-1]][1])+float(stocks[symb][datelist[trade_index]][1]))
            if highest < quotient_buy:
                highest = quotient_buy      #storing the one with the highest ratio
            pairs.append([symb,highest])
            prices.append(highest)
        max_price = max(prices)             #getting the max quotients and its stock symbol
        for ii in range(0,len(pairs)):
            if pairs[ii][1]==max_price:     #gets us the best stock with its ratio
                buying_share = pairs[ii]
        #buys all the affordable shares with the biggest ratio
        #this part of the code checks that the last entry of the transaction was a sell
        #or if the transcations list is empty. we have to do this as the buying transaction is out of the for loop
        if transactions==[] or transactions[-1]['volume']<0:
            trans_buy = { 'date':datelist[trade_index], 'symbol':str(buying_share[0]), 'volume':int(portfolio['cash'])//float(stocks[buying_share[0]][datelist[trade_index]][1])}       
            addTransaction(trans_buy,verbose)
                
        '''SELL'''
        #calculate q sell for a day
        #buying_share[0] is the name of the owned stock
        for iii in range(trade_index+1,len(datelist)):
            #iii is the days when we can sell
            quotient_sell = float(stocks[buying_share[0]][datelist[iii]][2]) / float(stocks[buying_share[0]][datelist[trade_index]][1])   #low price / high price(using the day we bought our share)
            if (quotient_sell < 0.7 or quotient_sell > 1.3):
                trans_sell = { 'date':datelist[iii], 'symbol':trans_buy['symbol'], 'volume':-int(trans_buy['volume']) }
                addTransaction(trans_sell,verbose)
                iterday = datelist.index(trans_sell['date'])
                break
        trade_index = datelist.index(portfolio['date'])
        iterday += 1            #starts new loop with the next day         
    return

def main():

    return

if __name__ == '__main__' or __name__ == 'builtins':
   main()
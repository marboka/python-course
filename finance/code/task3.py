'''
WARNING: no loadStock()
BUT in the final it is working
'''

portfolio={}
srocks={}

from task1 import normaliseDate
from task2 import loadStock

def loadPortfolio(fname):
    '''
    reads a csv file and creates the portfolio dictionary. 
    TODO: if it gets a non integer the next line doesn't reads in
    INPUT: str from keyboard, if file not found -> error, if str is empty -> portfolio.csv opens
    OUTPUT: portfolio dictionary: keys: date, cash, symbols; values: date, cahs, ammount of shares realted to symbols
    '''
    portfolio.clear()       #https://www.tutorialspoint.com/python/dictionary_clear.htm
    import csv
    with open ("/home/boti/botka/a_BOTI_a/study/sem4/python/finance/"+fname+".csv",'r',encoding='utf8',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        date = normaliseDate(next(csv_reader)[0])
        cash = float(next(csv_reader)[0])
        portfolio['date'] = date                #reads the date
        portfolio['cash'] = cash                #reads the cash ammount
        try:
            for line in csv_reader:             #eads until empty line
                if line == '':
                    break
                else:                   
                    symb = str(line[0])         #name of the stock
                    line[1] = int(line[1])      #quantity of given stock as integer
                    if type(line[1]) == int:    #only accepts integers
                        quant = int(line[1])
                        '''if symbol does not have a .CSV file then 
                           it does gets add to the portfolio
                           https://stackoverflow.com/questions/34000914/how-to-create-a-list-from-filenames-in-a-user-specified-directory-in-python
                           '''
                        import os
                        list1 = os.listdir("/home/boti/botka/a_BOTI_a/study/sem4/python/finance/stockdata")
                        if symb.upper()+'.csv' in list1:                        
                            portfolio[symb] = quant
                            loadStock(symb.upper())                         
                    else:
                        raise ValueError()      #not integer -> error                  
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
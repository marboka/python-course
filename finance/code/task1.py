# -*- coding: utf-8 -*-
class DateError(Exception):
    pass

def normaliseDate(s):
    '''
    replaces a string to YYYY-MM-DD
    if ending is not in this format or int input -> DateError
    input: any string
    output: date in YYYY-MM-DD as string
    '''
    try:
        s = s.replace('/','-')          #replaces / and . to -
        s = s.replace('.','-')
        lst = s.split('-')
        for i in range(0,3):            #adds the leading 0 if len == 1
            if len(lst[1]) >2:          #if year is in the middle, ERROR
                raise DateError('wrong format')
            if len(lst[i]) == 1:
                lst[i] = '0' + lst[i]
            if int(lst[i]) == False:    #if not numbers, ERROR
                raise DateError('wrong format')
        if len(lst[0]) == 2:            #sets YYYY-MM-DD
            lst.reverse() 
        s = '-'.join(lst)  
        if len(s) != 10:                #if not proper lenght, ERROR
            raise DateError('wrong format')
    except Exception:                   #if everything else, ERROR
        raise DateError('wrong format')
    return s

def test_normaliseDate():
    dates=['1.02.2012','2',5,'asd','1.2.2012','01.02.2012', \
           '2012/01/01','2013/1/1','as.as.asdf','312.2.2', \
           'asdddddddddddd','1.2134.1','1.1.1']
    for x in dates:
        print('before formating: ',x)
        try:
            print('after formating: ',normaliseDate(x),'\n')
        except DateError as e:
            print(e,'\n')
    return

#test_normaliseDate()

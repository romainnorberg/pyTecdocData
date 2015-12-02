# -*- coding: utf-8 -*-

import pypyodbc


__datadir = r'D:\tecdoc_data\data'

def setDataDir(dir):
    __datadir = dir

def getDataDir():
    return __datadir

class Cd:
    __conection = None
    __cursor = None
    __conected = None
    __dsnstr = ''
    __tables = []


    def __init__(self, name,dsn=''):
        self.name = name
        self.__datadir = r"{0}\{1}".format(getDataDir(),self.name)
        if dsn != '':
            self.__dsnstr = "DSN={0}".format(dsn)
            self.connect()

    def __str__(self):
        returnstr = 'Name: {0}\nData directory: {1}\n'.format(self.name,self.__datadir)
        if self.__dsnstr:
            returnstr = returnstr + 'DSN: {0}\n'.format(self.__dsnstr)
        if self.__conected:
            returnstr = returnstr + 'Conected to ODBC database : {0}\n'.format(self.__conected)
            returnstr = returnstr + 'We have loaded information about {0} tables.\n'.format(len(self.__tables))
        return returnstr

    def __del__(self):
        # please do not forget de delete everything !
        pass
    
    def conected(self):
        return self.__conected

    def connect(self,dsn=''):
        if dsn!='':
            self.__dsnstr = "DSN={0}".format(dsn)
        try:
            self.__conection = pypyodbc.connect(self.__dsnstr,unicode_results=True)
            self.__conected = True
            self.__cursor = self.__conection.cursor()
        except:
            self.__conected = False
            print('found an exception when connecting to ODBC database')

    def loadTablesFromDB(self):
        self.__cursor.execute('select tname from systable where owner > 1')
        for row in self.__cursor:
            newtable = Table(row[0])
            self.__tables.append(newtable)
            del(newtable)
            


class Table:
    def __init__(self, tname, rows=0):
        self.tname = tname
        self.rows = rows

    def __str__(self):
        #return 'Numele meu este {0}. Am {1} ani.'.format(self.name, self.age)
        pass

    def __del__(self):
        #print('Sterg persoana cu numele {0}'.format(self.name))
        pass


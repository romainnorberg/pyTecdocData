# -*- coding: utf-8 -*-

import tecdoc
import pySettings
import os


f = __file__
f = f.replace('.py','.ini')

settings = pySettings.Settings(f)

settings.load()

datadir = settings.getkey('datadir')
tecdoc.setDataDir(datadir)

#settings key complected_cds = []  list of complected cd's not used at this time


#settings key current_cd = {} keys: 'tecdocCD' and 'dsn'


current_cd = settings.getkey('current_cd')



cd = tecdoc.Cd(current_cd['tecdocCD'], dsn=current_cd['dsn'])
print(cd)

cd.loadTablesFromDB()
print(cd)

#cd.loadTableRows()

# -*- coding: utf-8 -*-

import tecdoc

cd = tecdoc.Cd('TECDOC_CD_2_2015', dsn="t_2_15")
print(cd)

cd.loadTablesFromDB()
print(cd)

cd.loadTableRows()

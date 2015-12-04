# -*- coding: utf-8 -*-

import tecdoc


#please set your data directory !
#make sure you have enougth space!
# DO NOT manualy delete it !

datadir = r'D:\tecdoc_data\data'
tecdoc.setDataDir(datadir)




#please set uo your DSN in Windows -> Control Panel -> ODBC
#you have to set remember password, and choose default schema (TECDOC_CD_n_nnnn)
#you should also change teccd to be the default schema !
#dsn is the name you give to your connection in Control Panel -> ODBC !
teccd = 'TECDOC_CD_2_2015'
cd = tecdoc.Cd(teccd, dsn="t_2_15")
print(cd)

cd.loadTablesFromDB()
print(cd)

cd.loadTableRows()

'''
    Fernando Piccini - 2021

    Python connection example with MySQL using pymysql
        1) Start the Service
        2) Run application
'''

import pymysql

conexao = pymysql.connect (
    host= 'localhost',
    user= 'root',
    passwd= 'root'
)

cursor = conexao.cursor()
cursor.execute('show databases')

for x in cursor:
    print(x)
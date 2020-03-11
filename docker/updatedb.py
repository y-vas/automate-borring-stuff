import json
from datetime import datetime
import sys
import configparser
import mysql.connector

config = configparser.ConfigParser()
config.read('../.env',encoding='utf-8-sig')

cnf = config['ENVIROMENT_VARIABLES']

cnx = mysql.connector.connect(
    user=cnf['DB_USERNAME'],
    password=cnf['DB_PASSWORD'],
    host=cnf['DB_HOST'],
    database=cnf['DB_DATABASE']
)

cursor = cnx.cursor()

data = json.loads( open("db/dbchanges.json", "r").read() )

for x in data.keys():
    dt = datetime.strptime(x, '%Y-%m-%d')

    if sys.argv[1] != 'all':
        ft = datetime.strptime(sys.argv[1], '%Y-%m-%d')
        if dt < ft: continue

    quers = data[x]

    for q in quers:
        cursor.execute(q)
        print('INSERTAT \n',q,'\n')

cnx.close()
print('sha acabat')

# https://dev.mysql.com/downloadeds/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '#S3XjH1d96^slL$h',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done!")
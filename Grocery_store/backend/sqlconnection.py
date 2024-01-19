import mysql.connector
cnx=None
def sqlconnect():
    global cnx
    if cnx==None:
        cnx=mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='grocery')
    
    return cnx
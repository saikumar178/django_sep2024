import pymysql

def connectDb():
    connectionObj = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='root123',
            db='sai_db', charset='utf8')
    print('Database connected successfully')
    return connectionObj

def disconnectDb(conn):
    conn.close()
    print('Database disconnected successfully')

connectionObject = connectDb()
disconnectDb(connectionObject)
import pymysql

db = pymysql.connect(host='localhost', user='root', password='ericsinger')
cursor = db.cursor()
# cursor.execute("select version()")

# data = cursor.fetchone()
# print(data)

sql = '''SELECT * FROM movit.posicoes'''
cursor.execute(sql)

data = cursor.fetchall()
print(data)
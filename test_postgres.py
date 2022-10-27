import psycopg2


con = psycopg2.connect(host='localhost', database='10i9', user='10i9', password='')
cur = con.cursor()

sql = 'SELECT version()'
cur.execute(sql)

data = cur.fetchall()
print(data)



# sql = "insert into cidade values (default,'São Paulo,'SP')"
# cur.execute(sql)
# con.commit()
# cur.execute('select * from cidade')
# recset = cur.fetchall()
# for rec in recset:
#print (rec)
# con.close()
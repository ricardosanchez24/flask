import pymysql

miConexion = pymysql.connect(host='localhots', user='root', passwd='123456789', database='holamundo')

cur = miConexion.cursor()
cur.execute('select titulo,autor,año from libros')
for titulo, autor, año in cur.fetchall:
    print(titulo, "|" ,autor, "|" ,año)

miConexion.close()
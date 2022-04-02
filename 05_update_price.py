import pymysql

con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
curs=con.cursor()
prodid=input('Enter product id : ')

curs.execute("select * from mobiles where prodid='%s'" %prodid)
data=curs.fetchall()

if data:
    pr=float(input('Enter price : '))
    curs.execute("update mobiles set price =%f where prodid='%s'" %(pr,prodid))
    con.commit()
    print('price updated')
else:
    print('mobile does not exist')
con.close()

import pymysql

con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
curs=con.cursor()
curs.execute("select * from mobiles")
data=curs.fetchall()
print(data)
# data is tuple of tuples

for rec in data:
    print(rec) 

con.close()


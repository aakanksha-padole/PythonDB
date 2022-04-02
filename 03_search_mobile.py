import pymysql
try:
    con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
    curs=con.cursor()

    md=input('Enter model name : ')
    curs.execute("select * from mobiles where prodid ='%s'" %md)
    data=curs.fetchall()

    for rec in data:
        print(rec)
except:
  print('not found')

con.close()

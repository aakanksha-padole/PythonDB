import pymysql
try:
    con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
    curs=con.cursor()

    cp=input('Enter company name : ')
    curs.execute("select * from mobiles where company ='%s'" %cp)
    data=curs.fetchall()

    for rec in data:
        print(rec)
except:
  print('not found')

con.close()

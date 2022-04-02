import pymysql

try:
    con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
    curs=con.cursor()
    mod = input('Enter Model Name of mobile : ')
    curs.execute("select * from mobiles where modelname = '%s'" %mod)
    data = curs.fetchall()
    if data:
        pur = input('Enter the purpose of mobile : ')
        curs.execute("update mobiles set purpose='%s' where modelname='%s'" %(pur, mod))
        con.commit()
        print('Purpose added successfully')
    else:
        print('Mobile not found')
except Exception as e:
    print('Error : %s' %e)
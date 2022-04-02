import pymysql
try: 
    con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
    curs=con.cursor()

    ram=input('Enter Ram : ')
    rom=input('Enter Rom : ')
    curs.execute("select * from mobiles where ram='%s' and rom='%s'" %(ram, rom))
    data=curs.fetchall()
    if data:
        for rec in data:
            print(rec)
    else:
        print('No mobile having these ram and rom combination')
except Exception as e:
    print('Error : %s' %e)
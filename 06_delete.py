from tkinter.messagebox import YES
import pymysql

con=pymysql.connect(host='b39ypfpbn2wifz69zi63-mysql.services.clever-cloud.com',user='ujzmqwgblkrmfx3j',password='mOrNa0jsZjx3iIRvGe6P',database='b39ypfpbn2wifz69zi63')
curs=con.cursor()
prodid=input('Enter product id : ')
curs.execute("select * from mobiles where prodid='%s'" %prodid)
data=curs.fetchall()

if data:
    ch=input('Do you want to delete ')
    if ch.lower()=='yes':
        curs.execute("delete from mobiles where prodid='%s'" %prodid)
        con.commit()
        print('mobiles deleted successfully')
else:
    print('mobiles does not exist')

con.close()

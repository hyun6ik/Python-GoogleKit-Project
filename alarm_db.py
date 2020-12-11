import datetime
import time
import pymysql

from global_collection import *

class Alarm_db:
    def __init__(self):
        self.conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        self.curs = self.conn.cursor()

    def checkDatabaseMorningConnect(self):
        morningCheck = "select Morning from medicinecheck where Morning in ('X','△','O') and Date = curdate()"
        self.curs.execute(morningCheck)
        self.conn.commit()
        self.conn.close()
        rows =self.curs.fetchall()
        print('rows = ', rows)
        return rows
        

    def checkDatabaseLunchConnect(self):
        lunchCheck = "select Lunch from medicinecheck where Lunch in ('X','△','O') and Date = curdate()"
        self.curs.execute(lunchCheck)
        self.conn.commit()
        self.conn.close()
        rows =self.curs.fetchall()
        print('rows = ', rows)
        return rows
    
    def checkDatabaseDinnerConnect(self):
        dinnerCheck = "select Dinner from medicinecheck where Dinner in ('X','△','O') and Date = curdate()"
        self.curs.execute(dinnerCheck)
        self.conn.commit()
        self.conn.close()
        rows =self.curs.fetchall()
        print('rows = ', rows)
        return rows
        

    def createDate(self):
        createDate = 'insert into medicinecheck(Date) select curdate() from dual where not exists (select Date from medicinecheck where Date=curdate())'
        self.curs.execute(createDate)
        self.conn.commit()
        self.conn.close()
        morningCount =0
        lunchCount =0
        dinnerCount =0
        time.sleep(300)
    
        
    
    

    
 
        
    

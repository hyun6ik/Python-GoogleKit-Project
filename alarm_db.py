import datetime
import time
import pymysql

from global_collection import *

class Alarm_db:
    def __init__(self):
        self.conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        self.curs = self.conn.cursor()

    def checkDatabaseMorningConnect(self, conn, curs):
        morningCheck = "select Morning from medicinechecks where Morning in ('X','△','O') and Date = curdate()"
        curs.execute(morningCheck)
        conn.commit()
        conn.close()
        rows =curs.fetchall()
        print('rows = ', rows)
        return rows
        

    def checkDatabaseLunchConnect(self, conn ,curs):
        lunchCheck = "select Lunch from medicinechecks where Lunch in ('X','△','O') and Date = curdate()"
        curs.execute(lunchCheck)
        conn.commit()
        conn.close()
        rows =curs.fetchall()
        print('rows = ', rows)
        return rows
    
    def checkDatabaseDinnerConnect(self, conn, curs):
        dinnerCheck = "select Dinner from medicinechecks where Dinner in ('X','△','O') and Date = curdate()"
        curs.execute(dinnerCheck)
        conn.commit()
        conn.close()
        rows =curs.fetchall()
        print('rows = ', rows)
        return rows
        

    def createDate(self, conn, curs):
        createDate = 'insert into medicinechecks(Date) select curdate() from dual where not exists (select Date from medicinechecks where Date=curdate())'
        curs.execute(createDate)
        conn.commit()
        conn.close()
        global morningCount
        morningCount =0
        global lunchCount
        lunchCount =0
        global dinnerCount
        dinnerCount =0
        
    
    

    
 
        
    

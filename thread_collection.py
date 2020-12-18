import threading
import twilio_multiple_test as tmt

from global_collection import *
# import alarm_test2 as at2

from alarm_db import *
from alarm_MLD import *
from alzheimer import *
from pygame import mixer

global rows

class AsyncTask:
    def __init__(self):
        self.conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        self.curs = self.conn.cursor()
#         self.db_init()
        self.m=Alarm()
        self.db_check = Alarm_db()
#         
#     def db_init(self):
#         self.conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
#         self.curs = self.conn.cursor()
#         

    def sing(self,route):
        mixer.init()
        mixer.music.load(route)
        mixer.music.play()
        
    def songstop(self):
        mixer.music.stop()
        
    def emergency(self,comment):
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        tmt.sendMessage(comment, conn, curs)
    
    def alzheimer_test(self):
        az = Alzheimer()
        
        az.questionCreate()
        az.answerCreate()
        az.alzheimerQuestion(1)
        az.alzheimerQuestion(2)
        az.alzheimerQuestion(3)
        az.alzheimerQuestion(4)
        az.alzheimerQuestion(5)
        az.scoreCheck()
        az.scoreTotal()
        mixer.init()
        mixer.music.load('/home/pi/Music/alzheimertestcomplete.mp3')
        mixer.music.play()
        
    
    def thread_date_create(self):
        
#         now = datetime.datetime.now()
#         hour = now.hour
#         minute = now.minute
#         print('thread_Date_create')
#         if hour == 12 and minute == 32:
        print('createDB')
#         dbCreate = Alarm_db()
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        self.db_check.createDate(conn, curs)
    
    def thread_alarm(self):
        print('thread_alarm')
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        
#         Count 들은 thread_date_create()에서 만들 때 모두 초기화
        global morningCount
        morningCount = 0
        global lunchCount
        lunchCount = 0
        global dinnerCount
        dinnerCount = 0
        
        while True:
            if hour == 13 and minute == 37:
                self.thread_date_create()
            if hour == 14 and minute ==7 and morningCount == 0:
                self.morning_func()
            if hour == 14 and minute == 0 and lunchCount ==0:
                self.lunch_func()
            if hour == 13 and minute == 27 and dinnerCount ==0:
                self.dinner_func()
            else:
                continue

    def morning_func(self):
        global morningCount
        morningCount = morningCount + 1
        
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        self.m.morning(conn, curs)
        
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        rows = self.db_check.checkDatabaseMorningConnect(conn, curs)
        
        self.thread_morning_check(rows)
            
    def lunch_func(self):
        global lunchCount
        lunchCount = lunchCount + 1
        
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        self.m.lunch(conn, curs)
        
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        rows = self.db_check.checkDatabaseLunchConnect(conn, curs)
        
        self.thread_lunch_check(rows)
        
    def dinner_func(self):
        global dinnerCount
        dinnerCount = dinnerCount + 1
        
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        self.m.dinner(conn, curs)
        
        conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
        curs = conn.cursor()
        rows = self.db_check.checkDatabaseDinnerConnect(conn, curs)
        
        self.thread_dinner_check(rows)
        
        
    def thread_morning_check(self,rows):
        global morningCount
        print(morningCount)
        
        
        
        if rows[0][0] == 'X' or rows[0][0] == '△':
#             morningCount = morningCount + 1
#             self.db_init()
            print('row[0][0] = ',rows[0][0])
            if morningCount == 3 and rows[0][0]=='X' :
                conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
                curs = conn.cursor()
                tmt.sendMessage('현재 아무개씨가 아침에 약을 드시지 않았습니다.확인 부탁드리겠습니다.', conn,curs)
                return
            elif morningCount ==3 and rows[0][0] == '△':
                conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
                curs = conn.cursor()
                tmt.sendMessage('현재 아무개씨가 30분째 아무런 응답이 없습니다. 신속히 확인 부탁드리겠습니다.', conn,curs)
                return
            else:
                time.sleep(10)
                self.morning_func()
        elif morningCount == 3:
            return
        elif rows[0][0] == 'O':
            morningCount=3
            print('morningCount = ',morningCount)
            return
        
    def thread_lunch_check(self,rows):
        global lunchCount
        print(lunchCount)
        
        
        
        if rows[0][0] == 'X' or rows[0][0] == '△':
#             morningCount = morningCount + 1
#             self.db_init()
            print('row[0][0] = ',rows[0][0])
            if lunchCount == 3 and rows[0][0]=='X' :
                conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
                curs = conn.cursor()
                tmt.sendMessage('현재 아무개씨가 점심에 약을 드시지 않았습니다.확인 부탁드리겠습니다.', conn,curs)
                return
            elif lunchCount ==3 and rows[0][0] == '△':
                conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
                curs = conn.cursor()
                tmt.sendMessage('현재 아무개씨가 30분째 아무런 응답이 없습니다. 신속히 확인 부탁드리겠습니다.', conn,curs)
                return
            else:
                time.sleep(10)
                self.lunch_func()
        elif lunchCount == 3:
            return
        elif rows[0][0] == 'O':
            lunchCount=3
            print('lunchCount = ',lunchCount)
            return
        
    def thread_dinner_check(self,rows):
        global dinnerCount
        print(dinnerCount)
        
        
        if rows[0][0] == 'X' or rows[0][0] == '△':
#             morningCount = morningCount + 1
#             self.db_init()
            print('row[0][0] = ',rows[0][0])
            if dinnerCount == 3 and rows[0][0]=='X' :
                conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
                curs = conn.cursor()
                tmt.sendMessage('현재 아무개씨가 저녁에 약을 드시지 않았습니다.확인 부탁드리겠습니다.', conn,curs)
                return
            elif dinnerCount ==3 and rows[0][0] == '△':
                conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
                curs = conn.cursor()
                tmt.sendMessage('현재 아무개씨가 30분째 아무런 응답이 없습니다. 신속히 확인 부탁드리겠습니다.', conn,curs)
                return
            else:
                time.sleep(10)
                self.dinner_func()
        elif dinnerCount == 3:
            return
        elif rows[0][0] == 'O':
            dinnerCount=3
            print('dinnerCount = ',dinnerCount)
            return
    
    
        
                
                

        


# def main():

# if __name__ == '__main__':
#     main()

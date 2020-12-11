import threading
import twilio_multiple_test as tmt
from global_collection import *
# import alarm_test2 as at2

from alarm_db import *
from alarm_MLD import *
from alzheimer import *
from pygame import mixer

class AsyncTask:
    def __init__(self):
        pass

    def sing(self,route):
        mixer.init()
        mixer.music.load(route)
        mixer.music.play()
        
    def songstop(self):
        mixer.music.stop()
        
    def emergency(self,comment):
        tmt.sendMessage(comment)
    
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
        
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        print('thread_Date_create')
        if hour == 13 and minute == 53:
            print('createDB')
            dbCreate = Alarm_db()
            dbCreate.createDate()
    
    def thread_alarm(self):
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        m=Alarm()
        if  hour ==  9 and minute == 0:
#             m = Alarm()
            m.morning()
            rows = m.checkDatabaseMorningConnect()
            if morningCount != 3:
                self.thread_morning_check()
        if hour == 15 and minute ==7:
            print('thread_alarm')
            m.lunch()
            print('m.lunch')
            rows = m.checkDatabaseLunchConnect()
            if lunchCount != 3:
                self.thread_lunch_check()
                print('thread_lunch_check()')
        if hour == 19 and minute ==0:
            m.dinner()
            rows = m.checkDatabaseDinnerConnect()
            if dinnerCount != 3:
                self.thread_dinner_check()        
        
    def thread_morning_check(self):
        if rows[0][0] == 'X' or rows[0][0] == '△':
            morningCount = morningCount + 1
            timer = threading.Timer(600,self.thread_morning_check)
            timer.start()
            print('row[0][0] = ',rows[0][0])
            if morningCount == 3 and rows[0][0]=='X' :
                tmt.sendMessage('현재 아무개씨가 아침에 약을 드시지 않았습니다.확인 부탁드리겠습니다.')
            elif morningCount ==3 and rows[0][0] == '△':
                tmt.sendMessage('현재 아무개씨가 30분째 아무런 응답이 없습니다. 신속히 확인 부탁드리겠습니다.')
        elif rows[0][0] == 'O':
            morningCount=3
            print('morningCount = ',morningCount)
        
    def thread_lunch_check(self):
        if rows[0][0] == 'X' or rows[0][0] == '△':
            lunchCount = lunchCount + 1
            timer = threading.Timer(60,self.thread_lunch_check)
            timer.start()
            print('row[0][0] = ',rows[0][0])
            if lunchCount == 3 and rows[0][0]=='X' :
                tmt.sendMessage('현재 아무개씨가 점심 약을 드시지 않았습니다.확인 부탁드리겠습니다.')
            elif lunchCount ==3 and rows[0][0] == '△':
                tmt.sendMessage('현재 아무개씨가 30분째 아무런 응답이 없습니다. 신속히 확인 부탁드리겠습니다.')
        elif rows[0][0] == 'O':
            lunchCount=3
            print('lunchCount = ',lunchCount)
            
    def thread_dinner_check(self):
        if rows[0][0] == 'X' or rows[0][0] == '△':
            dinnerCount = dinnerCount + 1
            timer = threading.Timer(600,self.thread_dinner_check)
            timer.start()
            print('row[0][0] = ',rows[0][0])
            if dinnerCount == 3 and rows[0][0]=='X' :
                tmt.sendMessage('현재 아무개씨가 저녁 약을 드시지 않았습니다.확인 부탁드리겠습니다.')
            elif dinnerCount ==3 and rows[0][0] == '△':
                tmt.sendMessage('현재 아무개씨가 30분째 아무런 응답이 없습니다. 신속히 확인 부탁드리겠습니다.')
        elif rows[0][0] == 'O':
            dinnerCount=3
            print('dinnerCount = ',dinnerCount)
                
                

        


# def main():

# if __name__ == '__main__':
#     main()

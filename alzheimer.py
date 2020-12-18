import pymysql
from global_collection import *  
import time

from language_collection import *
from gtts import gTTS
from pygame import mixer
from aiy.cloudspeech import CloudSpeechClient
from aiy.board import Board, Led

class Alzheimer:
    def __init__(self):
        self.conn = pymysql.connect(host = HOST, port= PORT, password= PASSWORD, user = USER, db = DB, charset= CHARSET)
        self.curs = self.conn.cursor()
        

    def alzheimerSQLConnect(self):
        sql = "SELECT * FROM alzheimer_tests where Date = curdate()" # 실행 할 쿼리문 입력
        self.curs.execute(sql) # 쿼리문 실행

        rows = self.curs.fetchall() # 데이터 패치
        self.conn.commit()

        print(rows)
        return rows
        
        

    def alzheimerUpdateConnect(self,text,reply):
        text = "'"+text+"'"
        sql2 = "set @text =" + text
        self.curs.execute(sql2)
        self.conn.commit()
        
        sql3 = "set @reply = " + str(reply)
        self.curs.execute(sql3)
        self.conn.commit()
        
        sql = "update alzheimer_tests set reply = @text where QuestionNumber = @reply and Date = curdate()" # 실행 할 쿼리문 입력
        self.curs.execute(sql) # 쿼리문 실행

        rows = self.curs.fetchall() # 데이터 패치
        self.conn.commit()
        time.sleep(1.5)
        print(rows)
        return 
        
        
    
    def alzheimerQuestion(self,question):
        dbTest = self.alzheimerSQLConnect()
        print(dbTest)
        mp3question = dbTest[question-1][3]
        __author__ = 'info-lab'
        tts = gTTS( text=mp3question, lang='ko', slow=False )
        tts.save('/home/pi/Music/question{0}.mp3'.format(question))
        mixer.init()
        mixer.music.load('/home/pi/Music/question{0}.mp3'.format(question))
        mixer.music.play()
        if question ==2 :
            time.sleep(3)
        else:
            time.sleep(1.5)
        
        
        logging.basicConfig(level=logging.DEBUG)
        parser = argparse.ArgumentParser(description='Assistant service example.')
        parser.add_argument('--language', default=locale_language())
        args = parser.parse_args()

        logging.info('Initializing for language %s...', args.language)

        hints = get_hints(args.language)
        print('치매테스트중')
        client = CloudSpeechClient()

        text = client.recognize(language_code=args.language)
        time.sleep(1)

        logging.info('Say something.')
        print(text)
        if text is None:
            text = str(text)
        self.alzheimerUpdateConnect(text,question)
        return 
        


    def answerCreate(self):
               
        answer1 = "update alzheimer_tests set Answer = (select case dayofweek(curdate()) \
        when '1' then '일요일' \
        when '2' then '월요일' \
        when '3' then '화요일' \
        when '4' then '수요일' \
        when '5' then '목요일' \
        when '6' then '금요일' \
        when '7' then '토요일' \
        end as dayofweek where questionNumber = 1)"
                    
        self.curs.execute(answer1)
        self.conn.commit()
        
        answer2 = "update alzheimer_tests set Answer = '서울특별시 양천구 목동' where questionNumber=2"
        self.curs.execute(answer2)
        self.conn.commit()
        answer3 = "update alzheimer_tests set Answer = '토마토 금황' where questionNumber=3"
        self.curs.execute(answer3)
        self.conn.commit()
        answer4 = "update alzheimer_tests set Answer = '88' where questionNumber=4"
        self.curs.execute(answer4)
        self.conn.commit()
        answer5 = "update alzheimer_tests set Answer = '간장 공장 공장장' where questionNumber=5"
        self.curs.execute(answer5)
        self.conn.commit()
        return 
        
    
    def scoreCheck(self):
        
        reply1 = "select reply from alzheimer_tests where questionnumber = 1"
        self.curs.execute(reply1)
        self.conn.commit()
        replyrows = self.curs.fetchall()
        
        answer1 = "select answer from alzheimer_tests where questionnumber = 1"
        self.curs.execute(answer1)
        self.conn.commit()
        answerrows = self.curs.fetchall()
        
        if replyrows == answerrows:
            scoreCheck = "update alzheimer_tests set scorecheck = 20 where questionnumber = 1"
            self.curs.execute(scoreCheck)
            self.conn.commit()
        else :
            scoreCheck = "update alzheimer_tests set scorecheck = 0 where questionnumber = 1"
            self.curs.execute(scoreCheck)
            self.conn.commit()
            
            
        reply2 = "select reply from alzheimer_tests where questionnumber = 2"
        self.curs.execute(reply2)
        self.conn.commit()
        replyrows = self.curs.fetchall()
        
        answer2 = "select answer from alzheimer_tests where questionnumber = 2"
        self.curs.execute(answer2)
        self.conn.commit()
        answerrows = self.curs.fetchall()
        
        if replyrows == answerrows:
            scoreCheck = "update alzheimer_tests set scorecheck = 20 where questionnumber = 2"
            self.curs.execute(scoreCheck)
            self.conn.commit()
        else :
            scoreCheck = "update alzheimer_tests set scorecheck = 0 where questionnumber = 2"
            self.curs.execute(scoreCheck)
            self.conn.commit()
            
        reply3 = "select reply from alzheimer_tests where questionnumber = 3"
        self.curs.execute(reply3)
        self.conn.commit()
        replyrows = self.curs.fetchall()
        
        answer3 = "select answer from alzheimer_tests where questionnumber = 3"
        self.curs.execute(answer3)
        self.conn.commit()
        answerrows = self.curs.fetchall()
        
        if replyrows == answerrows:
            scoreCheck = "update alzheimer_tests set scorecheck = 20 where questionnumber = 3"
            self.curs.execute(scoreCheck)
            self.conn.commit()
        else :
            scoreCheck = "update alzheimer_tests set scorecheck = 0 where questionnumber = 3"
            self.curs.execute(scoreCheck)
            self.conn.commit()
        
        reply4 = "select reply from alzheimer_tests where questionnumber = 4"
        self.curs.execute(reply4)
        self.conn.commit()
        replyrows = self.curs.fetchall()
        
        answer4 = "select answer from alzheimer_tests where questionnumber = 4"
        self.curs.execute(answer4)
        self.conn.commit()
        answerrows = self.curs.fetchall()
        
        if replyrows == answerrows:
            scoreCheck = "update alzheimer_tests set scorecheck = 20 where questionnumber = 4"
            self.curs.execute(scoreCheck)
            self.conn.commit()
        else :
            scoreCheck = "update alzheimer_tests set scorecheck = 0 where questionnumber = 4"
            self.curs.execute(scoreCheck)
            self.conn.commit()
            
            reply5 = "select reply from alzheimer_tests where questionnumber = 5"
            self.curs.execute(reply5)
            self.conn.commit()
            replyrows = self.curs.fetchall()
            
            answer5 = "select answer from alzheimer_tests where questionnumber = 5"
            self.curs.execute(answer5)
            self.conn.commit()
            answerrows = self.curs.fetchall()
        
        if replyrows == answerrows:
            scoreCheck = "update alzheimer_tests set scorecheck = 20 where questionnumber = 5"
            self.curs.execute(scoreCheck)
            self.conn.commit()
        else :
            scoreCheck = "update alzheimer_tests set scorecheck = 0 where questionnumber = 5"
            self.curs.execute(scoreCheck)
            self.conn.commit()
        
        return
            
        
    def questionCreate(self):           
        questionCreate = "insert into alzheimer_tests (Date, questionNumber, question) values (curdate(), 1, '오늘은 무슨 요일 입니까?'), (curdate(), 2, '현재 거주하고 계신 주소지를 말해보세요.'),(curdate(), 3, '황금토마토를 거꾸로 말해보세요.') , (curdate(), 4, '백 빼기 칠 빼기 오는?'), (curdate(), 5, '간장공장공장장을 따라해 보세요.')"
        
        self.curs.execute(questionCreate)
        self.conn.commit()
        return
        

    def scoreTotal(self):
        scoreTotal = 'insert into alzheimer_lists(Date,score) values (curdate(), (select sum(Scorecheck) from alzheimer_tests));'
        self.curs.execute(scoreTotal)
        self.conn.commit()
        self.conn.close()
        return
                            
# if __name__ == '__main__':
#     a = Alzheimer()
#     a.questionCreate()



                   
           



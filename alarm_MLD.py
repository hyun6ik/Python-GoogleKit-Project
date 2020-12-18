import argparse
import locale
import logging
import pymysql
import time

from global_collection import *
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from pygame import mixer


conn = pymysql.connect(host =HOST ,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
curs = conn.cursor()

morningOkay = "update medicinechecks set Morning = 'O' where Date= curdate()"
morningNo = "update medicinechecks set Morning = 'X'  where Date= curdate()"
morningNoanswer = "update medicinechecks set Morning = '△'  where Date= curdate()"
morningCheck = "select Morning from medicniechecks where Morning in ('X',null) and Date = curdate()"
lunchOkay = "update medicinechecks set Lunch = 'O'  where Date= curdate()"
lunchNo = "update medicinechecks set Lunch = 'X'  where Date= curdate()"
lunchNoanswer = "update medicinechecks set Lunch = '△'  where Date= curdate()"
dinnerOkay = "update medicinechecks set Dinner = 'O'  where Date= curdate()"
dinnerNo = "update medicinechecks set Dinner = 'X'  where Date= curdate()"
dinnerNoanswer = "update medicinechecks set Dinner = '△'  where Date= curdate()"

def get_hints(language_code):
    if language_code.startswith('ko_'):
        return ('먹었어',
            '아니')

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language


class Alarm:
    def __init__(self):
#         self.conn = pymysql.connect(host =HOST ,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
#         self.curs = self.conn.cursor()
        logging.basicConfig(level=logging.DEBUG)
        self.parser = argparse.ArgumentParser(description='Assistant service example.')
        self.parser.add_argument('--language', default=locale_language())
        self.args = self.parser.parse_args()
        logging.info('Initializing for language %s...', self.args.language)

        self.hints = get_hints(self.args.language)
        self.client = CloudSpeechClient()
        
    def morning(self,conn,curs):
       
        # 응답 3번 기다려주는 변수
        i=0
        count =0
        while i < 3 :
            
            if self.hints:
                logging.info('alarm_MLD : Say something, e.g. %s.' % ', '.join(self.hints))
            else:
                logging.info('alarm_MLD : Say something.')
        
            #
            time.sleep(5)
            mixer.init()
            mixer.music.load('/home/pi/Music/morningquestion.mp3')
            mixer.music.play()
            i = i + 1
            time.sleep(3)
            text = self.client.recognize(language_code=self.args.language,
                                hint_phrases=self.hints)
            if text is None:
                logging.info('alarm_MLD : You said nothing.')
                count = count + 1
                print('count',count)
                if count==3:
                    curs.execute(morningNoanswer)
                    conn.commit()
                    conn.close()
                    return 
                continue
            
                       
            logging.info('alarm_MLD : You said: "%s"' % text)

            if '먹었어' in text:
                logging.info('alarm_MLD : You said: "%s"' % text)
                curs.execute(morningOkay)
                conn.commit()
                conn.close()
                print('ConfirmOkay')
                mixer.init()
                mixer.music.load('/home/pi/Music/morninganswer.mp3')
                mixer.music.play()
                return
            elif '아니' in text:
                logging.info('alarm_MLD : You said: "%s"' % text)
                curs.execute(morningNo)
                conn.commit()
                conn.close()
                print('ConfirmNo')
                return 
            else:
                time.sleep(3)
                continue
            
    def lunch(self,conn,curs):
       
        # 응답 3번 기다려주는 변수
        i=0
        count =0
        while i < 3 :
            
            if self.hints:
                logging.info('alarm_MLD : Say something, e.g. %s.' % ', '.join(self.hints))
            else:
                logging.info('alarm_MLD : Say something.')
        
            
            time.sleep(10)
            mixer.init()
            mixer.music.load('/home/pi/Music/lunchquestion.mp3')
            mixer.music.play()
            i = i + 1
            time.sleep(4)
            text = self.client.recognize(language_code=self.args.language,
                                hint_phrases=self.hints)
            if text is None:
                logging.info('alarm_MLD : You said nothing.')
                count = count + 1
                print('count',count)
                if count==3:
                    curs.execute(lunchNoanswer)
                    conn.commit()
                    conn.close()
                    return 
                continue
            
                       
            logging.info('alarm_MLD : You said: "%s"' % text)

            if '먹었어' in text:
                logging.info('alarm_MLD : You said: "%s"' % text)
                curs.execute(lunchOkay)
                conn.commit()
                conn.close()
                print('ConfirmOkay')
                mixer.init()
                mixer.music.load('/home/pi/Music/lunchanswer.mp3')
                mixer.music.play()
                return
            elif '아니' in text:
                logging.info('alarm_MLD : You said: "%s"' % text)
                curs.execute(lunchNo)
                conn.commit()
                conn.close()
                print('ConfirmNo')
                return 
            else:
                time.sleep(3)
                continue
            
    def dinner(self,conn,curs):
       
        # 응답 3번 기다려주는 변수
        i=0
        count =0
        while i < 3 :
            
            if self.hints:
                logging.info('alarm_MLD : Say something, e.g. %s.' % ', '.join(self.hints))
            else:
                logging.info('alarm_MLD : Say something.')
        
            
            time.sleep(10)
            mixer.init()
            mixer.music.load('/home/pi/Music/dinnerquestion.mp3')
            mixer.music.play()
            i = i + 1
            time.sleep(4)
            text = self.client.recognize(language_code=self.args.language,
                                hint_phrases=self.hints)
            if text is None:
                logging.info('alarm_MLD : You said nothing.')
                count = count + 1
                print('count',count)
                if count==3:
                    curs.execute(dinnerNoanswer)
                    conn.commit()
                    conn.close()
                    return 
                continue
            
                       
            logging.info('alarm_MLD : You said: "%s"' % text)

            if '먹었어' in text:
                logging.info('alarm_MLD : You said: "%s"' % text)
                curs.execute(dinnerOkay)
                conn.commit()
                conn.close()
                print('ConfirmOkay')
                mixer.init()
                mixer.music.load('/home/pi/Music/dinneranswer.mp3')
                mixer.music.play()
                return
            elif '아니' in text:
                logging.info('alarm_MLD : You said: "%s"' % text)
                curs.execute(dinnerNo)
                conn.commit()
                conn.close()
                print('ConfirmNo')
                return 
            else:
                time.sleep(3)
                continue
    
    
   
            
    
    
        

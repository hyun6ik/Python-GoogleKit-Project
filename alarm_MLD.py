import argparse
import locale
import logging
import pymysql

from global_collection import *
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from pygame import mixer


conn = pymysql.connect(host =HOST ,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
curs = conn.cursor()

morningOkay = "update medicinecheck set Morning = 'O' where Date= curdate()"
morningNo = "update medicinecheck set Morning = 'X'  where Date= curdate()"
morningNoanswer = "update medicinecheck set Morning = '△'  where Date= curdate()"
morningCheck = "select Morning from medicniecheck where Morning in ('X',null) and Date = curdate()"
lunchOkay = "update medicinecheck set Lunch = 'O'  where Date= curdate()"
lunchNo = "update medicinecheck set Lunch = 'X'  where Date= curdate()"
lunchNoanswer = "update medicinecheck set Lunch = '△'  where Date= curdate()"
dinnerOkay = "update medicinecheck set Dinner = 'O'  where Date= curdate()"
dinnerNo = "update medicinecheck set Dinner = 'X'  where Date= curdate()"
dinnerNoanswer = "update medicinecheck set Dinner = '△'  where Date= curdate()"

def get_hints(language_code):
    if language_code.startswith('ko_'):
        return ('먹었어',
            '아니')

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language


class Alarm:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.parser = argparse.ArgumentParser(description='Assistant service example.')
        self.parser.add_argument('--language', default=locale_language())
        self.args = self.parser.parse_args()
        logging.info('Initializing for language %s...', self.args.language)

        self.hints = get_hints(self.args.language)
        self.client = CloudSpeechClient()
        
    def morning(self):
        if self.hints:
            logging.info('Say something, e.g. %s.' % ', '.join(self.hints))
        else:
            logging.info('Say something.')
        text = self.client.recognize(language_code=self.args.language,
                                hint_phrases=self.hints)
        i=0
        while i == 0 :
            mixer.init()
            mixer.music.load('/home/pi/Music/morningquestion.mp3')
            mixer.music.play()
            time.sleep(3)
            i = i + 1
            if text is None:
                logging.info('You said nothing.')
                count = count + 1
                print(count)
                if(count==3):
                    curs.execute(morningNoanswer)
                    conn.commit()
                    conn.close()
                continue
                       
        logging.info('You said: "%s"' % text)

        if '먹었어' in text:
            curs.execute(morningOkay)
            conn.commit()
            conn.close()
            print('ConfirmOkay')
            mixer.init()
            mixer.music.load('/home/pi/Music/morninganswer.mp3')
            mixer.music.play()
        elif '아니' in text:
            curs.execute(morningNo)
            conn.commit()
            conn.close()
            print('ConfirmNo')
            
            
    def lunch(self):
#         if self.hints:
#             logging.info('Say something, e.g. %s.' % ', '.join(self.hints))
#         else:
#             logging.info('Say something.')
        text = self.client.recognize(language_code=self.args.language,
                                hint_phrases=self.hints)
        i=0
        while i == 0 :
            mixer.init()
            mixer.music.load('/home/pi/Music/lunchquestion.mp3')
            mixer.music.play()
            time.sleep(3)
            i = i + 1
            if text is None:
                logging.info('You said nothing.')
                count = count + 1
                print(count)
                if(count==3):
                    curs.execute(lunchNoanswer)
                    conn.commit()
                    conn.close()
                continue
                       
        logging.info('You said: "%s"' % text)

        if '먹었어' in text:
            curs.execute(lunchOkay)
            conn.commit()
            conn.close()
            print('ConfirmOkay')
            mixer.init()
            mixer.music.load('/home/pi/Music/lunchanswer.mp3')
            mixer.music.play()
        elif '아니' in text:
            curs.execute(lunchNo)
            conn.commit()
            conn.close()
            print('ConfirmNo')
            
        
    def dinner(self):
        if self.hints:
            logging.info('Say something, e.g. %s.' % ', '.join(self.hints))
        else:
            logging.info('Say something.')
        text = self.client.recognize(language_code=self.args.language,
                                hint_phrases=self.hints)
        i=0
        while i == 0 :
            mixer.init()
            mixer.music.load('/home/pi/Music/dinnerquestion.mp3')
            mixer.music.play()
            time.sleep(3)
            i = i + 1
            if text is None:
                logging.info('You said nothing.')
                count = count + 1
                print(count)
                if(count==3):
                    curs.execute(dinnerNoanswer)
                    conn.commit()
                    conn.close()
                continue
                       
        logging.info('You said: "%s"' % text)

        if '먹었어' in text:
            curs.execute(dinnerOkay)
            conn.commit()
            conn.close()
            print('ConfirmOkay')
            mixer.init()
            mixer.music.load('/home/pi/Music/dinneranswer.mp3')
            mixer.music.play()
        elif '아니' in text:
            curs.execute(dinnerNo)
            conn.commit()
            conn.close()
            print('ConfirmNo')
    
    
        

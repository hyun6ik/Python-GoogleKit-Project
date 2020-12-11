from global_collection import *
from language_collection import *
from thread_collection import *
from aiy.cloudspeech import CloudSpeechClient
from aiy.board import Board, Led
from alzheimer import *


def main():
    
    
    
    thread_instance = AsyncTask()
    alzheimer_instance = Alzheimer()
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)

    hints = get_hints(args.language)
    client = CloudSpeechClient()
    
    with Board() as board:
        while True:
            createDB = threading.Thread(target=thread_instance.thread_date_create)
            createDB.start()
            
            alarm = threading.Thread(target = thread_instance.thread_alarm)
            alarm.start()

            
            if hints:
                logging.info('Say something, e.g. %s.' % ', '.join(hints))
            else:
                logging.info('Say something.')
            text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
            
            if  text is None:
                logging.info('You said nothing.')
                continue
            
            
            #
            logging.info('You said: "%s"' % text)
            if '임영웅노래틀어 줘' in text: 
                sing = threading.Thread(target=thread_instance.sing('/home/pi/Music/임영웅.mp3'))
                sing.start()
            elif '영탁노래틀어 줘' in text:
                sing = threading.Thread(target=thread_instance.sing('/home/pi/Music/영탁.mp3'))
                sing.start()
            elif '송가인노래틀어 줘' in text:
                sing = threading.Thread(target=thread_instance.sing('/home/pi/Music/송가인.mp3'))
                sing.start()
            elif '노래 꺼 줘' in text: 
                songstop = threading.Thread(target=thread_instance.songstop)
                songstop.start()
            elif text not in hints and '노래 틀어 줘' in text:
                nosong = threading.Thread(target=thread_instance.sing('/home/pi/Music/nosong.mp3'))
                nosong.start()
            elif '살려 줘' in text:
                emergency = threading.Thread(target=thread_instance.emergency("현재 아무개씨가 위험한 상황에 빠졌습니다. 신속히 확인 부탁드리겠습니다"))
                emergency.start()
            elif '치매테스트 할게' in text:
                alzheimer = threading.Thread(target=thread_instance.alzheimer_test)
                alzheimer.start()                
            elif 'goodbye' in text:
                break
            

if __name__ == '__main__':
    main()

    
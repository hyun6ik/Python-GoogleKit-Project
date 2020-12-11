import argparse
import locale
import logging

def get_hints(language_code):
    if language_code.startswith('ko_'):
        return ('turn on the light',
                'turn off the light',
                'goodbye',
                '반 짝 반 짝',
                '임영웅노래틀어 줘',
                '영탁노래틀어 줘',
                '송가인노래틀어 줘',
                '살려 줘',
                '먹었어',
                '아니',
                '치매테스트 할게')

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language



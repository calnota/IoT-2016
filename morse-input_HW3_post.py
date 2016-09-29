import RPi.GPIO as GPIO
import time
import random


CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(7,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(16,GPIO.IN)
prev_input=0
prev_input2=0
prev_input3=0

def dot(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.5)
    return

def dash(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.5)
    return

while True:
    button_input = GPIO.input(7)
    if ((not prev_input)and button_input):
        your_input = random.choice(['fuck more', 'google less', 'delete facebook'])

        for letter in your_input:
                for symbol in CODE[letter.upper()]:
                    if symbol == '-':
                        dash(11)
                    elif symbol == '.':
                        dot(13)
                    else:
                        time.sleep(1)
            time.sleep(1)    
    prev_input=button_input
    time.sleep(0.05)
    GPIO.cleanup()

        button2_input = GPIO.input(15)
    if ((not prev_input2) and button2_input):
        disagree_input = 'fuck u'
        for letter in disagree_input:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash(12)
                elif symbol == '.':
                    dot(12)
                else:
                    time.sleep(1)
        time.sleep(1)
    prev_input2 = button2_input
    time.sleep(0.05)
    GPIO.cleanup()

    button3_input = GPIO.input(16)
    if((not prev_input3) and button3_input):
        agree_input = 'ok'
        for letter in agree_input:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash(18)
                elif symbol == '.':
                    dot(18)
                else:
                    time.sleep(1)
        time.sleep(1)
    prev_input3=button3_input
    time.sleep(0.05)
    GPIO.cleanup()

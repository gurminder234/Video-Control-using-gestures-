import serial  # Install using 'pip install pyserial'
import time  # Required to use delay functions
import pyautogui # Install using 'pip install pyautogui'

ArduinoSerial = serial.Serial('com5', 9600)  # Create Serial port object called arduinoSerialData
time.sleep(2)

while 1:
    incoming = str(ArduinoSerial.readline())  # read
    print(incoming)


    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)

    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right')

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'up')

    incoming = "";

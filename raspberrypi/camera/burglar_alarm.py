# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 21:27:34 2015

@author: neal
"""

from pir import *
from camera import *
from email_notification import *
import time

PIR_PIN = 23
PREFIX = 'photos/alert'
EMAIL_USER = 'nealagordonauto@gmail.com'
EMAIL_SERVER = 'smtp.gmail.com:587'
EMAIL_PWD = '11test11'

pir = PassiveInfraredSensor(PIR_PIN)
camera = Camera()
notifier = EmailNotification(EMAIL_SERVER, EMAIL_USER, EMAIL_PWD)
i = 0
last_state = False
while True:
    if (pir.motion_detected() == True):
        if (last_state == False):
            print 'INTRUDER ALERT!'
            image_file = PREFIX + '{0}.jpg' .format(i)
            camera.take_photo(image_file)
            notifier.send(image_file)
            i = i + 1
            last_state = True
    else:
        if (last_state == True):
            time.sleep(1)
            last_state = False;
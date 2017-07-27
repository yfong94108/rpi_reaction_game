import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#The pin that corresponds with each LED
#----------------------------------------------------------
led1 = 12
led2 = 16
led3 = 18
led4 = 22
led5 = 15
led6 = 11

#Can be used if you want another light to light up when you press the button, or for multiplayer
#-----------------------------------------------------------------------------------------------------------
GreenLED1 = 7
GreenLED2 = 33

#Second button is for multiplayer
#-----------------------------------
button1 = 13
button2 = 31

#Counts and prints if you missed the light or if you pressed at the right time
#----------------------------------------------------------------------------------
hitCount = 0
missCount = 0

#This is the GPIO setup for each LED
#--------------------------------------
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)

#This can be used if you want an extra light to light up when you press the button at the right time, or for multiplayer
#-----------------------------------------------------------------------------------------------------------------------------------
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GreenLED1, GPIO.OUT)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GreenLED2, GPIO.OUT)

#Program that makes the lights blink
#-----------------------------------------
button1Pressed = 0
buttonPressTime = time.clock()

def mycallback(channel):
    global button1Pressed
    global buttonPressTime

    buttonPressTime = time.time()
    
    button1Pressed = 1
    GPIO.output(GreenLED1, 1)
    time.sleep(onWait)
    GPIO.output(GreenLED1, 0)
   
    
GPIO.add_event_detect(button1, GPIO.FALLING, callback=mycallback, bouncetime=300)


onWait =0.25
offWait = 0

try:
    while 1:
        GPIO.output(GreenLED1, 0)
        GPIO.output(led1, 1)
        time.sleep(onWait)
 
        GPIO.output(led1, 0)
        time.sleep(offWait)
        GPIO.output(led2, 1)
        time.sleep(onWait)
 
        GPIO.output(led2, 0)
        time.sleep(offWait)

        if button1Pressed == 1:
            button1Pressed = 0
            onWait = onWait*1.05
            missCount = missCount + 1
            print "Missed!   Total Tries %.0f " %(hitCount+missCount), "-- Hits: %.0f " % hitCount, " Misses: %.0f" % missCount ,"times"

        GPIO.output(led3, 1)
        lightOnTime = time.time()
        time.sleep(onWait)
        if button1Pressed :
           hitCount= hitCount+1 
           print "Good!     Total Tries %.0f " %(hitCount+missCount),"response time: %.0f"%((buttonPressTime- lightOnTime)*1000.0),"ms  -- Hits: %.0f " % hitCount, " Misses: %.0f" % missCount ,"times"
           onWait = onWait*0.94       
           GPIO.output(GreenLED1, 1)
           GPIO.output(led1, 1)
           GPIO.output(led2, 1)
           GPIO.output(led3, 1)
           GPIO.output(led4, 1)
           GPIO.output(led5, 1)
           GPIO.output(led6, 1)
 
           time.sleep(onWait)
           GPIO.output(GreenLED1, 0)
           GPIO.output(led1, 0)
           GPIO.output(led2, 0)
           GPIO.output(led3, 0)
           GPIO.output(led4, 0)
           GPIO.output(led5, 0)
           GPIO.output(led6, 0)
           time.sleep(onWait)
           GPIO.output(GreenLED1, 1)
           GPIO.output(led1, 1)
           GPIO.output(led2, 1)
           GPIO.output(led3, 1)
           GPIO.output(led4, 1)
           GPIO.output(led5, 1)
           GPIO.output(led6, 1)
           time.sleep(onWait)
           GPIO.output(GreenLED1, 0)
           GPIO.output(led1, 0)
           GPIO.output(led2, 0)
           GPIO.output(led3, 0)
           GPIO.output(led4, 0)
           GPIO.output(led5, 0)
           GPIO.output(led6, 0)
           time.sleep(onWait)
           GPIO.output(GreenLED1, 1)
           GPIO.output(led1, 1)
           GPIO.output(led2, 1)
           GPIO.output(led3, 1)
           GPIO.output(led4, 1)
           GPIO.output(led5, 1)
           GPIO.output(led6, 1)
           time.sleep(onWait)
           GPIO.output(GreenLED1, 0)
           GPIO.output(led1, 0)
           GPIO.output(led2, 0)
           GPIO.output(led3, 0)
           GPIO.output(led4, 0)
           GPIO.output(led5, 0)
           GPIO.output(led6, 0)
           time.sleep(onWait)
           GPIO.output(GreenLED1, 1)
           GPIO.output(led1, 1)
           GPIO.output(led2, 1)
           GPIO.output(led3, 1)
           GPIO.output(led4, 1)
           GPIO.output(led5, 1)
           GPIO.output(led6, 1)
           time.sleep(onWait)
           GPIO.output(GreenLED1, 0)
           time.sleep(onWait)
           button1Pressed = 0
           GPIO.output(led1, 0)
           GPIO.output(led2, 0)
           GPIO.output(led3, 0)
           GPIO.output(led4, 0)
           GPIO.output(led5, 0)
           GPIO.output(led6, 0)


        GPIO.output(led3, 0)
        time.sleep(offWait)
        GPIO.output(led4, 1)
        time.sleep(onWait)
        GPIO.output(led4, 0)
        time.sleep(offWait)
        GPIO.output(led5, 1)
        time.sleep(onWait)
        GPIO.output(led5, 0)
        time.sleep(offWait)
        GPIO.output(led6, 1)
        time.sleep(onWait)
        GPIO.output(led6, 0)
        time.sleep(offWait)
    GPIO.cleanup()
finally:
    GPIO.cleanup()

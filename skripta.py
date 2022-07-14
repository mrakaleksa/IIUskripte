import RPi.GPIO as gpio 
 
from time import sleep, time 
 
gpio.setmode(gpio.BCM) 
 
ledPins = (17, 27, 22) # red=17, green=27, blue=22 
trig = 24 
echo = 23 
 
def setup(): 
    global pwrRed, pwrGreen, pwrBlue 
    for pin in ledPins: 
        gpio.setup(pin, gpio.OUT) 
        gpio.output(pin, 1) 
     
    gpio.setup(trig, gpio.OUT) 
    gpio.setup(echo, gpio.IN) 
    pwrRed = gpio.PWM(17, 2000) 
    pwrGreen = gpio.PWM(27, 2000) 
    pwrBlue = gpio.PWM(22, 2000) 
    pwrRed.start(100) 
    pwrGreen.start(100) 
    pwrBlue.start(100) 
 
def distance(): 
    gpio.output(trig, 1) 
    sleep(0.00001) 
    gpio.output(trig, 0) 
    startTime = time() 
    stopTime = time() 
     
    while gpio.input(echo) == 0: 
        startTime = time() 
    while gpio.input(echo) == 1: 
        stopTime = time() 
    elapsedTime = stopTime - startTime 
    distance = (elapsedTime * 34300) / 2 
    return distance 
def setColor(r, g, b): 
    pwrRed.ChangeDutyCycle(r) 
    pwrGreen.ChangeDutyCycle(g) 
    pwrBlue.ChangeDutyCycle(b) 
 
def main(): 
    try: 
        while True: 
 
            if distance() < 20: 
                print("Nedozvoljen pristup!!!") 
                setColor(0,100,100) 
                sleep(1) 
 
            else: 
                setColor(100,0,100) 
                sleep(1) 
    except KeyboardInterrupt: 
 
        gpio.cleanup() 
 
if __name__=="__main__": 
    setup() 
    main() 
    gpio.cleanup() 
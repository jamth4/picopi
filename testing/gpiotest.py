import machine
import utime
import builtins

#This application is meant to use a LED to test each GPIO pin after 
#soldering headers onto a Pico Pi.  Just cycle through the GPIO pins
#one at a time.  

number = 0
done = False
conTest = ""
tested = []
failed = []

while done == False:
    number = int(input("what pin do you want to check? "))
    tested.append(number)
    led = machine.Pin(number, machine.Pin.OUT)
    led.value(1)
    utime.sleep(4)
    led.value(0)
    passed = input("Did the LED power on? ")
    passed = passed.lower()
    if passed == 'no':
        failed.append(number)
    conTest = input("Are you done testing pins? ")
    conTest = conTest.lower()
    if conTest == 'yes':
        done = True
    else:
        done = False
print('You tested the following pins:')
print(tested)

print('The following pins failed:')
print(failed)

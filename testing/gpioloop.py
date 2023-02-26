import machine
import utime
import builtins

failed = []

for i in range(0,29):
    if i == 23:
        print('skipping 23')
    elif i == 24:
        print('skipping 24')
    else:
        if i == 25:
            print('GPIO 25 is the onboard LED')
        else:
            print('Connect LED to GPIO ' + str(i))
        input('press enter when ready')
        led = machine.Pin(i, machine.Pin.OUT)
        led.value(1)
        utime.sleep(4)
        led.value(0)
        passed = input("Did the LED power on? ")
        passed = passed.lower()
        if passed == 'no':
            failed.append(i)
#Results
print('The following pins failed:')
print(failed)

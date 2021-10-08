import os
import time
import RPi.GPIO as GPIO

gpiopin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpiopin, GPIO.OUT)

def getCPUtemperature():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    cpu_temp = cpu_temp.replace("temp=", "")
    cpu_temp = cpu_temp.replace("'C", "")
    return cpu_temp

# Temperatur lesen und in einen Float wandeln
temp_float = float(getCPUtemperature())

try:
    if temp_float > 43:
      GPIO.output(gpiopin, 0)
      print("HOT",temp_float)
    else:
      print("COLD",temp_float)
      GPIO.cleanup()
# Wird das Programm abgebrochen, dann den Lüfter wieder ausschalten
except KeyboardInterrupt:
    print(float(getCPUtemperature()))
    print("power off fan...")
    GPIO.output(gpiopin, False)
    print("cancelling...")


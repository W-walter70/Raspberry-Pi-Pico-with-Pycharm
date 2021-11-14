from machine import Pin
from WTimer import WTon
import utime


def execute_example():
    led = Pin(25, Pin.OUT)
    t1 = WTon(3000)
    t2 = WTon(3000)
    millis = 0
    m_millis = 0
    delta = 0
    start1 = False
    start2 = False
    led_on = 0
    while True:
        millis = utime.ticks_ms()
        delta = millis - m_millis
        start1 = not t2.getOutput()
        t1.run(delta_time=delta, IN=start1)
        start2 = t1.getOutput()
        t2.run(delta_time=delta, IN=start2)

        led.value(t1.getOutput())
        m_millis = millis

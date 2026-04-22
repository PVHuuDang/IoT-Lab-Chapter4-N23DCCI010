from machine import Pin
import dht
import time

# ===== DHT22 =====
dht_sensor = dht.DHT22(Pin(16))

# ===== HC-SR04 =====
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

# ===== LED =====
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

# ===== Đo khoảng cách (có timeout) =====
def get_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()

    timeout = 30000  # 30ms

    start = time.ticks_us()
    # chờ echo lên HIGH
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return -1  # lỗi

    start = time.ticks_us()
    # đo thời gian HIGH
    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return -1

    duration = time.ticks_diff(time.ticks_us(), start)
    distance = duration * 0.0343 / 2
    return distance

# ===== Header CSV =====
print("timestamp,temperature,humidity,distance,status")

while True:
    try:
        # DHT
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()

        # HC-SR04
        dist = get_distance()
        if dist < 0:
            dist = 0.0  # tránh lỗi

        # Time
        t = time.localtime()
        ts = f"{t[3]:02d}:{t[4]:02d}:{t[5]:02d}"

        # Status
        if temp > 30 or hum > 80 or dist < 20:
            status = "WARNING"
            red.value(1); yellow.value(0); green.value(0)
        else:
            status = "NORMAL"
            red.value(0); yellow.value(0); green.value(1)

        print(f"{ts},{temp:.1f},{hum:.1f},{dist:.1f},{status}")

    except Exception as e:
        print("error,0,0,0,ERROR")

    time.sleep(2)
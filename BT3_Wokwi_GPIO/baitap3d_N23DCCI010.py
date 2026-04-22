from machine import Pin, PWM, ADC
import time

# ===== LED đỏ PWM =====
led = PWM(Pin(15))   # GP15
led.freq(1000)

# ===== Biến trở =====
pot = ADC(Pin(26))   # GP26 = ADC0

while True:
    # Pico dùng read_u16() (0 → 65535)
    raw = pot.read_u16()

    # Điều chỉnh độ sáng LED
    led.duty_u16(raw)

    print("ADC:", raw)

    time.sleep(0.1)
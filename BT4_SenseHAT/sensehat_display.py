from sense_emu import SenseHat
import time


sense = SenseHat()


# Hiển thị text chạy ngang
sense.show_message('Hello IoT!', text_colour=[0, 255, 0], scroll_speed=0.08)
time.sleep(1)
sense.clear()
print('Text hiển thị xong.')
from sense_emu import SenseHat
import time


sense = SenseHat()


# Định nghĩa màu
y = [255, 255, 0]  # Vàng
b = [0, 0, 0]      # Tắt (đen)
r = [255, 0, 0]    # Đỏ


# Mặt cười 8x8 — sinh viên TỰ THIẾT KẾ
smiley = [
    b, b, y, y, y, y, b, b,
    b, y, b, b, b, b, y, b,
    y, b, r, b, b, r, b, y,
    y, b, b, b, b, b, b, y,
    y, b, r, b, b, r, b, y,
    y, b, b, r, r, b, b, y,
    b, y, b, b, b, b, y, b,
    b, b, y, y, y, y, b, b,
]


sense.set_pixels(smiley)
print('Biểu tượng đã hiển thị.')
time.sleep(5)
sense.clear()

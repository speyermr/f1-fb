import mmap
import os
from time import sleep

with open('/sys/class/graphics/fb0/virtual_size') as f:
    line = f.readline().strip()
    width, height = map(int, line.split(','))

with open('/sys/class/graphics/fb0/bits_per_pixel') as f:
    bits_per_pixel = int(f.read().strip())

f = os.open('/dev/fb0', os.O_RDWR)

size = (width * height * bits_per_pixel) // 8
fb = mmap.mmap(f, size, mmap.MAP_SHARED, mmap.PROT_WRITE)

def horizontal_line(y, x0, x1, color):
    fb.seek(4 * (y * width + x0))
    fb.write(color * (x1 - x0))

for t in range(100):
    horizontal_line(500 + t + 0, 500, 900, '\x00\x00\x00\x00')
    horizontal_line(500 + t + 1, 500, 900, '\xff\xff\xff\x00')
    sleep(1/10)

os.close(f)

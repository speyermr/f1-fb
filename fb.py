from random import randint
from time import sleep
import mmap
import os

print('1', flush=True)

with open('/sys/class/graphics/fb0/virtual_size') as f:
    line = f.readline().strip()
    width, height = map(int, line.split(','))

with open('/sys/class/graphics/fb0/bits_per_pixel') as f:
    bits_per_pixel = int(f.read().strip())

f = os.open('/dev/fb0', os.O_RDWR)

size = (width * height * bits_per_pixel) // 8
fb = mmap.mmap(f, size, mmap.MAP_SHARED, mmap.PROT_WRITE)

print('1', flush=True)
buf0 = bytearray(size)
print('1', flush=True)
buf1 = bytearray(size)
print('1', flush=True)

def blank():
    fb.seek(0)
    fb.write(b'\0' * size)

def horizontal_line(y, x0, x1, color):
    fb.seek(4 * (y * width + x0))
    fb.write(color * (x1 - x0))

def rect(x0, y0, x1, y1, color):
    for y in range(y0, y1):
        horizontal_line(y, x0, x1, color)

blank()

vx = 1
vy = 3

x = randint(0, width - 30)
y = randint(0, height - 30)

for t in range(1000):
    rect(x, y, x + 30, y + 30, b'\0\0\0\0')

    x += vx
    y += vy

    if x >= width - 30:
        x = width - 30
        vx *= -1
    if x < 0:
        x = 0
        vx *= -1

    if y >= height - 30:
        y = height - 30
        vy *= -1
    if y < 0:
        y = 0
        vy *= -1

    t_slow = t // 10 
    color = bytes((255, 128, 0, 0))
    rect(x, y, x + 30, y + 30, color)

    sleep(1/120)

os.close(f)

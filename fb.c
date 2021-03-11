#include <stdio.h>

int main() {
        FILE *fh;

        int width = 1920;
        int height = 1024;

        int r, g, b;

        fh = fopen("/dev/fb0", "wb");
        for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                        g = 0x00;
                        b = y % 0xff;
                        r = x % 0xff;
                        fputc(b, fh);
                        fputc(g, fh);
                        fputc(r, fh);
                        fputc(0x00, fh);
                }
        }
}

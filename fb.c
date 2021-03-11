#include <stdio.h>

int main() {
        FILE *fh;

        int width = 1920;
        int height = 1024;

        int r, g, b;

        /*
           My desktop PC runs this in ~3.342s, which is SUSPICIOUSLY close to
           30FPS.

           It might be locked to my screen's refresh rate?

           */
        for (int t = 0; t < 100; t++) {
                fh = fopen("/dev/fb0", "wb");
                for (int y = 0; y < height; y++) {
                        for (int x = 0; x < width; x++) {
                                g = 0x00;
                                b = (y + t * 10) % 0xff;
                                r = (x + t * 10) % 0xff;
                                fputc(b, fh);
                                fputc(g, fh);
                                fputc(r, fh);
                                fputc(0x00, fh);
                        }
                }
                fclose(fh);
        }
}

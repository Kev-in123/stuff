#include <iostream>
#include <cmath>
#include <string.h>

int main() {
    float A = 0;
    float B = 0;
    float i;
    float j;
    float z[1760];
    char b[1760];
    std::cout << "\x1b[2J";
    while (true) {
        memset(b, 32, 1760);
        memset(z, 0, 7040);
        for (j = 0; j < 6.28; j += 0.07) {
            for (i = 0; i < 6.28; i += 0.02) {
                float c = sin(i);
                float d = cos(j);
                float e = sin(A);
                float f = sin(j);
                float g = cos(A);
                float h = d + 2;
                float D = 1 / (c * h * e + f * g + 5);
                float l = cos(i);
                float m = cos(B);
                float n = sin(B);
                float t = c * h * g - f * e;
                int x = 40 + 30 * D * (l * h * m - t * n);
                int y = 12 + 15 * D * (l * h * n + t * m);
                int o = x + 80 * y;
                int N = 8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n);
                if (0 < y && y < 22 && 0 < x && x < 80 && z[o] < D) {
                    z[o] = D;
                    b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
                }
            }
        }
        std::cout << "\x1b[H";
        for (int k = 0; k < 1761; k++) {
            putchar(k % 80 ? b[k] : 10);
        }
        A += 0.04;
        B += 0.02;
    }
}

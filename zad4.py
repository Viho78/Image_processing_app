import cv2
import numpy as np
import math
import struct

class zad4():
# ---------------------------------4.1----------------------------------przemieszczanie obrazu o wektor
    def zad4_1(self, px1, px2, s1):
        img1 = cv2.imread(s1)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f = image.read()
            b = bytearray(f)

        if b[1] != 80 or b[2] != 78 or b[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b[12] != 73 or b[13] != 72 or b[14] != 68 or b[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b[16:20])[0]
        height1 = struct.unpack('>L', b[20:24])[0]
        channel1 = len(img1[0][0])
        px1 = px1 * -1
        pom = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    if height1 > i + px1 > 0 and width1 > j + px2 > 0:
                        pom[i + px1, j + px2, c] = img1[i, j, c]

        cv2.imwrite('img4.1(gotowy).png', pom)

# ---------------------------------4.2----------------------------------skalowanie obrazu
    def zad4_2(self, s1, wsp1, wsp2):
        img1 = cv2.imread(s1)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f = image.read()
            b = bytearray(f)

        if b[1] != 80 or b[2] != 78 or b[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b[12] != 73 or b[13] != 72 or b[14] != 68 or b[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b[16:20])[0]
        height1 = struct.unpack('>L', b[20:24])[0]
        channel1 = len(img1[0][0])

        pom = np.array([[[0 for x in range(channel1)] for y in range(abs(int(width1 * wsp1)))] for g in range(abs(int(height1 * wsp2)))])

        for a in range(abs(int(height1 * wsp2))):
            for b in range(abs(int(width1 * wsp1))):
                for c in range(channel1):
                    if int(width1) > abs(int(b / wsp1)) >= 0 and int(height1) > abs(int(a / wsp2)) >= 0:
                        pom[a, b, c] = img1[abs(int(a / wsp2)), abs(int(b / wsp1)), c]

        cv2.imwrite('img4.2(gotowy).png', pom)
        return pom

# ---------------------------------4.3----------------------------------obracanie obrazu o kat
    def zad4_3(self, s1, kat):
        img1 = cv2.imread(s1)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f = image.read()
            b = bytearray(f)

        if b[1] != 80 or b[2] != 78 or b[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b[12] != 73 or b[13] != 72 or b[14] != 68 or b[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b[16:20])[0]
        height1 = struct.unpack('>L', b[20:24])[0]
        channel1 = len(img1[0][0])

        pom = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        pom.fill(-1)
        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    y2 = int(a * math.sin(kat) + b * math.cos(kat))
                    x2 = int(a * math.cos(kat) - b * math.sin(kat))
                    if width1 >= x2 > 0 and height1 >= y2 > 0:
                        pom[y2-1, x2-1, c-1] = img1[a-1, b-1, c-1]


        #interpolacja - sąsiad
        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    if pom[a, b, c] == -1:
                        if a < height1 - 1:
                            pom[a, b, c] = pom[a + 1, b, c]
                        else:
                            pom[a, b, c] = pom[a - 1, b, c]
                        if pom[a, b, c] == -1:
                            pom[a, b, c] = 0


        cv2.imwrite('img4.3(gotowy).png', pom)

# ---------------------------------4.4.1----------------------------------symetria wzgledem osi ukladu
    def zad4_4_1(self, s1):
        img1 = cv2.imread(s1)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f = image.read()
            b = bytearray(f)

        if b[1] != 80 or b[2] != 78 or b[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b[12] != 73 or b[13] != 72 or b[14] != 68 or b[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b[16:20])[0]
        height1 = struct.unpack('>L', b[20:24])[0]
        channel1 = len(img1[0][0])

        pom = np.array([[[0 for x in range(channel1)] for y in range(width1*2)] for g in range(height1*2)])
        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    y = a - height1
                    y2 = height1 - y
                    x = b - width1
                    x2 = width1 - x
                    pom[y2-1, x2-1, c] = img1[a, b, c]

        pom2 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        for a in range(height1*2):
            for b in range(width1*2):
                for c in range(channel1):
                    if a >= height1 > 0 and b >= width1 > 0:
                        pom2[a - height1, b - width1, c] = pom[a, b, c]

        cv2.imwrite('img4.4.1(gotowy).png', pom2)

# ---------------------------------4.4.2----------------------------------symetria wzgledem zadanej prostej
    def zad4_4_2(self, s1, linia):
        img1 = cv2.imread(s1)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f = image.read()
            b = bytearray(f)

        if b[1] != 80 or b[2] != 78 or b[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b[12] != 73 or b[13] != 72 or b[14] != 68 or b[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b[16:20])[0]
        height1 = struct.unpack('>L', b[20:24])[0]
        channel1 = len(img1[0][0])

        pom = np.array([[[0 for x in range(channel1)] for y in range(linia * 2)] for g in range(height1)])
        for a in range(height1):
            for b in range(linia*2):
                for c in range(channel1):
                    if b >= linia:
                        pom[a, b, c] = img1[a, linia * 2 - b, c]
                    else:
                        pom[a, b, c] = img1[a, b, c]

        cv2.imwrite('img4.4.2(gotowy).png', pom)

# ---------------------------------4.5----------------------------------wycinanie fragmentu obrazu
    def zad4_5(self, s1, x, y, x2, y2):
        img1 = cv2.imread(s1)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f = image.read()
            b = bytearray(f)

        if b[1] != 80 or b[2] != 78 or b[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b[12] != 73 or b[13] != 72 or b[14] != 68 or b[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b[16:20])[0]
        height1 = struct.unpack('>L', b[20:24])[0]
        channel1 = len(img1[0][0])

        y = abs(y - height1)
        y2 = abs(y2 - height1)

        if x < 0 or x > width1 or x2 < 0 or x2 > width1 or y < 0 or y > height1 or y2 < 0 or y2 > height1:
            print("wymiary wychodza poza obraz")
            return 0

        pom = np.array([[[0 for o in range(channel1)] for p in range(width1)] for g in range(height1)])
        for a in range(height1):
            for b in range(width1):
                if a > y2 and a < y and b > x and b < x2:
                    f = 0
                else:
                    for v in range(channel1):
                        pom[a, b, v] = img1[a, b, v]

        cv2.imwrite('img4.5(gotowy).png', pom)

# ---------------------------------4.6----------------------------------kopiowanie fragmentu obrazu
    def zad4_6(self, s1, x, y, x2, y2):
        img1 = cv2.imread(s1)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f = image.read()
            b = bytearray(f)

        if b[1] != 80 or b[2] != 78 or b[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b[12] != 73 or b[13] != 72 or b[14] != 68 or b[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b[16:20])[0]
        height1 = struct.unpack('>L', b[20:24])[0]
        channel1 = len(img1[0][0])

        y = abs(y - height1)
        y2 = abs(y2 - height1)

        if x < 0 or x > width1 or x2 < 0 or x2 > width1 or y < 0 or y > height1 or y2 < 0 or y2 > height1:
            print("wymiary wychodza poza obraz")
            return 0

        pom = np.array([[[0 for o in range(channel1)] for p in range(width1)] for g in range(height1)])
        for a in range(height1):
            for b in range(width1):
                if a > y2 and a < y and b > x and b < x2:
                    for v in range(channel1):
                        pom[a, b, v] = img1[a, b, v]

        pom2 = np.array([[[0 for k in range(channel1)] for l in range(x2 - x)] for m in range(y - y2)])
        for a in range(y - y2):
            for b in range(x2 - x):
                for c in range(channel1):
                    pom2[a, b, c] = pom[a + y2+1, b + x+1, c]

        cv2.imwrite('img4.6(gotowy).png', pom2)
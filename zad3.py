import cv2
import numpy as np
import math
import mainpyth
import struct

class zad3():
# ---------------------------------3.1.1----------------------------------sumowanie dwoch obrazów barwowych
    def zad3_1_1(self, s1, s2):
        img1 = cv2.imread(s1)
        img2 = cv2.imread(s2)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f1 = image.read()
            b1 = bytearray(f1)
        with open(s2, "rb") as image:
            f2 = image.read()
            b2 = bytearray(f2)

        if b1[1] != 80 or b1[2] != 78 or b1[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b1[12] != 73 or b1[13] != 72 or b1[14] != 68 or b1[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()
        if b2[1] != 80 or b2[2] != 78 or b2[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b2[12] != 73 or b2[13] != 72 or b2[14] != 68 or b2[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b1[16:20])[0]
        height1 = struct.unpack('>L', b1[20:24])[0]
        channel1 = len(img1[0][0])
        width2 = struct.unpack('>L', b2[16:20])[0]
        height2 = struct.unpack('>L', b2[20:24])[0]
        channel2 = len(img1[0][0])

        if (height1 < height2):
            dsize = (width1, height1)
            img2 = cv2.resize(img2, dsize)
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape
        else:
            dsize = (width2, height2)
            img3 = img2
            img2 = cv2.resize(img1, dsize)
            img1 = img3
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape

        b3 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    b3[i][j][c] = img1[i][j][c] + img2[i][j][c]
                    bpom = int(img1[i][j][c]) + int(img2[i][j][c])
                    if bpom > 255:
                        Q = bpom
                        D = Q - 255
                        X = int((D / 255))
                        b3[i][j][c] = img1[i][j][c] - (img1[i][j][c] * X) + img2[i][j][c] - (img2[i][j][c] * X)

        b3 = mainpyth.Normalizacja(b3, height1, width1, channel1)

        cv2.imwrite('img3.1.1(gotowy).png', b3)

# ---------------------------------3.1.2----------------------------------sumowanie obrazu barwowego ze stala
    def zad3_1_2(self, s1, stala):
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

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    pom[i][j][c] = img1[i][j][c] + stala
                    bpom = int(img1[i][j][c]) + stala
                    if bpom > 255:
                        Q = bpom
                        D = Q - 255
                        X = int((D / 255))
                        pom[i][j][c] = img1[i][j][c] - (img1[i][j][c] * X) + stala - (stala * X)

        pom = mainpyth.Normalizacja(pom, height1, width1, channel1)
        cv2.imwrite('img3.1.2(gotowy).png', pom)

# ---------------------------------3.1.3----------------------------------odejmowanie dwoch obrazów barwowych
    def zad3_1_3(self, s1, s2):
        img1 = cv2.imread(s1)
        img2 = cv2.imread(s2)

        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f1 = image.read()
            b1 = bytearray(f1)
        with open(s2, "rb") as image:
            f2 = image.read()
            b2 = bytearray(f2)

        if b1[1] != 80 or b1[2] != 78 or b1[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b1[12] != 73 or b1[13] != 72 or b1[14] != 68 or b1[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()
        if b2[1] != 80 or b2[2] != 78 or b2[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b2[12] != 73 or b2[13] != 72 or b2[14] != 68 or b2[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b1[16:20])[0]
        height1 = struct.unpack('>L', b1[20:24])[0]
        channel1 = len(img1[0][0])
        width2 = struct.unpack('>L', b2[16:20])[0]
        height2 = struct.unpack('>L', b2[20:24])[0]
        channel2 = len(img1[0][0])

        if (height1 < height2):
            dsize = (width1, height1)
            img2 = cv2.resize(img2, dsize)
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape
        else:
            dsize = (width2, height2)
            img3 = img2
            img2 = cv2.resize(img1, dsize)
            img1 = img3
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape

        b3 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    b3[i][j][c] = img1[i][j][c] - img2[i][j][c]
                    bpom = int(img1[i][j][c]) - int(img2[i][j][c])
                    if bpom > 255:
                        Q = bpom
                        D = Q - 255
                        X = int((D / 255))
                        b3[i][j][c] = img1[i][j][c] - (img1[i][j][c] * X) + img2[i][j][c] - (img2[i][j][c] * X)

        b3 = mainpyth.Normalizacja(b3, height1, width1, channel1)
        cv2.imwrite('img3.1.3(gotowy).png', b3)

# ---------------------------------3.1.4----------------------------------odejmowanie obrazu barwowego ze stala
    def zad3_1_4(self, s1, stala):
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

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    pom[i][j][c] = img1[i][j][c] - stala
                    bpom = int(img1[i][j][c]) - stala
                    if bpom > 255:
                        Q = bpom
                        D = Q - 255
                        X = int((D / 255))
                        pom[i][j][c] = img1[i][j][c] - (img1[i][j][c] * X) + stala - (stala * X)

        pom = mainpyth.Normalizacja(pom, height1, width1, channel1)
        cv2.imwrite('img3.1.4(gotowy).png', pom)

# ---------------------------------3.2.1----------------------------------mnozenie dwoch obrazow barwowych
    def zad3_2_1(self, s1, s2):
        img1 = cv2.imread(s1)
        img2 = cv2.imread(s2)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f1 = image.read()
            b1 = bytearray(f1)
        with open(s2, "rb") as image:
            f2 = image.read()
            b2 = bytearray(f2)

        if b1[1] != 80 or b1[2] != 78 or b1[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b1[12] != 73 or b1[13] != 72 or b1[14] != 68 or b1[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()
        if b2[1] != 80 or b2[2] != 78 or b2[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b2[12] != 73 or b2[13] != 72 or b2[14] != 68 or b2[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b1[16:20])[0]
        height1 = struct.unpack('>L', b1[20:24])[0]
        channel1 = len(img1[0][0])
        width2 = struct.unpack('>L', b2[16:20])[0]
        height2 = struct.unpack('>L', b2[20:24])[0]
        channel2 = len(img1[0][0])

        if (height1 < height2):
            dsize = (width1, height1)
            img2 = cv2.resize(img2, dsize)
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape
        else:
            dsize = (width2, height2)
            img3 = img2
            img2 = cv2.resize(img1, dsize)
            img1 = img3
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape

        b3 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    if img1[i][j][c] == 255:
                        b3[i][j][c] = img2[i][j][c]
                    elif img1[i][j][c] == 0:
                        b3[i][j][c] = 0
                    else:
                        b3[i][j][c] = math.ceil(int(img1[i][j][c]) * int(img2[i][j][c]) / 256)

        b3 = mainpyth.Normalizacja(b3, height1, width1, channel1)
        cv2.imwrite('img3.2.1(gotowy).png', b3)

# ---------------------------------3.2.2----------------------------------mnozenie obrazu barwowego przez stala
    def zad3_2_2(self,s1,  stala):
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

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    if img1[i][j][c] == 255:
                        pom[i][j][c] = stala
                    elif img1[i][j][c] == 0:
                        pom[i][j][c] = 0
                    else:
                        pom[i][j][c] = math.ceil(int(img1[i][j][c]) * stala / 256)

        pom = mainpyth.Normalizacja(pom, height1, width1, channel1)
        cv2.imwrite('img3.2.2(gotowy).png', pom)

# ---------------------------------3.3----------------------------------mieszanie obrazow barwowych z wspolczynnikiem
    def zad3_3(self, s1, s2, wsp):
        img1 = cv2.imread(s1)
        img2 = cv2.imread(s2)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f1 = image.read()
            b1 = bytearray(f1)
        with open(s2, "rb") as image:
            f2 = image.read()
            b2 = bytearray(f2)

        if b1[1] != 80 or b1[2] != 78 or b1[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b1[12] != 73 or b1[13] != 72 or b1[14] != 68 or b1[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()
        if b2[1] != 80 or b2[2] != 78 or b2[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b2[12] != 73 or b2[13] != 72 or b2[14] != 68 or b2[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b1[16:20])[0]
        height1 = struct.unpack('>L', b1[20:24])[0]
        channel1 = len(img1[0][0])
        width2 = struct.unpack('>L', b2[16:20])[0]
        height2 = struct.unpack('>L', b2[20:24])[0]
        channel2 = len(img1[0][0])

        if (height1 < height2):
            dsize = (width1, height1)
            img2 = cv2.resize(img2, dsize)
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape
        else:
            dsize = (width2, height2)
            img3 = img2
            img2 = cv2.resize(img1, dsize)
            img1 = img3
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape

        b3 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    b3[i, j, c] = int(wsp * img1[i, j, c] + (1 - wsp) * img2[i, j, c])

        b3 = mainpyth.Normalizacja(b3, height1, width1, channel1)

        cv2.imwrite('img3.3(gotowy).png', b3)

# ---------------------------------3.4----------------------------------potegowanie obrazu barwowego
    def zad3_4(self, s1, potega):
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

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    pom[i][j][c] = math.ceil(pow(int(img1[i][j][c]), potega))

        pom = mainpyth.Normalizacja(pom, height1, width1, channel1)
        cv2.imwrite('img3.4(gotowy).png', pom)

# ---------------------------------3.5.1----------------------------------dzielenie dwoch obrazow barwowych
    def zad3_5_1(self, s1, s2):
        img1 = cv2.imread(s1)
        img2 = cv2.imread(s2)
        # Czytanie wys i szerokosci
        with open(s1, "rb") as image:
            f1 = image.read()
            b1 = bytearray(f1)
        with open(s2, "rb") as image:
            f2 = image.read()
            b2 = bytearray(f2)

        if b1[1] != 80 or b1[2] != 78 or b1[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b1[12] != 73 or b1[13] != 72 or b1[14] != 68 or b1[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()
        if b2[1] != 80 or b2[2] != 78 or b2[3] != 71:
            print("obraz nie jest typu PNG")
            exit()
        if b2[12] != 73 or b2[13] != 72 or b2[14] != 68 or b2[15] != 82:
            print("obraz nie jest typu IHDR")
            exit()

        width1 = struct.unpack('>L', b1[16:20])[0]
        height1 = struct.unpack('>L', b1[20:24])[0]
        channel1 = len(img1[0][0])
        width2 = struct.unpack('>L', b2[16:20])[0]
        height2 = struct.unpack('>L', b2[20:24])[0]
        channel2 = len(img1[0][0])

        if (height1 < height2):
            dsize = (width1, height1)
            img2 = cv2.resize(img2, dsize)
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape
        else:
            dsize = (width2, height2)
            img3 = img2
            img2 = cv2.resize(img1, dsize)
            img1 = img3
            height1, width1, channels1 = img1.shape
            height2, width2, channels2 = img2.shape

        b3 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    bpom = int(img1[i][j][c]) + int(img2[i][j][c])
                    Q = bpom + 1
                    b3[i][j][c] = int((bpom * 255) / Q)

        b3 = mainpyth.Normalizacja(b3, height1, width1, channel1)
        cv2.imwrite('img3.5.1(gotowy).png', b3)

# ---------------------------------3.5.2----------------------------------dzielenie obrazu barwowego przez stala
    def zad3_5_2(self, s1, stala):
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

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    bpom = int(img1[i, j, c]) + stala
                    Q = bpom + 1
                    pom[i, j, c] = int((bpom * 255) / Q)

        pom = mainpyth.Normalizacja(pom, height1, width1, channel1)
        cv2.imwrite('img3.5.2(gotowy).png', pom)

# ---------------------------------3.6----------------------------------pierwiastkowanie obrazu barwowego
    def zad3_6(self,s1, potega):
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

        b3 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    b3[i][j][c] = math.ceil(pow(int(img1[i][j][c]), potega))

        b3 = mainpyth.Normalizacja(b3, height1, width1, channel1)
        cv2.imwrite('img3.6(gotowy).png', b3)

# ---------------------------------3.7----------------------------------logarytmowanie obrazu barwowego
    def zad3_7(self, s1):
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

        b3 = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])

        for i in range(height1):
            for j in range(width1):
                for c in range(channel1):
                    b3[i][j][c] = math.log10(1 + img1[i,j,c])

        b3 = mainpyth.Normalizacja(b3, height1, width1, channel1)
        cv2.imwrite('img3.7(gotowy).png', b3)
import cv2
import numpy as np
import math
import mainpyth
import struct
import zad4

class zad1():
# ---------------------------------1.1----------------------------------ujednolicenie dwoch obrazów szarych - geometryczne
    def zad1_1(self, s1, s2):
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
        channel2 = len(img2[0][0])

        x = 0

        if height1 <= height2 and width1 <= width2:
            pom = np.array([[[0 for x in range(channel2)] for y in range(width2)] for g in range(height2)])
            for a in range(height2):
                for b in range(width2):
                    for c in range(channel2):
                        if a <= height1 and b <= width1:
                            pom[a, b, c] = img1[a-1, b-1, c]
                        else:
                            pom[a, b, c] = 1
            cv2.imwrite('img1.1(gotowy).png', pom)
        elif height1 >= height2 and width1 >= width2:
            pom = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
            for a in range(height1):
                for b in range(width1):
                    for c in range(channel1):
                        if a <= height2 and b <= width2:
                            pom[a, b, c] = img2[a-1, b-1, c]
                        else:
                            pom[a, b, c] = 1
            cv2.imwrite('img1.1(gotowy).png', pom)
        elif height1 >= height2 and width1 <= width2:
            max_wys = max(height1, height2)
            max_szer = max(width1, width2)
            pom1 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            pom2 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            for a in range(max_wys):
                for b in range(max_szer):
                    for c in range(channel1):
                        if a <= height2 and b <= width2:
                            pom2[a, b, c] = img2[a-1, b-1, c]
                        else:
                            pom2[a , b , c ] = 1
                        if a <= height1 and b <= width1:
                            pom1[a, b, c] = img1[a-1, b-1, c]
                        else:
                            pom1[a - 1, b - 1, c - 1] = 1
            cv2.imwrite('img1.1-1(gotowy).png', pom1)
            cv2.imwrite('img1.1-2(gotowy).png', pom2)
            x = 1
        elif height1 <= height2 and width1 >= width2:
            max_wys = max(height1, height2)
            max_szer = max(width1, width2)
            pom1 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            pom2 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            for a in range(max_wys):
                for b in range(max_szer):
                    for c in range(channel1):
                        if a <= height2 and b <= width2:
                            pom2[a , b , c ] = img2[a -1, b -1, c]
                        else:
                            pom2[a , b , c ] = 1
                        if a <= height1 and b <= width1:
                            pom1[a , b , c ] = img1[a -1, b -1, c]
                        else:
                            pom1[a, b, c ] = 1
            cv2.imwrite('img1.1-1(gotowy).png', pom1)
            cv2.imwrite('img1.1-2(gotowy).png', pom2)
            x = 1
        return x

# ---------------------------------1.3----------------------------------ujednolicenie dwoch obrazów barwowych - geometryczne
    def zad1_3(self, s1, s2):
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
        channel2 = len(img2[0][0])

        x = 0

        if height1 <= height2 and width1 <= width2:
            pom = np.array([[[0 for x in range(channel2)] for y in range(width2)] for g in range(height2)])
            for a in range(height2):
                for b in range(width2):
                    for c in range(channel2):
                        if a <= height1 and b <= width1:
                            pom[a, b, c] = img1[a - 1, b - 1, c]
                        else:
                            pom[a, b, c] = 1
            cv2.imwrite('img1.3(gotowy).png', pom)
        elif height1 >= height2 and width1 >= width2:
            pom = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
            for a in range(height1):
                for b in range(width1):
                    for c in range(channel1):
                        if a <= height2 and b <= width2:
                            pom[a, b, c] = img2[a - 1, b - 1, c]
                        else:
                            pom[a, b, c] = 1
            cv2.imwrite('img1.3(gotowy).png', pom)
        elif height1 >= height2 and width1 <= width2:
            max_wys = max(height1, height2)
            max_szer = max(width1, width2)
            pom1 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            pom2 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            for a in range(max_wys):
                for b in range(max_szer):
                    for c in range(channel1):
                        if a <= height2 and b <= width2:
                            pom2[a, b, c] = img2[a - 1, b - 1, c]
                        else:
                            pom2[a, b, c] = 1
                        if a <= height1 and b <= width1:
                            pom1[a, b, c] = img1[a - 1, b - 1, c]
                        else:
                            pom1[a - 1, b - 1, c - 1] = 1
            cv2.imwrite('img1.3-1(gotowy).png', pom1)
            cv2.imwrite('img1.3-2(gotowy).png', pom2)
            x = 1
        elif height1 <= height2 and width1 >= width2:
            max_wys = max(height1, height2)
            max_szer = max(width1, width2)
            pom1 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            pom2 = np.array([[[0 for x in range(channel2)] for y in range(max_szer)] for g in range(max_wys)])
            for a in range(max_wys):
                for b in range(max_szer):
                    for c in range(channel1):
                        if a <= height2 and b <= width2:
                            pom2[a, b, c] = img2[a - 1, b - 1, c]
                        else:
                            pom2[a, b, c] = 1
                        if a <= height1 and b <= width1:
                            pom1[a, b, c] = img1[a - 1, b - 1, c]
                        else:
                            pom1[a, b, c] = 1
            cv2.imwrite('img1.3-1(gotowy).png', pom1)
            cv2.imwrite('img1.3-2(gotowy).png', pom2)
            x = 1
        return x

# ---------------------------------1.2----------------------------------ujednolicenie dwoch obrazów szarych - rozdzielczosciowe
    def zad1_2(self, s1, s2):
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
        channel2 = len(img2[0][0])

        clas4 = zad4.zad4()
        x = 0

        if height1 <= height2 and width1 <= width2:  #img1 jest mniejszy
            wspy = height2/height1
            wspx = width2/width1
            cv2.imwrite('pom.png', img1)
            pom = clas4.zad4_2('pom.png', wspx, wspy)
            cv2.imwrite('img1.2(gotowy).png', pom)

        elif height1 >= height2 and width1 >= width2:  #img2 jest mniejszy
            wspy = height1 / height2
            wspx = width1 / width2
            cv2.imwrite('pom.png', img2)
            pom = clas4.zad4_2('pom.png', wspx, wspy)
            cv2.imwrite('img1.2(gotowy).png', pom)

        elif height1 >= height2 and width1 <= width2:
            wspy = height1 / height2
            wspx = width2 / width1
            cv2.imwrite('pom1.png', img1)
            cv2.imwrite('pom2.png', img2)
            pom1 = clas4.zad4_2('pom1.png', wspx, 1)
            pom2 = clas4.zad4_2('pom2.png', 1, wspy)
            cv2.imwrite('img1.2-1(gotowy).png', pom1)
            cv2.imwrite('img1.2-2(gotowy).png', pom2)
            x = 1

        elif height1 <= height2 and width1 >= width2:
            wspy = height2 / height1
            wspx = width1 / width2
            cv2.imwrite('pom1.png', img1)
            cv2.imwrite('pom2.png', img2)
            pom1 = clas4.zad4_2('pom1.png', 1, wspy)
            pom2 = clas4.zad4_2('pom2.png', wspx, 1)
            cv2.imwrite('img1.2-1(gotowy).png', pom1)
            cv2.imwrite('img1.2-2(gotowy).png', pom2)
            x = 1
        return x

# ---------------------------------1.4----------------------------------ujednolicenie dwoch obrazów barwowych - rozdzielczosciowe
    def zad1_4(self, s1, s2):
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
        channel2 = len(img2[0][0])

        clas4 = zad4.zad4()
        x = 0

        if height1 <= height2 and width1 <= width2:  #img1 jest mniejszy
            wspy = height2/height1
            wspx = width2/width1
            cv2.imwrite('pom.png', img1)
            pom = clas4.zad4_2('pom.png', wspx, wspy)
            cv2.imwrite('img1.4(gotowy).png', pom)

        elif height1 >= height2 and width1 >= width2:  #img2 jest mniejszy
            wspy = height1 / height2
            wspx = width1 / width2
            cv2.imwrite('pom.png', img2)
            pom = clas4.zad4_2('pom.png', wspx, wspy)
            cv2.imwrite('img1.4(gotowy).png', pom)

        elif height1 >= height2 and width1 <= width2:
            wspy = height1 / height2
            wspx = width2 / width1
            cv2.imwrite('pom1.png', img1)
            cv2.imwrite('pom2.png', img2)
            pom1 = clas4.zad4_2('pom1.png', wspx, 1)
            pom2 = clas4.zad4_2('pom2.png', 1, wspy)
            cv2.imwrite('img1.4-1(gotowy).png', pom1)
            cv2.imwrite('img1.4-2(gotowy).png', pom2)
            x = 1

        elif height1 <= height2 and width1 >= width2:
            wspy = height2 / height1
            wspx = width1 / width2
            cv2.imwrite('pom1.png', img1)
            cv2.imwrite('pom2.png', img2)
            pom1 = clas4.zad4_2('pom1.png', 1, wspy)
            pom2 = clas4.zad4_2('pom2.png', wspx, 1)
            cv2.imwrite('img1.4-1(gotowy).png', pom1)
            cv2.imwrite('img1.4-2(gotowy).png', pom2)
            x = 1
        return x
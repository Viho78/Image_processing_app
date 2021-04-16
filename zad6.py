import cv2
import numpy as np
import struct
import mainpyth
import matplotlib.pyplot as plt


class zad6():
# ---------------------------------6.1----------------------------------tworzenie histogramu barwowy
    def zad6_1(self, s1):
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

        # podział na RGB
        b1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        g1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        r1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    if c == 0:
                        b1[a, b] = img1[a, b, c]
                    if c == 1:
                        g1[a, b] = img1[a, b, c]
                    if c == 2:
                        r1[a, b] = img1[a, b, c]


        uniqueB, countsB = np.unique(b1, return_counts=True)
        uniqueG, countsG = np.unique(g1, return_counts=True)
        uniqueR, countsR = np.unique(r1, return_counts=True)

        for i in range(len(countsB)):
            countsB[i] = int(int(countsB[i])/50)
        for i in range(len(countsG)):
            countsG[i] = int(int(countsG[i])/50)
        for i in range(len(countsR)):
            countsR[i] = int(int(countsR[i])/50)

        maxim = max(max(countsB), max(countsG), max(countsR))  #szerokosc wykresu

        xB = np.zeros((255, maxim))
        xG = np.zeros((255, maxim))
        xR = np.zeros((255, maxim))

        x = 0
        for i in range(255):
            if int(uniqueB[x]) == i:
                for j in range(countsB[x]):
                    xB[i, j] = 255
                x += 1
            else:
                xB[i, 0] = 0
            if len(uniqueB) == x:
                break

        x = 0
        for i in range(255):
            if uniqueG[x] == i:
                for j in range(countsG[x]):
                    xG[i, j] = 255
                x += 1
            else:
                xG[i, 0] = 0
            if len(uniqueG) == x:
                break

        x = 0
        for i in range(255):
            if uniqueR[x] == i:
                for j in range(countsR[x]):
                    xR[i, j] = 255
                x += 1
            else:
                xR[i, 0] = 0
            if len(uniqueR) == x:
                break

        xB = np.rot90(xB)
        xG = np.rot90(xG)
        xR = np.rot90(xR)

        pom = np.array([[[0 for x in range(channel1)] for y in range(255)] for g in range(maxim)])

        #merge
        for a in range(maxim):
            for b in range(255):
                pom[a, b, 0] = xB[a, b]

        for a in range(maxim):
            for b in range(255):
                pom[a, b, 1] = xG[a, b]

        for a in range(maxim):
            for b in range(255):
                pom[a, b, 2] = xR[a, b]


        cv2.imwrite('img6.1(gotowy).png', pom)
        plt.plot(uniqueB, countsB, color='b')
        plt.plot(uniqueG, countsG, color='g')
        plt.plot(uniqueR, countsR, color='r')
        plt.show()

# ---------------------------------6.2----------------------------------przemieszczanie histogramu barwowy
    def zad6_2(self, s1, wart):
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

        # podział na RGB
        b1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        g1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        r1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                if img1[a, b, 0] + wart < 0:
                    b1[a, b] = 0
                elif img1[a, b, 0] + wart > 255:
                    b1[a, b] = 255
                else:
                    b1[a, b] = img1[a, b, 0] + wart

                if img1[a, b, 1] + wart < 0:
                    g1[a, b] = 0
                elif img1[a, b, 1] + wart > 255:
                    g1[a, b] = 255
                else:
                    g1[a, b] = img1[a, b, 1] + wart

                if img1[a, b, 2] + wart < 0:
                    r1[a, b] = 0
                elif img1[a, b, 2] + wart > 255:
                    r1[a, b] = 255
                else:
                    r1[a, b] = img1[a, b, 2] + wart


        uniqueB, countsB = np.unique(b1, return_counts=True)
        uniqueG, countsG = np.unique(g1, return_counts=True)
        uniqueR, countsR = np.unique(r1, return_counts=True)

        dlgB = 0
        dlgG = 0
        dlgR = 0

        for i in range(len(countsB)):
            countsB[i] = int(int(countsB[i])/50)
            dlgB = i
        for i in range(len(countsG)):
            countsG[i] = int(int(countsG[i])/50)
            dlgG = i
        for i in range(len(countsR)):
            countsR[i] = int(int(countsR[i])/50)
            dlgR = i

        countsB2 = np.asarray(countsB)
        countsG2 = np.asarray(countsG)
        countsR2 = np.asarray(countsR)
        countsB = np.zeros(dlgB)
        countsG = np.zeros(dlgG)
        countsR = np.zeros(dlgR)
        uniqueB2 = np.asarray(uniqueB)
        uniqueG2 = np.asarray(uniqueG)
        uniqueR2 = np.asarray(uniqueR)
        uniqueB = np.zeros(dlgB)
        uniqueG = np.zeros(dlgG)
        uniqueR = np.zeros(dlgR)

        for i in range(dlgB):
            countsB[i] = countsB2[i]
            uniqueB[i] = uniqueB2[i]
        for i in range(dlgG):
            countsG[i] = countsG2[i]
            uniqueG[i] = uniqueG2[i]
        for i in range(dlgR):
            countsR[i] = countsR2[i]
            uniqueR[i] = uniqueR2[i]

        maxim = int(max(max(countsB), max(countsG), max(countsR)))  #szerokosc wykresu

        xB = np.zeros((255, maxim))
        xG = np.zeros((255, maxim))
        xR = np.zeros((255, maxim))

        x = 0
        for i in range(255):
            if int(uniqueB[x]) == i:
                for j in range(int(countsB[x])):
                    xB[i, j] = 255
                x += 1
            else:
                xB[i, 0] = 0
            if len(uniqueB) == x:
                break

        x = 0
        for i in range(255):
            if uniqueG[x] == i:
                for j in range(int(countsG[x])):
                    xG[i, j] = 255
                x += 1
            else:
                xG[i, 0] = 0
            if len(uniqueG) == x:
                break

        x = 0
        for i in range(255):
            if uniqueR[x] == i:
                for j in range(int(countsR[x])):
                    xR[i, j] = 255
                x += 1
            else:
                xR[i, 0] = 0
            if len(uniqueR) == x:
                break

        xB = np.rot90(xB)
        xG = np.rot90(xG)
        xR = np.rot90(xR)

        pom = np.array([[[0 for x in range(channel1)] for y in range(255)] for g in range(maxim)])

        #merge
        for a in range(maxim):
            for b in range(255):
                pom[a, b, 0] = xB[a, b]

        for a in range(maxim):
            for b in range(255):
                pom[a, b, 1] = xG[a, b]

        for a in range(maxim):
            for b in range(255):
                pom[a, b, 2] = xR[a, b]


        cv2.imwrite('img6.2(gotowy).png', pom)

        plt.plot(uniqueB, countsB, color='b')
        plt.plot(uniqueG, countsG, color='g')
        plt.plot(uniqueR, countsR, color='r')
        plt.show()

# ---------------------------------6.3----------------------------------rozciaganie histogramu barwowy
    def zad6_3(self, s1):
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

        maxwart = np.amax(img1)
        minwart = np.amin(img1)

        pom = np.array([[[0 for x in range(channel1)] for y in range(width1)] for g in range(height1)])
        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    if img1[a, b, c] < minwart:
                        pom[a, b, c] = 0
                    elif img1[a, b, c] > maxwart:
                        pom[a, b, c] = 255
                    else:
                        pom[a, b, c] = ((img1[a, b, c] - minwart) * 255) / (maxwart - minwart)

        maxwart = np.amax(pom)
        minwart = np.amin(pom)

        # podział na RGB
        b1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        g1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        r1 = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    if c == 0:
                        b1[a, b] = pom[a, b, c]
                    if c == 1:
                        g1[a, b] = pom[a, b, c]
                    if c == 2:
                        r1[a, b] = pom[a, b, c]


        uniqueB, countsB = np.unique(b1, return_counts=True)
        uniqueG, countsG = np.unique(g1, return_counts=True)
        uniqueR, countsR = np.unique(r1, return_counts=True)

        for i in range(len(countsB)):
            countsB[i] = int(int(countsB[i])/50)
        for i in range(len(countsG)):
            countsG[i] = int(int(countsG[i])/50)
        for i in range(len(countsR)):
            countsR[i] = int(int(countsR[i])/50)

        maxim = max(max(countsB), max(countsG), max(countsR))  #szerokosc wykresu

        xB = np.zeros((255, maxim))
        xG = np.zeros((255, maxim))
        xR = np.zeros((255, maxim))

        x = 0
        for i in range(255):
            if int(uniqueB[x]) == i:
                for j in range(countsB[x]):
                    xB[i, j] = 255
                x += 1
            else:
                xB[i, 0] = 0
            if len(uniqueB) == x:
                break

        x = 0
        for i in range(255):
            if uniqueG[x] == i:
                for j in range(countsG[x]):
                    xG[i, j] = 255
                x += 1
            else:
                xG[i, 0] = 0
            if len(uniqueG) == x:
                break

        x = 0
        for i in range(255):
            if uniqueR[x] == i:
                for j in range(countsR[x]):
                    xR[i, j] = 255
                x += 1
            else:
                xR[i, 0] = 0
            if len(uniqueR) == x:
                break

        xB = np.rot90(xB)
        xG = np.rot90(xG)
        xR = np.rot90(xR)

        pom = np.array([[[0 for x in range(channel1)] for y in range(255)] for g in range(maxim)])

        # merge
        for a in range(maxim):
            for b in range(255):
                pom[a, b, 0] = xB[a, b]

        for a in range(maxim):
            for b in range(255):
                pom[a, b, 1] = xG[a, b]

        for a in range(maxim):
            for b in range(255):
                pom[a, b, 2] = xR[a, b]


        cv2.imwrite('img6.3(gotowy).png', pom)
        plt.plot(uniqueB, countsB, color='b')
        plt.plot(uniqueG, countsG, color='g')
        plt.plot(uniqueR, countsR, color='r')
        plt.show()

# ---------------------------------6.4----------------------------------progowanie globalne wieloprogowe barwowe
    def zad6_4(self, s1, prog1, prog2, prog3):
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

        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    if img1[a, b, c] < prog1:
                        pom[a, b, c] = 0
                    elif img1[a, b, c] < prog2:
                        pom[a, b, c] = prog1
                    elif img1[a, b, c] < prog3:
                        pom[a, b, c] = prog2
                    else:
                        pom[a, b, c] = prog3

        cv2.imwrite('img6.4(gotowy).png', pom)

# ---------------------------------6.5----------------------------------progowanie lokalne wieloprogowe barwowe
    def zad6_5(self, s1):
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


        for a in range(height1):
            for b in range(width1):
                suma = 0
                counter = 0
                if height1 >= a - 5 >= 0 and height1 >= a + 5 >= 0 and width1 >= b - 5 >= 0 and width1 >= b + 5 >= 0:
                    for i in range(a - 5, a + 5):
                        for j in range(b - 5, b + 5):
                            suma += img1[i, j, 0]
                            counter += 1
                    prog1 = suma / counter
                    prog2 = suma / counter * 2
                    prog3 = suma / counter * 3
                    for c in range(channel1):
                        if img1[a, b, c] < prog1:
                            pom[a, b, c] = 0
                        elif img1[a, b, c] < prog2:
                            pom[a, b, c] = prog1
                        elif img1[a, b, c] < prog3:
                            pom[a, b, c] = prog2
                        else:
                            pom[a, b, c] = prog3
                elif height1 >= a - 5 >= 0 and height1 >= a + 5 >= 0:
                    for i in range(a - 5, a + 5):
                        for j in range(1):
                            suma += img1[i, j, 0]
                            counter += 1
                    prog1 = suma / counter
                    prog2 = suma / counter * 2
                    prog3 = suma / counter * 3
                    for c in range(channel1):
                        if img1[a, b, c] < prog1:
                            pom[a, b, c] = 0
                        elif img1[a, b, c] < prog2:
                            pom[a, b, c] = prog1
                        elif img1[a, b, c] < prog3:
                            pom[a, b, c] = prog2
                        else:
                            pom[a, b, c] = prog3
                elif width1 >= b - 5 >= 0 and width1 >= b + 5 >= 0:
                    for i in range(1):
                        for j in range(b - 5, b + 5):
                            suma += img1[i, j, 0]
                            counter += 1
                    prog1 = suma / counter
                    prog2 = suma / counter * 2
                    prog3 = suma / counter * 3
                    for c in range(channel1):
                        if img1[a, b, c] < prog1:
                            pom[a, b, c] = 0
                        elif img1[a, b, c] < prog2:
                            pom[a, b, c] = prog1
                        elif img1[a, b, c] < prog3:
                            pom[a, b, c] = prog2
                        else:
                            pom[a, b, c] = prog3
        cv2.imwrite('img6.5(gotowy).png', pom)

# ---------------------------------6.6----------------------------------progowanie lokalne jednoprogowe barwowe
    def zad6_6(self, s1):
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


        for a in range(height1):
            for b in range(width1):
                suma = 0
                counter = 0
                if height1 >= a - 5 >= 0 and height1 >= a + 5 >= 0 and width1 >= b - 5 >= 0 and width1 >= b + 5 >= 0:
                    for i in range(a - 5, a + 5):
                        for j in range(b - 5, b + 5):
                            suma += img1[i, j, 0]
                            counter += 1
                    prog = suma / counter
                    for c in range(channel1):
                        if img1[a, b, c] < prog:
                            pom[a, b, c] = 0
                        else:
                            pom[a, b, c] = prog
                elif height1 >= a - 5 >= 0 and height1 >= a + 5 >= 0:
                    for i in range(a - 5, a + 5):
                        for j in range(1):
                            suma += img1[i, j, 0]
                            counter += 1
                    prog = suma / counter
                    for c in range(channel1):
                        if img1[a, b, c] < prog:
                            pom[a, b, c] = 0
                        else:
                            pom[a, b, c] = prog
                elif width1 >= b - 5 >= 0 and width1 >= b + 5 >= 0:
                    for i in range(1):
                        for j in range(b - 5, b + 5):
                            suma += img1[i, j, 0]
                            counter += 1
                    prog = suma / counter
                    for c in range(channel1):
                        if img1[a, b, c] < prog:
                            pom[a, b, c] = 0
                        else:
                            pom[a, b, c] = prog
        cv2.imwrite('img6.6(gotowy).png', pom)

# ---------------------------------6.7----------------------------------progowanie globalne jednoprogowe barwowe
    def zad6_7(self, s1, prog):
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

        for a in range(height1):
            for b in range(width1):
                for c in range(channel1):
                    if img1[a, b, c] < prog:
                        pom[a, b, c] = 0
                    else:
                        pom[a, b, c] = prog

        cv2.imwrite('img6.7(gotowy).png', pom)
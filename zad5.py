import cv2
import numpy as np
import struct
import matplotlib.pyplot as plt

class zad5():
# ---------------------------------5.1----------------------------------tworzenie histogramu czarno bialy
    def zad5_1(self, s1):
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

        pom = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                pom[a,b] = img1[a,b,0]

        unique, counts = np.unique(pom, return_counts=True)

        for i in range(len(counts)):
            counts[i] = int(int(counts[i])/100)

        xB = np.zeros((255, np.max(counts)))

        x = 0
        for i in range(255):
            if int(unique[x]) == i:
                for j in range(int(counts[x])):
                    xB[i, j] = 150
                x += 1
            else:
                xB[i, 0] = 0
            if len(unique) == x:
                break

        xB = np.rot90(xB)

        cv2.imwrite('img5.1(gotowy).png', xB)
        plt.plot(unique, counts, color='k')
        plt.show()

# ---------------------------------5.2----------------------------------przemieszczanie histogramu czarno bialy
    def zad5_2(self, s1, wart):
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

        pom = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                if img1[a, b, 0] + wart < 0:
                    pom[a, b] = 0
                elif img1[a, b, 0] + wart > 255:
                    pom[a, b] = 255
                else:
                    pom[a, b] = img1[a, b, 0] + wart
        cv2.imwrite('img5.2obr(gotowy).png', pom)
        unique, counts = np.unique(pom, return_counts=True)

        for i in range(len(counts)):
            counts[i] = int(int(counts[i])/100)

        xB = np.zeros((255, np.max(counts)))

        x = 0
        for i in range(255):
            if int(unique[x]) == i:
                for j in range(int(counts[x])):
                    xB[i, j] = 150
                x += 1
            else:
                xB[i, 0] = 0
            if len(unique) == x:
                break

        xB = np.rot90(xB)
        cv2.imwrite('img5.2(gotowy).png', xB)
        plt.plot(unique, counts, color='k')
        plt.show()

# ---------------------------------5.3----------------------------------rozciaganie histogramu czarno bialy
    def zad5_3(self, s1):
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

        pom = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                if img1[a, b, 0] < minwart:
                    pom[a, b] = 0
                elif img1[a, b, 0] > maxwart:
                    pom[a, b] = 255
                else:
                    pom[a, b] = ((img1[a, b, 0] - minwart) * 255) / (maxwart - minwart)
        cv2.imwrite('img5.3obr(gotowy).png', pom)
        unique, counts = np.unique(pom, return_counts=True)

        for i in range(len(counts)):
            counts[i] = int(int(counts[i])/100)

        xB = np.zeros((255, np.max(counts)))

        x = 0
        for i in range(255):
            if int(unique[x]) == i:
                for j in range(int(counts[x])):
                    xB[i, j] = 150
                x += 1
            else:
                xB[i, 0] = 0
            if len(unique) == x:
                break

        xB = np.rot90(xB)
        cv2.imwrite('img5.3(gotowy).png', xB)
        plt.plot(unique, counts, color='k')
        plt.show()

# ---------------------------------5.4----------------------------------progowanie lokalne czarno biale
    def zad5_4(self, s1):
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

        pom = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                pom[a, b] = img1[a, b, 0]

        for a in range(height1):
            for b in range(width1):
                suma = 0
                counter = 0
                if height1 >= a - 5 >= 0 and height1 >= a + 5 >= 0 and width1 >= b - 5 >= 0 and width1 >= b + 5 >= 0:
                    for i in range(a - 5, a + 5):
                        for j in range(b - 5, b + 5):
                            suma += pom[i, j]
                            counter += 1
                    prog = suma / counter
                    if pom[a, b] < prog:
                        pom[a, b] = 0
                    else:
                        pom[a, b] = prog
                elif height1 >= a - 5 >= 0 and height1 >= a + 5 >= 0:
                    for i in range(a - 5, a + 5):
                        for j in range(1):
                            suma += pom[i, j]
                            counter += 1
                    prog = suma / counter
                    if pom[a, b] < prog:
                        pom[a, b] = 0
                    else:
                        pom[a, b] = prog
                elif width1 >= b - 5 >= 0 and width1 >= b + 5 >= 0:
                    for i in range(1):
                        for j in range(b - 5, b + 5):
                            suma += pom[i, j]
                            counter += 1
                    prog = suma / counter
                    if pom[a, b] < prog:
                        pom[a, b] = 0
                    else:
                        pom[a, b] = prog

        cv2.imwrite('img5.4(gotowy).png', pom)

# ---------------------------------5.5----------------------------------progowanie globalne czarno biale
    def zad5_5(self, s1, prog):
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

        pom = np.array([[0 for o in range(width1)] for p in range(height1)])
        for a in range(height1):
            for b in range(width1):
                pom[a, b] = img1[a, b, 0]

        for a in range(height1):
            for b in range(width1):
                if pom[a, b] < prog:
                    pom[a, b] = 0
                else:
                    pom[a, b] = prog

        cv2.imwrite('img5.5(gotowy).png', pom)
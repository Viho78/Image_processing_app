import cv2
import numpy as np
import math
import matplotlib
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import Tk, Label
from PIL import Image, ImageTk

import zad1
import zad2
import zad3
import zad4
import zad5
import zad6
DUZE = ("Helvetica", 18)
SREDNIE = ("Helvetica", 14)


class Zad11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad11.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad11.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad11.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad11.destroyy(self))], width=40)
        self.button1.pack()

    def wykonaj(self):
        clas1 = zad1.zad1()
        self.x = clas1.zad1_1(self.path1, self.path2)

        if self.x == 1:
            self.img3 = ImageTk.PhotoImage(Image.open('img1.1-1(gotowy).png'))
            self.img4 = ImageTk.PhotoImage(Image.open('img1.1-2(gotowy).png'))
            hei1 = self.img3.height()
            wid1 = self.img3.width()
            hei2 = self.img4.height()
            wid2 = self.img4.width()
            i1 = Image.open('img1.1-1(gotowy).png')
            i2 = Image.open('img1.1-2(gotowy).png')
            self.img3 = ImageTk.PhotoImage(i1.resize(((int(wid1/2)), int(hei1/2))))
            self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2/2), int(hei2/2)))))
            self.panel3 = tk.Label(self, image=self.img3)
            self.panel3.pack(side="left", fill="both", expand="yes")
            self.panel4 = tk.Label(self, image=self.img4)
            self.panel4.pack(side="left", fill="both", expand="yes")
        else:
            self.img4 = ImageTk.PhotoImage(Image.open('img1.1(gotowy).png'))
            hei2 = self.img4.height()
            wid2 = self.img4.width()
            i2 = Image.open('img1.1(gotowy).png')
            self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
            self.panel4 = tk.Label(self, image=self.img4)
            self.panel4.pack(side="left", fill="both", expand="yes")


    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")


    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        if self.x == 1:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel3.destroy()
            self.panel4.destroy()
        else:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel4.destroy()

class Zad13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad13.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad13.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad13.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad13.destroyy(self))], width=40)
        self.button1.pack()

    def wykonaj(self):
        clas1 = zad1.zad1()
        self.x = clas1.zad1_3(self.path1, self.path2)

        if self.x == 1:
            self.img3 = ImageTk.PhotoImage(Image.open('img1.3-1(gotowy).png'))
            self.img4 = ImageTk.PhotoImage(Image.open('img1.3-2(gotowy).png'))
            hei1 = self.img3.height()
            wid1 = self.img3.width()
            hei2 = self.img4.height()
            wid2 = self.img4.width()
            i1 = Image.open('img1.3-1(gotowy).png')
            i2 = Image.open('img1.3-2(gotowy).png')
            self.img3 = ImageTk.PhotoImage(i1.resize(((int(wid1/2)), int(hei1/2))))
            self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2/2), int(hei2/2)))))
            self.panel3 = tk.Label(self, image=self.img3)
            self.panel3.pack(side="left", fill="both", expand="yes")
            self.panel4 = tk.Label(self, image=self.img4)
            self.panel4.pack(side="left", fill="both", expand="yes")
        else:
            self.img5 = ImageTk.PhotoImage(Image.open('img1.3(gotowy).png'))
            hei2 = self.img5.height()
            wid2 = self.img5.width()
            i3 = Image.open('img1.3(gotowy).png')
            self.img5 = ImageTk.PhotoImage(i3.resize(((int(wid2 / 2), int(hei2 / 2)))))
            self.panel5 = tk.Label(self, image=self.img5)
            self.panel5.pack(side="left", fill="both", expand="yes")


    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")


    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        if self.x == 1:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel3.destroy()
            self.panel4.destroy()
        else:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel5.destroy()

class Zad12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad12.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad12.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad12.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad12.destroyy(self))], width=40)
        self.button1.pack()

    def wykonaj(self):
        clas1 = zad1.zad1()
        self.x = clas1.zad1_2(self.path1, self.path2)

        if self.x == 1:
            self.img3 = ImageTk.PhotoImage(Image.open('img1.2-1(gotowy).png'))
            self.img4 = ImageTk.PhotoImage(Image.open('img1.2-2(gotowy).png'))
            hei1 = self.img3.height()
            wid1 = self.img3.width()
            hei2 = self.img4.height()
            wid2 = self.img4.width()
            i1 = Image.open('img1.2-1(gotowy).png')
            i2 = Image.open('img1.2-2(gotowy).png')
            self.img3 = ImageTk.PhotoImage(i1.resize(((int(wid1/2)), int(hei1/2))))
            self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2/2), int(hei2/2)))))
            self.panel3 = tk.Label(self, image=self.img3)
            self.panel3.pack(side="left", fill="both", expand="yes")
            self.panel4 = tk.Label(self, image=self.img4)
            self.panel4.pack(side="left", fill="both", expand="yes")
        else:
            self.img5 = ImageTk.PhotoImage(Image.open('img1.2(gotowy).png'))
            hei2 = self.img5.height()
            wid2 = self.img5.width()
            i3 = Image.open('img1.2(gotowy).png')
            self.img5 = ImageTk.PhotoImage(i3.resize(((int(wid2 / 2), int(hei2 / 2)))))
            self.panel5 = tk.Label(self, image=self.img5)
            self.panel5.pack(side="left", fill="both", expand="yes")


    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")


    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        if self.x == 1:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel3.destroy()
            self.panel4.destroy()
        else:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel5.destroy()



class Zad14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad14.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad14.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad14.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad14.destroyy(self))], width=40)
        self.button1.pack()

    def wykonaj(self):
        clas1 = zad1.zad1()
        self.x = clas1.zad1_4(self.path1, self.path2)

        if self.x == 1:
            self.img3 = ImageTk.PhotoImage(Image.open('img1.4-1(gotowy).png'))
            self.img4 = ImageTk.PhotoImage(Image.open('img1.4-2(gotowy).png'))
            hei1 = self.img3.height()
            wid1 = self.img3.width()
            hei2 = self.img4.height()
            wid2 = self.img4.width()
            i1 = Image.open('img1.4-1(gotowy).png')
            i2 = Image.open('img1.4-2(gotowy).png')
            self.img3 = ImageTk.PhotoImage(i1.resize(((int(wid1/2)), int(hei1/2))))
            self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2/2), int(hei2/2)))))
            self.panel3 = tk.Label(self, image=self.img3)
            self.panel3.pack(side="left", fill="both", expand="yes")
            self.panel4 = tk.Label(self, image=self.img4)
            self.panel4.pack(side="left", fill="both", expand="yes")
        else:
            self.img5 = ImageTk.PhotoImage(Image.open('img1.4(gotowy).png'))
            hei2 = self.img5.height()
            wid2 = self.img5.width()
            i3 = Image.open('img1.4(gotowy).png')
            self.img5 = ImageTk.PhotoImage(i3.resize(((int(wid2 / 2), int(hei2 / 2)))))
            self.panel5 = tk.Label(self, image=self.img5)
            self.panel5.pack(side="left", fill="both", expand="yes")


    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")


    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        if self.x == 1:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel3.destroy()
            self.panel4.destroy()
        else:
            self.panel1.destroy()
            self.panel2.destroy()
            self.panel5.destroy()

class Zad211(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad211.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad211.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad211.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad211.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas2 = zad2.zad2()
        clas2.zad2_1_1(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.1.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.1.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad212(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad212.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad212.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad212.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas2 = zad2.zad2()
        clas2.zad2_1_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.1.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.1.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad213(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad213.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad213.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad213.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad213.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas2 = zad2.zad2()
        clas2.zad2_1_3(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.1.3(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.1.3(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad214(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad214.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad214.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad214.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas2 = zad2.zad2()
        clas2.zad2_1_4(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.1.4(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.1.4(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad221(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad221.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad221.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad221.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad221.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas2 = zad2.zad2()
        clas2.zad2_2_1(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.2.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.2.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad222(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad222.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad222.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad222.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas2 = zad2.zad2()
        clas2.zad2_2_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.2.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.2.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad23(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad23.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad23.getpath2(self)), width=40)
        self.button4.pack()

        self.label2 = tk.Label(self, text="Podaj współczynnik przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad23.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad23.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas2 = zad2.zad2()
        clas2.zad2_3(self.path1, self.path2, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.3(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.3(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad24(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad24.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj potęge ( >= 1 ) przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad24.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad24.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas2 = zad2.zad2()
        clas2.zad2_4(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.4(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.4(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad251(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad251.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad251.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad251.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad251.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas2 = zad2.zad2()
        clas2.zad2_5_1(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.5.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.5.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad252(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad252.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad252.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad252.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas2 = zad2.zad2()
        clas2.zad2_5_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.5.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.5.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad26(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad26.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą ([0;1]) przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad26.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad26.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = float(self.entry1.get())
        clas2 = zad2.zad2()
        clas2.zad2_6(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.6(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.6(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad27(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad27.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad27.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad27.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas2 = zad2.zad2()
        clas2.zad2_7(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img2.7(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img2.7(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad311(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad311.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad311.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad311.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad311.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas3 = zad3.zad3()
        clas3.zad3_1_1(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.1.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.1.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad312(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad312.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad312.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad312.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas3 = zad3.zad3()
        clas3.zad3_1_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.1.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.1.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad313(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad313.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad313.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad313.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad313.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas3 = zad3.zad3()
        clas3.zad3_1_3(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.1.3(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.1.3(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad314(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad314.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad314.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad314.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas3 = zad3.zad3()
        clas3.zad3_1_4(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.1.4(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.1.4(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad321(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad321.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad321.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad321.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad321.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas3 = zad3.zad3()
        clas3.zad3_2_1(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.2.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.2.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad322(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad322.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad322.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad322.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas3 = zad3.zad3()
        clas3.zad3_2_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.2.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.2.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad33(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad33.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad33.getpath2(self)), width=40)
        self.button4.pack()

        self.label2 = tk.Label(self, text="Podaj współczynnik przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad33.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad33.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas3 = zad3.zad3()
        clas3.zad3_3(self.path1, self.path2, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.3(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.3(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad34(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad34.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj potęge ( >= 1 ) przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad34.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad34.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas3 = zad3.zad3()
        clas3.zad3_4(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.4(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.4(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad351(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz 1", command=lambda: controller.show_frame(Zad351.getpath1(self)), width=40)
        self.button2.pack()
        self.button4 = ttk.Button(self, text="Wybierz obraz 2",command=lambda: controller.show_frame(Zad351.getpath2(self)), width=40)
        self.button4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad351.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad351.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas3 = zad3.zad3()
        clas3.zad3_5_1(self.path1, self.path2)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.5.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.5.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def getpath2(self):
        self.path2 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img2 = ImageTk.PhotoImage(Image.open(self.path2))
        hei2 = self.img2.height()
        wid2 = self.img2.width()
        self.panel2 = tk.Label(self, image=self.img2)
        i2 = Image.open(self.path2)
        self.img2 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel2 = tk.Label(self, image=self.img2)
        self.panel2.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel2.destroy()
        self.panel4.destroy()

class Zad352(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad352.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad352.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad352.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas3 = zad3.zad3()
        clas3.zad3_5_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.5.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.5.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad36(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad36.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj stałą ([0;1]) przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad36.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad36.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = float(self.entry1.get())
        clas3 = zad3.zad3()
        clas3.zad3_6(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.6(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.6(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad37(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obrazy a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad37.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad37.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad37.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas3 = zad3.zad3()
        clas3.zad3_7(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img3.7(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img3.7(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad41(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad41.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj wektor przesunięcia x przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()
        self.label4 = tk.Label(self, text="Podaj wektor przesunięcia y przed wciśnięciem przycisku |wykonaj operacje|",
                               font=SREDNIE)
        self.label4.pack(pady=10, padx=10)
        self.entry2 = tk.Entry(self, width="5")
        self.entry2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad41.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad41.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        stala2 = int(self.entry2.get())
        clas4 = zad4.zad4()
        clas4.zad4_1(stala2, stala1, self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img4.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img4.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad42(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad42.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj wartosc skalowania w pionie (y) przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()
        self.label4 = tk.Label(self, text="Podaj wartosc skalowania w poziomie (x) przed wciśnięciem przycisku |wykonaj operacje|",
                               font=SREDNIE)
        self.label4.pack(pady=10, padx=10)
        self.entry2 = tk.Entry(self, width="5")
        self.entry2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad42.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad42.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = float(self.entry1.get())
        stala2 = float(self.entry2.get())
        clas4 = zad4.zad4()
        clas4.zad4_2(self.path1, stala2, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img4.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img4.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad43(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad43.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj kąt (radiany) przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad43.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad43.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = float(self.entry1.get())
        clas4 = zad4.zad4()
        clas4.zad4_3(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img4.3(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img4.3(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad441(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad441.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad441.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad441.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas4 = zad4.zad4()
        clas4.zad4_4_1(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img4.4.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img4.4.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad442(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad442.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj punkt x osi przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad442.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad442.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas4 = zad4.zad4()
        clas4.zad4_4_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img4.4.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img4.4.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad45(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz i wpisz dane a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad45.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj lewy dolny róg i prawy góry róg, obszaru który chcesz wyciąć:",
                               font=SREDNIE)
        self.label2 = tk.Label(self, text="Podaj x lewego dolnego rogu", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()
        self.label3 = tk.Label(self, text="Podaj y lewego dolnego rogu", font=SREDNIE)
        self.label3.pack(pady=10, padx=10)
        self.entry2 = tk.Entry(self, width="5")
        self.entry2.pack()
        self.label4 = tk.Label(self, text="Podaj x prawego górnego rogu", font=SREDNIE)
        self.label4.pack(pady=10, padx=10)
        self.entry3 = tk.Entry(self, width="5")
        self.entry3.pack()
        self.label5 = tk.Label(self, text="Podaj y prawego górnego rogu", font=SREDNIE)
        self.label5.pack(pady=10, padx=10)
        self.entry4 = tk.Entry(self, width="5")
        self.entry4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad45.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad45.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        stala2 = int(self.entry2.get())
        stala3 = int(self.entry3.get())
        stala4 = int(self.entry4.get())
        clas4 = zad4.zad4()
        clas4.zad4_5(self.path1, stala1, stala2, stala3, stala4)

        self.img4 = ImageTk.PhotoImage(Image.open('img4.5(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img4.5(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad46(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz i wpisz dane a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad46.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj lewy dolny róg i prawy góry róg, obszaru który chcesz skopiować:",
                               font=SREDNIE)
        self.label2 = tk.Label(self, text="Podaj x lewego dolnego rogu", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()
        self.label3 = tk.Label(self, text="Podaj y lewego dolnego rogu", font=SREDNIE)
        self.label3.pack(pady=10, padx=10)
        self.entry2 = tk.Entry(self, width="5")
        self.entry2.pack()
        self.label4 = tk.Label(self, text="Podaj x prawego górnego rogu", font=SREDNIE)
        self.label4.pack(pady=10, padx=10)
        self.entry3 = tk.Entry(self, width="5")
        self.entry3.pack()
        self.label5 = tk.Label(self, text="Podaj y prawego górnego rogu", font=SREDNIE)
        self.label5.pack(pady=10, padx=10)
        self.entry4 = tk.Entry(self, width="5")
        self.entry4.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad46.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad46.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        stala2 = int(self.entry2.get())
        stala3 = int(self.entry3.get())
        stala4 = int(self.entry4.get())
        clas4 = zad4.zad4()
        clas4.zad4_6(self.path1, stala1, stala2, stala3, stala4)

        self.img4 = ImageTk.PhotoImage(Image.open('img4.6(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img4.6(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad51(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad51.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad51.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad51.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas5 = zad5.zad5()
        clas5.zad5_1(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img5.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img5.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad52(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad52.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj wartość przemieszczenia przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad52.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad52.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas5 = zad5.zad5()
        clas5.zad5_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img5.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img5.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad53(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad53.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad53.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad53.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas5 = zad5.zad5()
        clas5.zad5_3(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img5.3(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img5.3(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad54(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad54.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad54.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad54.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas5 = zad5.zad5()
        clas5.zad5_4(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img5.4(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img5.4(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad55(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad55.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj próg przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad55.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad55.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas5 = zad5.zad5()
        clas5.zad5_5(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img5.5(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img5.5(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad61(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad61.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad61.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad61.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas6 = zad6.zad6()
        clas6.zad6_1(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img6.1(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img6.1(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad62(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad62.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj próg przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad62.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad62.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas6 = zad6.zad6()
        clas6.zad6_2(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img6.2(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img6.2(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad63(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad63.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad63.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad63.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas6 = zad6.zad6()
        clas6.zad6_3(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img6.3(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img6.3(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad64(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad64.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj próg 1 przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()
        self.label3 = tk.Label(self, text="Podaj próg 2 przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label3.pack(pady=10, padx=10)
        self.entry2 = tk.Entry(self, width="5")
        self.entry2.pack()
        self.label4 = tk.Label(self, text="Podaj próg 3 przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label4.pack(pady=10, padx=10)
        self.entry3 = tk.Entry(self, width="5")
        self.entry3.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad64.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad64.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        stala2 = int(self.entry2.get())
        stala3 = int(self.entry3.get())
        clas6 = zad6.zad6()
        clas6.zad6_4(self.path1, stala1, stala2, stala3)

        self.img4 = ImageTk.PhotoImage(Image.open('img6.4(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img6.4(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad65(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad65.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad65.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad65.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas6 = zad6.zad6()
        clas6.zad6_5(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img6.5(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img6.5(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad66(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad66.getpath1(self)), width=40)
        self.button2.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad66.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad66.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        clas6 = zad6.zad6()
        clas6.zad6_6(self.path1)

        self.img4 = ImageTk.PhotoImage(Image.open('img6.6(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img6.6(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()

class Zad67(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Wybierz obraz a dopiero następnie kliknij |wykonaj operacje|", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.button2 = ttk.Button(self, text="Wybierz obraz", command=lambda: controller.show_frame(Zad67.getpath1(self)), width=40)
        self.button2.pack()

        self.label2 = tk.Label(self, text="Podaj próg przed wciśnięciem przycisku |wykonaj operacje|", font=SREDNIE)
        self.label2.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width="5")
        self.entry1.pack()

        self.button4 = ttk.Button(self, text="Wykonaj operacje (może chwile potrwać)",command=lambda: controller.show_frame(Zad67.wykonaj(self)), width=40)
        self.button4.pack()

        self.button1 = ttk.Button(self, text="Powrót do menu", command=lambda: [controller.show_frame(StartPage), controller.show_frame(Zad67.destroyy(self))])
        self.button1.pack()

    def wykonaj(self):
        stala1 = int(self.entry1.get())
        clas6 = zad6.zad6()
        clas6.zad6_7(self.path1, stala1)

        self.img4 = ImageTk.PhotoImage(Image.open('img6.7(gotowy).png'))
        hei2 = self.img4.height()
        wid2 = self.img4.width()
        i2 = Image.open('img6.7(gotowy).png')
        self.img4 = ImageTk.PhotoImage(i2.resize(((int(wid2 / 2), int(hei2 / 2)))))
        self.panel4 = tk.Label(self, image=self.img4)
        self.panel4.pack(side="left", fill="both", expand="yes")

    def getpath1(self):
        self.path1 = fd.askopenfilename(filetypes=[("png files", ".png")])
        self.img1 = ImageTk.PhotoImage(Image.open(self.path1))
        hei1 = self.img1.height()
        wid1 = self.img1.width()
        self.panel1 = tk.Label(self, image=self.img1)
        i1 = Image.open(self.path1)
        self.img1 = ImageTk.PhotoImage(i1.resize(((int(wid1 / 2), int(hei1 / 2)))))
        self.panel1 = tk.Label(self, image=self.img1)
        self.panel1.pack(side="left", fill="both", expand="yes")

    def destroyy(self):
        self.panel1.destroy()
        self.panel4.destroy()


class StartPage3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Przetwarzanie obrazów - aplikacja Juliusz Stańczyk", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.label4 = tk.Label(self, text="5. Operacje na histogramie obrazu szarego:", font=SREDNIE)
        self.label4.pack(pady=10, padx=10)
        self.button14 = ttk.Button(self, text="5.1 Obliczanie histogramu",
                                   command=lambda: controller.show_frame(Zad51), width=50)
        self.button14.pack()
        self.button15 = ttk.Button(self, text="5.2 Przemieszczanie histogramu",
                                   command=lambda: controller.show_frame(Zad52), width=50)
        self.button15.pack()
        self.button16 = ttk.Button(self, text="5.3 Rozciąganie histogramu",
                                   command=lambda: controller.show_frame(Zad53), width=50)
        self.button16.pack()
        self.button17 = ttk.Button(self, text="5.4 Progowanie lokalne",
                                   command=lambda: controller.show_frame(Zad54), width=50)
        self.button17.pack()
        self.button18 = ttk.Button(self, text="5.5 Progowanie globalne",
                                   command=lambda: controller.show_frame(Zad55), width=50)
        self.button18.pack()


        self.label5 = tk.Label(self, text="6. Operacje na histogramie obrazu barwowego:", font=SREDNIE)
        self.label5.pack(pady=10, padx=10)
        self.button1 = ttk.Button(self, text="6.1 Obliczanie histogramu",
                                   command=lambda: controller.show_frame(Zad61), width=50)
        self.button1.pack()
        self.button2 = ttk.Button(self, text="6.2 Przemieszczanie histogramu",
                                   command=lambda: controller.show_frame(Zad62), width=50)
        self.button2.pack()
        self.button3 = ttk.Button(self, text="6.3 Rozciąganie histogramu",
                                   command=lambda: controller.show_frame(Zad63), width=50)
        self.button3.pack()
        self.button4 = ttk.Button(self, text="6.4 Progowanie globalne wieloprogowe",
                                   command=lambda: controller.show_frame(Zad64), width=50)
        self.button4.pack()
        self.button5 = ttk.Button(self, text="6.5 Progowanie lokalne wieloprogowe",
                                   command=lambda: controller.show_frame(Zad65), width=50)
        self.button5.pack()
        self.button6 = ttk.Button(self, text="6.6 Progowanie lokalne jednoprogowe",
                                   command=lambda: controller.show_frame(Zad66), width=50)
        self.button6.pack()
        self.button7 = ttk.Button(self, text="6.7 Progowanie globalne jednoprogowe",
                                   command=lambda: controller.show_frame(Zad67), width=50)
        self.button7.pack()

        self.button1 = ttk.Button(self, text="Poprzednia strona",
                                   command=lambda: controller.show_frame(StartPage2), width=30)
        self.button1.pack(side="right")

class StartPage2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Przetwarzanie obrazów - aplikacja Juliusz Stańczyk", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.label4 = tk.Label(self, text="3. Operacje sumowania arytmetycznego obrazów barwowych:", font=SREDNIE)
        self.label4.pack(pady=10, padx=10)
        self.button14 = ttk.Button(self, text="3.1.1 Sumowanie stałej z obrazem",
                                   command=lambda: controller.show_frame(Zad312), width=50)
        self.button14.pack()
        self.button15 = ttk.Button(self, text="3.1.2 Sumowanie dwóch obrazów",
                                   command=lambda: controller.show_frame(Zad311), width=50)
        self.button15.pack()
        self.button16 = ttk.Button(self, text="3.1.3 Odejmowanie stałej z obrazem",
                                   command=lambda: controller.show_frame(Zad314), width=50)
        self.button16.pack()
        self.button17 = ttk.Button(self, text="3.1.4 Odejmowanie dwóch obrazów",
                                   command=lambda: controller.show_frame(Zad313), width=50)
        self.button17.pack()
        self.button18 = ttk.Button(self, text="3.2.1 Mnożenie obrazu przez zadaną liczbę",
                                   command=lambda: controller.show_frame(Zad322), width=50)
        self.button18.pack()
        self.button19 = ttk.Button(self, text="3.2.2 Mnożenie obrazu przez drugi obraz",
                                   command=lambda: controller.show_frame(Zad321), width=50)
        self.button19.pack()
        self.button20 = ttk.Button(self, text="3.3 Mieszanie obrazów z określonym wspołczynnikiem",
                                   command=lambda: controller.show_frame(Zad33), width=50)
        self.button20.pack()
        self.button21 = ttk.Button(self, text="3.4 Potęgowanie obrazu",
                                   command=lambda: controller.show_frame(Zad34), width=50)
        self.button21.pack()
        self.button22 = ttk.Button(self, text="3.5.1 Dzielenie obrazu przez stałą",
                                   command=lambda: controller.show_frame(Zad352), width=50)
        self.button22.pack()
        self.button23 = ttk.Button(self, text="3.5.2 Dzielenie obrazu przez drugi obraz",
                                   command=lambda: controller.show_frame(Zad351), width=50)
        self.button23.pack()
        self.button24 = ttk.Button(self, text="3.6 Pierwiastkowanie obrazu",
                                   command=lambda: controller.show_frame(Zad36), width=50)
        self.button24.pack()
        self.button25 = ttk.Button(self, text="3.7 Logarytmowanie obrazu",
                                   command=lambda: controller.show_frame(Zad37), width=50)
        self.button25.pack()

        self.label5 = tk.Label(self, text="4. Operacje geometryczne na obrazie:", font=SREDNIE)
        self.label5.pack(pady=10, padx=10)
        self.button26 = ttk.Button(self, text="4.1 Przemieszczanie obrazu o zadany wektor",
                                   command=lambda: controller.show_frame(Zad41), width=50)
        self.button26.pack()
        self.button27 = ttk.Button(self, text="4.2 Jednorodne i niejednorodne skalowanie obrazu",
                                   command=lambda: controller.show_frame(Zad42), width=50)
        self.button27.pack()
        self.button28 = ttk.Button(self, text="4.3 Obracanie obrazu o dowolny kąt",
                                   command=lambda: controller.show_frame(Zad43), width=50)
        self.button28.pack()
        self.button29 = ttk.Button(self, text="4.4.1 Symetria względem osi układu",
                                   command=lambda: controller.show_frame(Zad441), width=50)
        self.button29.pack()
        self.button31 = ttk.Button(self, text="4.4.2 Symetria względem zadanej prostej pionowej",
                                   command=lambda: controller.show_frame(Zad442), width=50)
        self.button31.pack()
        self.button30 = ttk.Button(self, text="4.5 Wycinanie fragmentu obrazu",
                                   command=lambda: controller.show_frame(Zad45), width=50)
        self.button30.pack()
        self.button32 = ttk.Button(self, text="4.6 Kopiowanie fragmentu obrazu",
                                   command=lambda: controller.show_frame(Zad46), width=50)
        self.button32.pack()

        self.button2 = ttk.Button(self, text="Następna strona",
                                   command=lambda: controller.show_frame(StartPage3), width=30)
        self.button2.pack(side="right")
        self.button1 = ttk.Button(self, text="Poprzednia strona",
                                  command=lambda: controller.show_frame(StartPage), width=30)
        self.button1.pack(side="right")

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text="Przetwarzanie obrazów - aplikacja Juliusz Stańczyk", font=DUZE)
        self.label1.pack(pady=10, padx=10)

        self.label8 = tk.Label(self, text="1. Operacje ujednolicenia obrazów:", font=SREDNIE)
        self.label8.pack(pady=10, padx=10)
        self.button1 = ttk.Button(self, text="1.1 Ujednolicenie obrazów szarych geometryczne",command=lambda: controller.show_frame(Zad11), width=50)
        self.button1.pack()
        self.button34 = ttk.Button(self, text="1.2 Ujednolicenie obrazów szarych rozdzielczościowe",
                                  command=lambda: controller.show_frame(Zad12), width=50)
        self.button34.pack()
        self.button35 = ttk.Button(self, text="1.3 Ujednolicenie obrazów barwowych geometryczne",
                                  command=lambda: controller.show_frame(Zad13), width=50)
        self.button35.pack()
        self.button36 = ttk.Button(self, text="1.4 Ujednolicenie obrazów barwowych rozdzielczościowe",
                                  command=lambda: controller.show_frame(Zad14), width=50)
        self.button36.pack()

        self.label3 = tk.Label(self, text="2. Operacje sumowania arytmetycznego obrazów szarych:", font=SREDNIE)
        self.label3.pack(pady=10, padx=10)
        self.button2 = ttk.Button(self, text="2.1.1 Sumowanie stałej z obrazem",command=lambda: controller.show_frame(Zad212), width=50)
        self.button2.pack()
        self.button3 = ttk.Button(self, text="2.1.2 Sumowanie dwóch obrazów",
                                  command=lambda: controller.show_frame(Zad211), width=50)
        self.button3.pack()
        self.button4 = ttk.Button(self, text="2.1.3 Odejmowanie stałej z obrazem",
                                  command=lambda: controller.show_frame(Zad214), width=50)
        self.button4.pack()
        self.button5 = ttk.Button(self, text="2.1.4 Odejmowanie dwóch obrazów",
                                  command=lambda: controller.show_frame(Zad213), width=50)
        self.button5.pack()
        self.button6 = ttk.Button(self, text="2.2.1 Mnożenie obrazu przez zadaną liczbę",
                                  command=lambda: controller.show_frame(Zad222), width=50)
        self.button6.pack()
        self.button7 = ttk.Button(self, text="2.2.2 Mnożenie obrazu przez drugi obraz",
                                  command=lambda: controller.show_frame(Zad221), width=50)
        self.button7.pack()
        self.button8 = ttk.Button(self, text="2.3 Mieszanie obrazów z określonym wspołczynnikiem",
                                  command=lambda: controller.show_frame(Zad23), width=50)
        self.button8.pack()
        self.button9 = ttk.Button(self, text="2.4 Potęgowanie obrazu",
                                  command=lambda: controller.show_frame(Zad24), width=50)
        self.button9.pack()
        self.button10 = ttk.Button(self, text="2.5.1 Dzielenie obrazu przez stałą",
                                  command=lambda: controller.show_frame(Zad252), width=50)
        self.button10.pack()
        self.button11 = ttk.Button(self, text="2.5.2 Dzielenie obrazu przez drugi obraz",
                                  command=lambda: controller.show_frame(Zad251), width=50)
        self.button11.pack()
        self.button12 = ttk.Button(self, text="2.6 Pierwiastkowanie obrazu",
                                  command=lambda: controller.show_frame(Zad26), width=50)
        self.button12.pack()
        self.button13 = ttk.Button(self, text="2.7 Logarytmowanie obrazu",
                                   command=lambda: controller.show_frame(Zad27), width=50)
        self.button13.pack()

        self.button33 = ttk.Button(self, text="Następna strona",
                                   command=lambda: controller.show_frame(StartPage2), width=30)
        self.button33.pack(side="right")


class MMain(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Przetwarzanie obrazów")
        tk.Tk.wm_state(self,'zoomed')

        cont = tk.Frame(self)
        cont.pack(side="top", fill="both", expand=True)
        cont.grid_columnconfigure(0, weight=1)
        cont.grid_rowconfigure(0, weight=1)


        self.frames = {}

        for FR in (StartPage, Zad11, Zad211, Zad212, Zad213, Zad214, Zad221, Zad222, Zad23, Zad24, Zad251, Zad252,
                   Zad26, Zad27, Zad311, Zad312, Zad313, Zad314, Zad321, Zad322, Zad33, Zad34, Zad34, Zad351, Zad352,
                   Zad36, Zad37, Zad41, StartPage2, StartPage3, Zad42, Zad43, Zad441, Zad442, Zad45, Zad46, Zad51, Zad52,
                   Zad53, Zad54, Zad55, Zad61, Zad62, Zad63, Zad64, Zad65, Zad66, Zad67, Zad13, Zad12, Zad14):
            frame = FR(cont, self)

            self.frames[FR] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, contt):
        frame = self.frames[contt]
        frame.tkraise()

def Normalizacja(img, height1, width1, chan1):
    minb = 255
    ming = 255
    minr = 255

    maxb = 0
    maxg = 0
    maxr = 0

    b3 = np.array([[0 for x in range(width1)] for y in range(height1)])
    g3 = np.array([[0 for x in range(width1)] for y in range(height1)])
    r3 = np.array([[0 for x in range(width1)] for y in range(height1)])

    for i in range(height1):
        for j in range(width1):
            for c in range(chan1):
                if c == 0:
                    b3[i, j] = img[i, j, c]
                elif c == 1:
                    g3[i, j] = img[i, j, c]
                elif c == 2:
                    r3[i, j] = img[i, j, c]

    for i in range(height1):
        for j in range(width1):
            if i == 0 & j == 0:
                minb = b3[i][j]
                ming = g3[i][j]
                minr = r3[i][j]

                maxb = b3[i][j]
                maxg = g3[i][j]
                maxr = r3[i][j]

            if b3[i][j] < minb:
                minb = b3[i][j]
            if b3[i][j] > maxb:
                maxb = b3[i][j]

            if g3[i][j] < ming:
                ming = g3[i][j]
            if g3[i][j] > maxb:
                maxg = g3[i][j]

            if r3[i][j] < minr:
                minr = r3[i][j]
            if r3[i][j] > maxr:
                maxr = r3[i][j]

    min1 = min(minb, ming, minr)
    max1 = max(maxb, maxg, maxr)

    bdone = np.array([[0 for x in range(width1)] for y in range(height1)])
    gdone = np.array([[0 for x in range(width1)] for y in range(height1)])
    rdone = np.array([[0 for x in range(width1)] for y in range(height1)])

    for i in range(height1):
        for j in range(width1):
            bdone[i, j] = ((int(b3[i, j]) - int(min1)) / (int(max1) - int(min1))) * 255
            gdone[i, j] = ((int(g3[i, j]) - int(min1)) / (int(max1) - int(min1))) * 255
            rdone[i, j] = ((int(r3[i, j]) - int(min1)) / (int(max1) - int(min1))) * 255

    pom = np.array([[[0 for x in range(3)] for y in range(width1)] for g in range(height1)])
    # merge
    for a in range(height1):
        for b in range(width1):
            for c in range(3):
                if c == 0:
                    pom[a, b, 0] = bdone[a, b]
                if c == 1:
                    pom[a, b, 1] = gdone[a, b]
                if c == 2:
                    pom[a, b, 2] = rdone[a, b]

    return pom

if __name__ == '__main__':
    app = MMain()
    app.mainloop()

    #c = zad2.zad2()
    #c.zad2_1_1("aimg1.png", "aimg3.png")


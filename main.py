from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random


class MainApp(Tk):
    size = '475x565'
    __cerodados = '0'
    dadosa0 = {4: 0, 6: 0, 8: 0, 10: 0, 12: 0, 20: 0}

    def __init__(self):
        Tk.__init__(self)
        self.geometry(self.size)
        self.title('Simulador de Dados')
        self.configure(bg='#ECECEC')
        self.resizable(0, 0)

        self.dados4 = StringVar(value='')
        # self.dados4.trace('w', self.validate(self.dados4.get()))
        self.dados6 = StringVar(value='')
        # self.dados6.trace('w', self.validate(self.dados6.get()))
        self.dados8 = StringVar(value='')
        # self.dados8.trace('w', self.validate(self.dados8.get()))
        self.dados10 = StringVar(value='')
        # self.dados10.trace('w', self.validate(self.dados10.get()))
        self.dados12 = StringVar(value='')
        # self.dados12.trace('w', self.validate(self.dados12.get()))
        self.dados20 = StringVar(value='')
        # self.dados20.trace('w', self.validate(self.dados20.get()))
        self.seleccion = {4: self.dados4, 6: self.dados6, 8: self.dados8, 10: self.dados10, 12: self.dados12,
                          20: self.dados20}

        self.createlayout()
    '''
    def validate(self, dados):
        ndados = dados
        try:
            int(ndados)
            self.__cerodados = ndados
        except:
            # self.dados.set(self.__cerodados)
            pass
    '''

    def createlayout(self):

        self.lbldados = ttk.Label(self, text='Numero de dados:').place(x=150, y=10)

        self.entradad4 = ttk.Entry(self, textvariable=self.dados4).place(x=150, y=40)
        self.photod4 = ImageTk.PhotoImage(Image.open("d4.gif"))
        self.canvas = Label(self, image=self.photod4)
        self.canvas.place(x=10, y=22)

        self.entradad6 = ttk.Entry(self, textvariable=self.dados6).place(x=150, y=140)
        self.photod6 = ImageTk.PhotoImage(Image.open("d6.gif"))
        self.canvas = Label(self, image=self.photod6)
        self.canvas.place(x=10, y=112)

        self.entradad8 = ttk.Entry(self, textvariable=self.dados8).place(x=150, y=230)
        self.photod8 = ImageTk.PhotoImage(Image.open("d8.gif"))
        self.canvas = Label(self, image=self.photod8)
        self.canvas.place(x=10, y=202)

        self.entradad10 = ttk.Entry(self, textvariable=self.dados10).place(x=150, y=320)
        self.photod10 = ImageTk.PhotoImage(Image.open("d10.gif"))
        self.canvas = Label(self, image=self.photod10)
        self.canvas.place(x=10, y=292)

        self.entradad12 = ttk.Entry(self, textvariable=self.dados12).place(x=150, y=410)
        self.photod12 = ImageTk.PhotoImage(Image.open("d12.gif"))
        self.canvas = Label(self, image=self.photod12)
        self.canvas.place(x=10, y=382)

        self.entradad20 = ttk.Entry(self, textvariable=self.dados20).place(x=150, y=500)
        self.photod20 = ImageTk.PhotoImage(Image.open("d20.gif"))
        self.canvas = Label(self, image=self.photod20)
        self.canvas.place(x=10, y=472)

    def tirada(self):
        tirada = 0
        for i in range(0, int(self.seleccion.values())+1):
            tirada += random()

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()

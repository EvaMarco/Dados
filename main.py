from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random


class MainApp(Tk):
    size = '475x565'
    resultado = 0

    def __init__(self):
        # Para no tener que poner .ttk en todos lados.
        Tk.__init__(self)
        # Tamaño de la ventana, nombre, color de fondo y que no se pueda modificar el tamaño.
        self.geometry(self.size)
        self.title('Simulador de Dados')
        self.configure(bg='#ECECEC')
        self.resizable(0, 0)

        # Creamos las variables del número de dados. Y le pedimos q nos de el valor para meterlo en el diccionario.
        self.dados4 = IntVar(value=0)
        self.d4 = self.dados4.get()

        self.dados6 = IntVar(value=0)
        self.d6 = self.dados6.get()

        self.dados8 = IntVar(value=0)
        self.d8 = self.dados8.get()

        self.dados10 = IntVar(value=0)
        self.d10 = self.dados10.get()

        self.dados12 = IntVar(value=0)
        self.d12 = self.dados12.get()

        self.dados20 = IntVar(value=0)
        self.d20 = self.dados20.get()

        # Aqui se pinta la pantalla, esta abajo más especificada.
        self.createlayout()

        # El diccionario que no se actualiza, no se donde lo tengo que poner para que lo haga.
        self.pooldados = {4: self.d4, 6: self.d6, 8: self.d8, 10: self.d10, 12: self.d12, 20: self.d20}



    def tirada(self, *args):

        resultado = 0

        for i in self.pooldados:

            value = self.pooldados.get(i)
            if value != 0:

                for j in range(value):
                    number = random.randint(1, i)
                    resultado += number
        print(resultado)
        print(self.pooldados)
        return resultado

    def createlayout(self):

        # Aqui aparecen las etiquetas, las imagenes y demás.

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

        # El botón que lanza la función tirar dados.

        self.boton = ttk.Button(self, text="Tirar", command=self.tirada).place(x=350, y=100)

        # La etiqueta donde quiero que salga el resultado pero no lo hace.

        self.lblresultado = ttk.Label(self, textvariable=self.resultado, foreground="yellow",
                                      background="black") .place(x=350, y=200)

    # Bucle principal.
    def start(self):
        self.mainloop()

# Para que se ejecute desde la aplicación, sin tener que escribirlo en el shell.
if __name__ == '__main__':
    app = MainApp()
    app.start()

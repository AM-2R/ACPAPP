from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text, Image, ttk
from PIL import ImageTk, Image

from main import *
root = Tk()
root.title('ACP')
root.iconbitmap('assets/ACP.ico')
root.geometry("900x750")
root.minsize(900, 750)
root.configure(bg='white')

imgS = Image.open("assets\second.png")
resized_image = imgS.resize((900, 150))
new_image = ImageTk.PhotoImage(resized_image)
label = Label(root, image=new_image, bg='white')
label.pack()


# text lowel
L5 = Label(root, background='white',
           font=('Segoe UI', 18, 'bold'),
           bg='white',
           fg='#707070',
           text="Intervalle de temps pour chaque terminal")
L5.place(x=30, y=155)
L51 = Label(root, background='white',
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg='#707070',
            text=f"Terminal 1")
L51.place(x=30, y=185)
L51 = Label(root, background='white',
            font=('Segoe UI', 12),
            bg='white',
            fg='#707070',
            text=f"Le valeur doit être un entier")
L51.place(x=150, y=192)


def ab3at3():
    sad1 = achfa2.get()
    GAP1(sad1)


achfa2 = IntVar()

input2 = Entry(highlightthickness=1,
               width=30,
               textvariable=achfa2,
               font=('Segoe UI', 25))

input2.place(x=30, y=220)


input2.config(highlightbackground="#707070",
              font=('Segoe UI', 25),
              highlightcolor='#707070')

img3 = Image.open("assets/valider.png")
re = img3.resize((200, 50))
img3 = ImageTk.PhotoImage(re)

Button(root, image=img3, bd=0, bg="#037EF3",
       activebackground='#ffffff',
       highlightthickness=1,
       command=ab3at3).place(x=575, y=220)
# text zawej

L61 = Label(root, background='white',
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg='#707070',
            text=f"Terminal 2")
L61.place(x=30, y=275)
L61 = Label(root, background='white',
            font=('Segoe UI', 12),
            bg='white',
            fg='#707070',
            text=f"Le valeur doit être un entier")
L61.place(x=150, y=282)


def ab3at4():
    sad1 = achfa4.get()
    GAP2(sad1)


achfa4 = IntVar()

input4 = Entry(highlightthickness=1,
               width=30,
               textvariable=achfa4,
               font=('Segoe UI', 25))

input4.place(x=30, y=310)


input4.config(highlightbackground="#707070",
              font=('Segoe UI', 25),
              highlightcolor='#707070')

img5 = Image.open("assets/valider.png")
re = img5.resize((200, 50))
img5 = ImageTk.PhotoImage(re)

Button(root, image=img5, bd=0, bg="#037EF3",
       activebackground='#ffffff',
       highlightthickness=1,
       command=ab3at4).place(x=575, y=310)
# text talet

L71 = Label(root, background='white',
            font=('Segoe UI', 16, 'bold'),
            bg='white',
            fg='#707070',
            text=f"Terminal Ouest")
L71.place(x=30, y=365)
L71 = Label(root, background='white',
            font=('Segoe UI', 12),
            bg='white',
            fg='#707070',
            text=f"Le valeur doit être un entier")
L71.place(x=190, y=372)


def ab3at7():
    sad1 = achfa7.get()
    GAP4(sad1)


achfa7 = IntVar()

input7 = Entry(highlightthickness=1,
               width=30,
               textvariable=achfa7,
               font=('Segoe UI', 25))

input7.place(x=30, y=400)


input7.config(highlightbackground="#707070",
              font=('Segoe UI', 25),
              highlightcolor='#707070')

img7 = Image.open("assets/valider.png")
re = img7.resize((200, 50))
img7 = ImageTk.PhotoImage(re)

Button(root, image=img7, bd=0, bg="#037EF3",
       activebackground='#ffffff',
       highlightthickness=1,
       command=ab3at7).place(x=575, y=400)

# DU
L8 = Label(root, background='white',
           font=('Segoe UI', 18, 'bold'),
           bg='white',
           fg='#707070',
           text="Le Temps de Brigade de Nuit")
L8.place(x=30, y=465)
L8 = Label(root, background='white',
           font=('Segoe UI', 14, 'bold'),
           bg='white',
           fg='#707070',
           text="Du")
L8.place(x=30, y=500)
L9 = Label(root, background='white',
           font=('Segoe UI', 14),
           bg='white',
           fg='#707070',
           text="l'heure de debut de brigade de nuit en Heure")
L9.place(x=60, y=500)

def ab3at8():
    sad1 = achfa8.get()


achfa8 = IntVar()
input8 = Entry(highlightthickness=1,
               width=15,
               textvariable=achfa8,
               font=('Segoe UI', 25))

input8.place(x=30, y=530)


input8.config(highlightbackground="#707070",
              font=('Segoe UI', 25),
              highlightcolor='#707070')


# AU

L9 = Label(root, background='white',
           font=('Segoe UI', 14, 'bold'),
           bg='white',
           fg='#707070',
           text="Au")
L9.place(x=30, y=585)
L10 = Label(root, background='white',
            font=('Segoe UI', 14),
            bg='white',
            fg='#707070',
            text="l'heure de debut de brigade de nuit en Heure")
L10.place(x=60, y=585)

achfa9 = IntVar()

input9 = Entry(highlightthickness=1,
               width=15,
               textvariable=achfa9,
               font=('Segoe UI', 25))

input9.place(x=30, y=615)


input9.config(highlightbackground="#707070",
              font=('Segoe UI', 25),
              highlightcolor='#707070')

# valider
imgF = Image.open("assets/fin.png")
reF = imgF.resize((231, 60))
imgF = ImageTk.PhotoImage(reF)


def Fin():
    sad1 = achfa8.get()
    TNuit1(sad1)

    sad2 = achfa9.get()
    TNuit2(sad2)



Fin = Button(root, image=imgF, bd=0, bg='#ffffff',
             activebackground='#ffffff',
             command=Fin)
Fin.place(x=30, y=680)
root.mainloop()

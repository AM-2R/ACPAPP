from ast import If
from cProfile import label
from fileinput import filename
from msilib.schema import RadioButton
import os
from ssl import Options
import sys
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text, Image, ttk
from tkinter.filedialog import asksaveasfile
from xml.dom.expatbuilder import parseString
from PIL import ImageTk, Image
from main import *
root = Tk()
root.title('ACP')
root.iconbitmap('assets/ACP.ico')
root.geometry("900x750")
root.minsize(900, 750)
root.configure(bg='white')
p = dat()


imgM = Image.open("assets\main.png")
resized_image = imgM.resize((900, 150))
new_image = ImageTk.PhotoImage(resized_image)
label = Label(root, image=new_image, bg='white')
label.pack()
# text lowel
L1 = Label(root, background='white',
           font=('Segoe UI', 18, 'bold'),
           bg='white',
           fg='#707070',
           text="Importer des données")
L1.place(x=30, y=155)
L11 = Label(root, background='white',
            font=('Segoe UI', 12, ),
            bg='white',
            fg='#707070',
            text="Tous les fichiers doivent être des fichiers xlsx contenant les colonnes suivantes ( Terminal , Date , HPA, HPD )")
L11.place(x=30, y=190)


# open exel file


def open():
    global options
    root.filename = filedialog.askopenfilename(
        title="Selectionnez un ficher", filetypes=[("Fichier Excel", "*.xlsx")])
    Operation01(root.filename)

    p.Datelist()
    print('hna')
    print(p.options)
    ref()


# button image
img1 = Image.open("assets/import.png")
re = img1.resize((380, 80))
img1 = ImageTk.PhotoImage(re)

Button(root, image=img1, bd=0, bg='#ffffff',
       activebackground='#ffffff',
       command=open).place(x=30, y=215)

# text zawej
L2 = Label(root, background='white',
           font=('Segoe UI', 18, 'bold'),
           bg='white',
           fg='#707070',
           text="Choisissez votre date")
L2.place(x=30, y=290)
L21 = Label(root, background='white',
            font=('Segoe UI', 12),
            bg='white',
            fg='#707070',
            text="la date doit être au format Annee-Mois-Jour, et incluse dans le fichier xlsx que vous avez importé avant .")
L21.place(x=30, y=320)

# input yakho
# hna hover


def click(event):

    input1.config(state=NORMAL)
    input1.delete(0, END)


# hna save input


def ab3at():
    sad = achfa.get()
    DateCheck(sad)
    print(sad)


op = (' ')
el3andalib = StringVar(root)


def ref():
    el3andalib.set('')
    w['menu'].delete(0, 'end')
    for choice in p.options:
        w['menu'].add_command(
            label=choice,
            command=tk._setit(el3andalib, choice))
    print(choice)


el3andalib.set('Selectioner votre date ici')  # default value
el3andalib.trace("w", ref)
w = OptionMenu(root, el3andalib, *op)

w.config(bg='white',

         font=('Segoe UI', 22),
         highlightthickness=1,
         fg='#707070',
         highlightbackground="#707070",
         highlightcolor='#CDCBCB',
         borderwidth=0, width=40)
w.place(x=30, y=350)
# achfa = StringVar()
# input1 = Entry(root, highlightthickness=1,
#                width=30,
#                textvariable=achfa,
#                font=('Segoe UI', 25))

# input1.place(x=30, y=350)
# input1.insert(0, 'Ecrire votre date ici')
# input1.config(highlightbackground="#707070",
#               state=DISABLED,
#               font=('Segoe UI', 25),
#               highlightcolor='#707070')

# input1.bind("<Button-1>", click)
# button image
# img2 = Image.open("assets/valider.png")
# re = img2.resize((200, 50))
# img2 = ImageTk.PhotoImage(re)

# Button(root, image=img2, bd=0, bg="#037EF3",
#        activebackground='#ffffff',
#        highlightthickness=1,
#        command=ab3at).place(x=575, y=350)


# text talet
L2 = Label(root, background='white',
           font=('Segoe UI', 18, 'bold'),
           bg='white',
           fg='#707070',
           text="3. Choisissez votre Brigade")
L2.place(x=30, y=405)
L21 = Label(root, background='white',
            font=('Segoe UI', 12),
            bg='white',
            fg='#707070',
            text="vous pouvez toujours aller au paramettre pour vérifier l'heure de début de la brigade de nuit et la changer")
L21.place(x=30, y=440)
# radio button
v1 = IntVar()


def nuit():
    Br = 'Nuit'
    BrigadeCheck(Br)
    print(Br)
    Operations02()


def jour():
    Br = 'Journee'
    print(Br)
    BrigadeCheck(Br)
    Operations02()


r1 = Radiobutton(root,
                 text='Journee',
                 variable=v1,
                 font=('Segoe UI', 15, 'bold'),
                 bg='white',
                 fg='#707070',
                 value=1,
                 command=jour)
r1.place(x=100, y=465)

r2 = Radiobutton(root, text='Nuit',
                 variable=v1,
                 font=('Segoe UI', 15, 'bold'),
                 bg='white',
                 fg='#707070',
                 value=2,
                 command=nuit)
r2.place(x=300, y=465)


# text raba3
L4 = Label(root, background='white',
           font=('Segoe UI', 18, 'bold'),
           bg='white',
           fg='#707070',
           text="4. Choisissez le nombre de conducteur")
L4.place(x=30, y=500)
L41 = Label(root, background='white',
            font=('Segoe UI', 12, 'bold'),
            bg='white',
            fg='#707070',
            text=f"Le nombre minimum possible est : {min_Conducteur}")
L41.place(x=30, y=530)

# input yakho
# hna hover


# def ss(event2):
#     input2.config(state=NORMAL)
#     input2.delete(0, 'end')
#     input2.unbind(0, '<FocusIn>')

# hna save input


def ab3at2():
    sad1 = achfa2.get()
    ConducteurCheck(sad1)


achfa2 = IntVar()

input2 = Entry(highlightthickness=1,
               width=30,
               textvariable=achfa2,
               font=('Segoe UI', 25))

input2.place(x=30, y=560)


input2.config(highlightbackground="#707070",
              #   state=DISABLED,
              font=('Segoe UI', 25),
              highlightcolor='#707070')

# input2.insert(0, 'Ecrire le nombre de conducteur ici')
# input1.bind('<FocusIn>', ss)
# button image
img3 = Image.open("assets/valider.png")
re = img3.resize((200, 50))
img3 = ImageTk.PhotoImage(re)

Button(root, image=img3, bd=0, bg="#037EF3",
       activebackground='#ffffff',
       highlightthickness=1,
       command=ab3at2).place(x=575, y=560)

# text raba3
L4 = Label(root, background='white',
           font=('Segoe UI', 12),
           bg='white',
           fg='#707070',
           text=f"Ecrire un chiffre supérieur ou egale à : {min_Conducteur}")
L4.place(x=30, y=620)
# button submit
img4 = Image.open("assets/submit.png")
re = img4.resize((700, 90))
img4 = ImageTk.PhotoImage(re)


def FinalOpe():
    SaveData()
    os.system('python Operationpyomo.py')


Gen = Button(root, image=img4, bd=0, bg='#ffffff',
             activebackground='#ffffff',
             command=FinalOpe)
Gen.place(x=30, y=650)
root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 08:39:52 2024

@author: anyta
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x500")
root.title("ME MAREO!!!!!!!!!!!!!!!")
root.configure(background = "grey")

Foto = ""
def AbrirArchivo():
    global Foto
    Foto = filedialog.askopenfilename(title= "Abriendo imagen", filetypes = (("image files", "*.jpg *.png *.gif"),))
    im = Image.open(Foto)
    img = ImageTk.PhotoImage(im)
    Imagen["image"] = img
    img.close()
    
    
Abrir = Button(root, text="Abrir imagen", bg="purple", command=AbrirArchivo)

Imagen = Label(root, bg="red")

Marear = Button(root, text="Marea la foto", bg="purple")
    
Abrir.place(relx=0.5, rely=0.2, anchor=CENTER)
Imagen.place(relx=0.5, rely=0.5, anchor=CENTER)
Marear.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
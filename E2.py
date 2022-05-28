from tkinter import *

lista=Tk()
etiqueta=Label(text="Listado de mis películas favoritas").pack()
elementos=Listbox(lista)
elementos.insert(1, "Harry Potter")
elementos.insert(2, "Animales Fantásticos")
elementos.insert(3, "El Señor de los Anillos")
elementos.insert(4, "Constantine")
elementos.insert(5, "Star Wars")
elementos.insert(6, "The Mandalorian")

elementos.pack()
lista.mainloop()
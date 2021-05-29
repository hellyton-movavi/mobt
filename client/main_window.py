import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class MainRoot():
    def __init__(self):
        self.root = tk.Tk()
    
        self.name = tk.Label(self.root, text="Имя пользователя")
        self.title_1 = tk.Label(self.root, text="Уровень: ")
        self.title_2 = tk.Label(self.root, text="Опыт: ")

        self.title_3 = tk.Label(self.root, text="Час назад: ")
        self.title_4 = tk.Label(self.root, text="Пользователей: ")
        self.title_5 = tk.Label(self.root, text="Прибыль: ")
        self.title_6 = tk.Label(self.root, text="Баланс: ")


        self.canvas = Canvas(self.root, width=550, height=280)
        self.img = PhotoImage(file="temp.png")      
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)      
        

        self.button_1 = tk.Button(self.root, text="Вышки")
        self.button_2 = tk.Button(self.root, text="Офисы")

        self.now = tk.Label(self.root, text="Сейчас: ")
        self.users = tk.Label(self.root, text="Пользователей: ")
        self.get = tk.Label(self.root, text="Прибыль: ")
        self.balance = tk.Label(self.root, text='Баланс:')

        self.name.grid(row=0, column=1, columnspan=2, sticky=tk.W, padx=10, pady=10)
        self.title_1.grid(row=1, column=1, columnspan=2, sticky=tk.W, padx=10, pady=10)
        self.title_2.grid(row=2, column=1, columnspan=2, sticky=tk.W, padx=10, pady=10)
        
        self.title_3.grid(row=3, column=2, columnspan=2, sticky=tk.W, padx=10, pady=10)
        self.title_4.grid(row=4, column=2, columnspan=2, sticky=tk.W, padx=10, pady=10)
        self.title_5.grid(row=5, column=2, columnspan=2, sticky=tk.W, padx=10, pady=10)
        self.title_6.grid(row=6, column=2, columnspan=2, sticky=tk.W, padx=10, pady=10)

        self.now.grid(row=3, column=8, columnspan=10, sticky=tk.W, padx=10, pady=10)
        self.users.grid(row=4, column=8, columnspan=10, sticky=tk.W, padx=10, pady=10)
        self.get.grid(row=5, column=8, columnspan=10, sticky=tk.W, padx=10, pady=10)
        self.balance.grid(row=6, column=8, columnspan=10, sticky=tk.W, padx=10, pady=10)
        

        self.canvas.grid(row=10, column=2, columnspan=10, rowspan=10, sticky=tk.W, padx=10, pady=10)

        self.button_1.grid(row=0, column=10, columnspan=2, sticky=tk.W)
        self.button_2.grid(row=1, column=10, columnspan=2, sticky=tk.W)
        
        self.root.mainloop()

mr = MainRoot()

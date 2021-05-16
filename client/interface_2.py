import tkinter as tk
import requests as rq

SERVER_ADDRESS = 'https://maxmine2.pythonanywhere.com'


class App():
    def __init__(self):
        self.root = tk.Tk()

        self.bt_come = tk.Button(self.root, text='Log in')
        self.bt_reg = tk.Button(self.root, text='Registration')

        #  Привязка к функциям
        self.bt_come.bind("<Button-1>", self.login)
        self.bt_reg.bind("<Button-1>", self.reg)

        #  Распаковка
        self.bt_come.pack()
        self.bt_reg.pack()

        self.root.mainloop()

    def check(self, event):
        #  Здесь нужно проверять то, что было введено пользователем
        nick = self.en_1.get()
        pw = self.en_2.get()
        mail = self.en_3.get()

        if nick == '' or pw == '' or mail == '':
            self.lb_info.config(text='Please, fill all of the fields')
        else:
            if '@' in mail and '.' in mail[mail.index('@'):]:
                self.lb_info.config(text='Ok')

                self.send_reqinfo(nick, pw, mail)
                popup = Popup(
                    f"You've been successfully registrated. To continue registration process, please follow the link in the e-mail. E-mail was send to {mail}", self.root)
                popup.show()
            else:
                self.lb_info.config(text='Incorrect mail')

    def login(self, event):
        """Вход"""
        self.root.withdraw()  # Скрываем главное окошко

        self.log_in = tk.Toplevel(self.root)
        self.log_in.title('Log in')

        self.lb_nick = tk.Label(self.log_in, text="Enter nick:")
        self.en_nick = tk.Entry(self.log_in)

        self.lb_psw = tk.Label(self.log_in, text="Enter password:")
        self.en_psw = tk.Entry(self.log_in, show='*')

        self.check = tk.Button(self.log_in, text="Submit")
        self.check.bind('<Button-1>', self.checking)

        self.information = tk.Label(self.log_in, text="")

        #  Проявить поля для ввода nick
        self.en_nick.grid(row=0, column=1, columnspan=2,
                       sticky=tk.W, padx=10, pady=10)
        self.lb_nick.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        #  Проявить поля для ввода password
        self.en_psw.grid(row=1, column=1, columnspan=2,
                       sticky=tk.W, padx=10, pady=10)
        self.lb_psw.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

        #  Проявить кнопку для отправления данных и кнопку инфы
        self.check.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=10, pady=10)
        self.information.grid(row=3, column=0, sticky=(
            tk.W, tk.E), padx=10, pady=10)

    def checking(self, event):
        print('Проверка')

    def reg(self, event):
        """Регистрация"""
        self.root.withdraw()  # Скрываем главное окошко

        self.reg = tk.Toplevel(self.root)
        self.reg.title('Registration')

        self.lb_info = tk.Label(self.reg, text="")

        self.lb_1 = tk.Label(self.reg, text="Enter nick:")
        self.en_1 = tk.Entry(self.reg)

        self.lb_2 = tk.Label(self.reg, text="Enter password:")
        self.en_2 = tk.Entry(self.reg, show='*')

        self.lb_3 = tk.Label(self.reg, text="Enter mail:")
        self.en_3 = tk.Entry(self.reg)

        self.bt_back = tk.Button(self.reg, text="Go home")
        self.bt_back.bind("<Button-1>", self.main_root_from_reg)

        self.bt = tk.Button(self.reg, text="Submit")
        self.bt.bind('<Button-1>', self.check)

        #  Проявить поля для ввода nick
        self.en_1.grid(row=0, column=1, columnspan=2,
                       sticky=tk.W, padx=10, pady=10)
        self.lb_1.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        #  Проявить поля для ввода password
        self.en_2.grid(row=1, column=1, columnspan=2,
                       sticky=tk.W, padx=10, pady=10)
        self.lb_2.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

        #  Проявить поля для ввода почты
        self.en_3.grid(row=2, column=1, columnspan=2,
                       sticky=tk.W, padx=10, pady=10)
        self.lb_3.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

        #  Проявить кнопку для отправления данных
        self.bt.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=10, pady=10)
        self.lb_info.grid(row=3, column=0, sticky=(
            tk.W, tk.E), padx=10, pady=10)

        #  Проявить кнопку для возвращения в главное меню
        self.bt_back.grid(row=4, column=0, sticky=(
            tk.W, tk.E), padx=10, pady=10)

    def send_reqinfo(self, nick, pw, mail):

        response = Login.register(nick, pw, mail)
        if response == 0:
            # TODO: Сказать пользователю "Зайдите на почту" =)

            pass
        elif response == -1:
            # TODO: Какая-то проблема, мол, попробуйте позже или обновите приложение
            pass
        elif response == -2:
            # TODO: Тоже проблема, но уж точно на стороне сервера
            pass
        self.main_root_from_reg(self)

    def main_root_from_reg(self, event):
        #  Показать главное
        self.root.deiconify()

        # Спрятать побочное
        self.reg.withdraw()


class Popup():
    def __init__(self, text, root):
        self.text = text
        self.root = root

    def show(self):
        self.popup = tk.Toplevel(self.root)
        self.popup.title('popup')
        self.lb = tk.Label(self.popup, text=self.text)
        self.lb.pack()


class Login():
    @staticmethod
    def register(mail, nick, pw):
        data = {
            "mail": mail,
            "nick": nick,
            "password": pw}

        u_save = rq.post(SERVER_ADDRESS + "/api/reg", data)
        print(u_save)
        recv = dict(eval(u_save.text))
        print(recv)
        if recv.status_code == 200:
            return 0, recv
        elif 400 <= recv.status_code < 500:
            return -1, recv
        elif recv.status_code >= 500:
            return -2, recv

    @staticmethod
    def login(nick, pw):
        data = {
            "nick": nick,
            "password": pw
        }
        recv = rq.post(SERVER_ADDRESS + '/api/login')
        if recv.status_code == 200:
            data = dict(eval(recv.texts))
            if data['status'] == 'error':
                return -1, data['error']

            else return 0


app = App()

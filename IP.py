from tkinter import *
from tkinter import ttk
import tkinter as tk
import socket
from requests import get
from tkinter.commondialog import Dialog

# color #
cor5 = "#123c80"
cor3 = "#00e03c"
cor2 = "#ffffff"
cor1 = "#0000FF"

tela = Tk()
tela.geometry("650x450+365+157")
tela.minsize(120, 1)
tela.maxsize(1370, 749)
tela.resizable(1,  1)
tela.title("IP")
tela.configure(background="#369f33")

# messagebox #

__all__ = ["showinfo", "showwarning", "showerror",
           "askquestion", "askokcancel", "askyesno",
           "askyesnocancel", "askretrycancel"]

# icons #
WARNING = "warning"


# types #
OK = "ok"


class Message(Dialog):
    "A message box"

    command = "tk_messageBox"


def show(title=None, message=None, icon=None, type=None, **options):
    if icon and "icon" not in options:
        options["icon"] = icon
    if type and "type" not in options:
        options["type"] = type
    if title:
        options["title"] = title
    if message:
        options["message"] = message
    res = Message(**options).show()


def showwarning(title=None, message=None, **options):
    "Show a warning message"
    return show(title, message, WARNING, OK, **options)


if __name__ == "__main__":
    print("warning", showwarning(
        "Aviso", "verifique o status da conexão do seu dispositivo para prosseguir deve está conectado em rede."))


# FRAME #
Frame1 = tk.Frame(tela)
Frame1.place(relx=0.05, rely=0.156,
             relheight=0.567, relwidth=0.858)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#ffffff")

Frame2 = tk.Frame(tela)
Frame2.place(relx=0.400, rely=0.160,
             relheight=0.100, relwidth=0.490)
Frame2.configure(relief='groove')
Frame2.configure(borderwidth="2")
Frame2.configure(relief="groove")
Frame2.configure(background="#00e03c")

Frame2_1 = tk.Frame(tela)
Frame2_1.place(relx=0.400, rely=0.353,
               relheight=0.100, relwidth=0.490)
Frame2_1.configure(relief='groove')
Frame2_1.configure(borderwidth="2")
Frame2_1.configure(relief="groove")
Frame2_1.configure(background="#00e03c")
Frame2_1.configure(highlightbackground="#d9d9d9")
Frame2_1.configure(highlightcolor="black")

Frame2_1_1 = tk.Frame(tela)
Frame2_1_1.place(relx=0.400, rely=0.580,
                 relheight=0.100, relwidth=0.490)
Frame2_1_1.configure(relief='groove')
Frame2_1_1.configure(borderwidth="2")
Frame2_1_1.configure(relief="groove")
Frame2_1_1.configure(background="#00e03c")
Frame2_1_1.configure(highlightbackground="#d9d9d9")
Frame2_1_1.configure(highlightcolor="black")


Label1 = tk.Label(tela)
Label1.place(relx=0.10, rely=0.160, height=41, width=175)
Label1.configure(activeforeground="#0000ff")
Label1.configure(background="#ffffff")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(
    font="-family {Segoe UI Semibold} -size 15 -weight bold")
Label1.configure(foreground="#000000")
Label1.configure(text='''Nome da Maquina:''')

Label1_1 = tk.Label(tela)
Label1_1.place(relx=0.10, rely=0.353, height=41, width=175)
Label1_1.configure(activebackground="#f9f9f9")
Label1_1.configure(activeforeground="black")
Label1_1.configure(background="#ffffff")
Label1_1.configure(disabledforeground="#a3a3a3")
Label1_1.configure(
    font="-family {Segoe UI Semibold} -size 15 -weight bold")
Label1_1.configure(foreground="#000000")
Label1_1.configure(highlightbackground="#d9d9d9")
Label1_1.configure(highlightcolor="black")
Label1_1.configure(text='''IP Interno:''')

Label1_1_1 = tk.Label(tela)
Label1_1_1.place(relx=0.10, rely=0.580, height=41, width=175)
Label1_1_1.configure(activebackground="#f9f9f9")
Label1_1_1.configure(activeforeground="black")
Label1_1_1.configure(background="#ffffff")
Label1_1_1.configure(cursor="fleur")
Label1_1_1.configure(disabledforeground="#a3a3a3")
Label1_1_1.configure(
    font="-family {Segoe UI Semibold} -size 15 -weight bold")
Label1_1_1.configure(foreground="#000000")
Label1_1_1.configure(highlightbackground="#d9d9d9")
Label1_1_1.configure(highlightcolor="black")
Label1_1_1.configure(text='''IP Externo:''')

todos_valores = ""
todos_valores3 = ""
todos_valores4 = ""


def buscar_ip():
    global todos_valores, todos_valores3, todos_valores4
    maquina = socket.gethostname()
    ipInterno = socket.gethostbyname(maquina)
    ipExterno = get('https://api.ipify.org').text
    todos_valores = todos_valores + str(maquina)
    valores_texto.set(todos_valores)
    todos_valores3 = todos_valores3 + str(ipInterno)
    valores_texto3.set(todos_valores3)
    todos_valores4 = todos_valores4 + str(ipExterno)
    valores_texto4.set(todos_valores4)


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valores_texto.set("")
# function para limpar tela#


def limpar_tela():
    global todos_valores, todos_valores3, todos_valores4
    todos_valores = ""
    todos_valores3 = ""
    todos_valores4 = ""
    valores_texto.set("")
    valores_texto3.set("")
    valores_texto4.set("")


valores_texto = StringVar()
valores_texto3 = StringVar()
valores_texto4 = StringVar()

tela1 = Label(Frame2, textvariable=valores_texto, width=26, height=2, padx=1,
              relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 16'), bg=cor3, fg=cor2)
tela1.place(x=0, y=0)


tela2 = Label(Frame2_1, textvariable=valores_texto3, width=26, height=2, padx=1,
              relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 16'), bg=cor3, fg=cor2)
tela2.place(x=0, y=0)

tela3 = Label(Frame2_1_1, textvariable=valores_texto4, width=26, height=2, padx=1,
              relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 16'), bg=cor3, fg=cor2)
tela3.place(x=0, y=0)

Button1 = tk.Button(tela)
Button1.place(relx=0.118, rely=0.824, height=34, width=77)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#369f33")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#FFFFFF")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''BUSCAR''')
Button1.configure(command=buscar_ip)

Button1_1 = tk.Button(tela)
Button1_1.place(relx=0.641, rely=0.824, height=34, width=77)
Button1_1.configure(activebackground="#ececec")
Button1_1.configure(activeforeground="#000000")
Button1_1.configure(background="#369f33")
Button1_1.configure(disabledforeground="#a3a3a3")
Button1_1.configure(foreground="#FFFFFF")
Button1_1.configure(highlightbackground="#d9d9d9")
Button1_1.configure(highlightcolor="black")
Button1_1.configure(pady="0")
Button1_1.configure(text='''LIMPAR''')
Button1_1.configure(command=limpar_tela)


tela.mainloop()

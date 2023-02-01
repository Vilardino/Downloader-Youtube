from functools import partial
from tkinter.scrolledtext import ScrolledText

from sup import *
from tkinter import *


def submeter():
    button_mp3["state"] = DISABLED
    button1["state"] = DISABLED
    download(link.get(), mp3.get())
    button1["state"] = NORMAL
    button_mp3["state"] = NORMAL


window = Tk()
# add widgets here

window.title('Donwload youtube')
window.maxsize(1200, 1200)
window.config(bg="skyblue")

# trava tamanho da tela
window.resizable(0, 0)

# Create left and right frames
left_frame = Frame(window, width=400, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=7, pady=7)

right_frame = Frame(window, width=400, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=7, pady=7)

# Cria Link

Label(left_frame, text="Link", font='Times 15').grid(row=0, column=0, padx=5, pady=5)
link = StringVar(value='')
e_link = Entry(left_frame, width=55, textvariable=link) \
    .grid(row=0, column=1, padx=7, pady=7, columnspan=3, ipady=5)

# Trava tamanho do frame
left_frame.grid_propagate(0)

# Botoes de checagem para mp3 e lista
mp3 = BooleanVar(value=False)
button_mp3 = Checkbutton(left_frame, text="mp3", variable=mp3, font='Times 15', onvalue=True, offvalue=False)
button_mp3.grid(row=1, column=0, padx=7, pady=7, columnspan=2)

# log
log_show = ScrolledText(left_frame, undo=True, width=45, height=15)
log_show.grid(row=2, column=0, padx=7, pady=7, columnspan=4)

# Sair e Submeter

button1 = Button(left_frame, text="Submeter", command=submeter)
button1.grid(row=3, column=0, padx=7, pady=7, columnspan=2, sticky=W + E)

button2 = Button(left_frame, text="Fechar", command=partial(exit))
button2.grid(row=3, column=2, padx=7, pady=7, columnspan=2, sticky=W + E)

window.mainloop()

from os import listdir, remove
from moviepy.editor import *


# youtube nao baixa em mp3 entao...


def conversor_mp3():
    caminho = './converter'
    lista_arqs = [arq for arq in listdir(caminho)]
    print(lista_arqs)

    for i in lista_arqs:
        audio = AudioFileClip("./converter/" + i)
        audio.write_audiofile("./convertidos/" + i.rstrip('.mp4') + '.mp3')
        remove('./converter/' + i)
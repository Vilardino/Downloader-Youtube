import downyt
import para_html
import conversor


def download(html, mp3, lista):
    if mp3 and lista:
        para_html.gen_html(html)
        downyt.download_list_mp3()
        conversor.conversor_mp3()
    elif mp3:
        downyt.download_mp3(html)
        conversor.conversor_mp3()
    elif lista:
        para_html.gen_html(html)
        downyt.download_list()
    else:
        downyt.download(html)

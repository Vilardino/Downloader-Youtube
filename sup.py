import downyt
import d_selenium
import conversor


def download(html, mp3, lista):
    if mp3 and lista:
        d_selenium.gen_html(html)
        downyt.download_list_mp3()
        conversor.conversor_mp3()
    elif mp3:
        downyt.download_mp3(html)
        conversor.conversor_mp3()
    elif lista:
        d_selenium.gen_html(html)
        downyt.download_list()
    else:
        downyt.download(html)

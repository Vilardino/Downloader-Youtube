import downyt
import d_selenium
import conversor
from pytube import Playlist, YouTube


def download(html, mp3):
    converter = './converter'
    videos = "./videos"

    if mp3 and 'list' in html:
        p = Playlist(html)
        for url in p.videos:
            url.streams.filter(subtype='mp4').get_lowest_resolution().download(converter)
            print("Preparamos o para futura conversao para mp3: " + url.title)
        conversor.conversor_mp3()
        print("Baixamos a Playlist mp3")

    elif mp3:
        p = YouTube(html)
        p.streams.filter(subtype='mp4').get_lowest_resolution().download(converter)
        conversor.conversor_mp3()
        print("Baixamos o mp3: " + p.title)

    elif 'list' in html:
        p = Playlist(html)
        print(p)
        for url in p.videos:
            print(url)
            url.streams.filter(subtype='mp4').get_highest_resolution().download(videos)
            print("Baixamos: " + p.title)

    else:
        p = YouTube(html)
        p.streams.filter(subtype='mp4').get_highest_resolution().download(videos)
        print("Baixamos: " + p.title)

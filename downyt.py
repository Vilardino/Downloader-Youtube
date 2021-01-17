import pytube


def download_list_mp3():
    with open("links.txt") as file:
        for link in file:
            try:
                yt = pytube.YouTube(link)
                video = yt.streams.filter(mime_type="audio/mp4").first()
                path = './converter'
                video.download(path)
                print("Baixamos: " + yt.title)
            except:
                print('Deu BO meu consagrado ' + link)


def download_mp3(link):
    try:
        yt = pytube.YouTube(link)
        video = yt.streams.filter(mime_type="audio/mp4").first()
        path = './converter'
        video.download(path)
        print("Baixamos: " + yt.title)
    except:
        print('Deu BO meu consagrado ' + link)


def download_list():
    with open("links.txt") as file:
        for link in file:
            try:
                yt = pytube.YouTube(link)
                video = yt.streams.filter(mime_type="video/mp4").first()
                path = './videos'
                video.download(path)
                print("Baixamos: " + yt.title)
            except:
                print('Deu BO meu consagrado ' + link)


def download(link):
    try:
        yt = pytube.YouTube(link)
        video = yt.streams.filter(mime_type="video/mp4").first()
        path = './videos'
        video.download(path)
        print("Baixamos: " + yt.title)
    except:
        print('Deu BO meu consagrado ' + link)

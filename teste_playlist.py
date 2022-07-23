from pytube import Playlist

p = Playlist("https://www.youtube.com/playlist?list=PLXP-A8qzEKQO17_xeREHDZBkMF0EdL0D0")

for url in p.videos:
    print(url.streams.filter(subtype='mp4').get_lowest_resolution())
    url.streams.filter(subtype='mp4').get_highest_resolution().download()

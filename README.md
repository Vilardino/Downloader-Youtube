# Downloader-Youtube

## Pode baixar um único vídeo ou uma playlist, sendo eles mp3 ou não

### Crie uma pasta chamada *converter*, uma chamada *convertidos* e o arquivo links.txt

#### Bibliotecas necessárias:
- BeautifulSoup4 -obsoleto
- requests
- tkinter
- functools
- pytube3
- os
- moviepy.editor 
- selenium

#### Bibliotecas necessárias:
Modifeque extract.py

```parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)``` -> ```parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)```
from pytubefix import YouTube, Playlist

opcion = int(input("Quiere descargar una cancion o playlist? (1 o 2): "))
if (opcion == 1):
    url = input("Ingrese la url de la canción a descargar:\n")
    yt = YouTube(url)
    ytName = yt.title
    print("Descargando '",ytName,"'")          
    yt = yt.streams.get_audio_only()
    yt.download(r'H:\Musica', mp3=True)
    print(ytName, "Descargado.")

if (opcion == 2):
    url = input("Ingrese la url de la playlist a descargar:\n")
    yt = Playlist(url)
    for video in yt.videos:
        ys = video.streams.get_audio_only() 
        ytName = ys.title
        print("Descargando '",ytName,"'")
        ys.download(r'H:\Musica', mp3=True)
        print(ytName, "Descargado.")

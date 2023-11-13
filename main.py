# V 1.0 🐢🐢🐢

from pytube import YouTube as yt1
from pytube import Playlist

def download_video(url):
    try:
        yt = yt1(url)
        choice = input('Czy to playlista(p) czy odcinek(o)?')
        if choice == 'p':
            p = Playlist(url)

            print(f'Pobieram {p.title}')
            for video in p.videos:
                print(f'Pobieram {video.title}')
                video.streams.filter(progressive='True', file_extension='mp4').order_by('resolution').desc().first().download()
                print(f'Film {video.title} został pobrany pomyślnie. ')
                

        elif choice == 'o':
            print(yt.streams)
            yt.streams.filter(progressive='True', file_extension='mp4').order_by('resolution').desc().first().download()
            print(f'Film {yt.title} został pobrany pomyślnie')
        else:
            print('Wybrano nieodpowiedni znak')


    except Exception as e:
        print(f'Wystąpił błąd podczas pobierania filmu: {e}')
url = input('Podaj url filmu: ')
download_video(url)
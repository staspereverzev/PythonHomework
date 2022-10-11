import pytube

def download_yt(url):
    # url = 'http://youtube.com/watch?v=2lAe1cqCOXo'
    link = pytube.YouTube(url)

    stream = link.streams.get_by_itag(22)
    stream.download()

    return (f'Скачано')
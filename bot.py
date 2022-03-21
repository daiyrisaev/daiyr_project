import re
import requests
from bs4 import BeautifulSoup
response= requests.get('https://www.vgmusic.com/music/console/nintendo/nes/')
html_code_text=response.text
soup=BeautifulSoup(html_code_text,'html.parser')
print(f'{soup}')
print(dir(soup))
print(f'{html_code_text=}')


def download_track(track_element):
    track_title = track_element.text.strip().replace('/', '-')
    download_url = f'https://www.vgmusic.com/music/console/nintendo/nes/{track_element["href"]}'
    file_name = f'{track_title}.mid'
    r = requests.get(download_url, allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(r.content)


attrs = {'href': re.compile(r'\.mid$')}
songs = soup.find_all('a', attrs=attrs)
print(len(songs), 'Песен мы получаем')
for song in songs:
    print(song)


first_song = songs[100]
print(first_song)
download_track(first_song)

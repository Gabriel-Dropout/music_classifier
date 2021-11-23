#유튜브에서 음원을 찾아 audio.mp3라는 이름으로 다운로드합니다
from pytube import YouTube

def get_audio(id):
    if not id.startswith('https://www.youtube.com/watch?v='):
        id = 'https://www.youtube.com/watch?v=' + id
    yt = YouTube(id)

    print(yt.streams.filter(only_audio=True).first())

    # 특정영상 다운로드
    yt.streams.filter(only_audio=True, file_extension='mp4').first().download(filename="audio.mp3")

if(__name__=='__main__'):
    get_audio("https://www.youtube.com/watch?v=DXGe4mn_2Js")
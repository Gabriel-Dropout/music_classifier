#원래 파일(mp3)를 30초로 자르고 wav로 변환하여 반환합니다
from pydub import AudioSegment

def mp3_to_wav(path):
    sound=AudioSegment.from_file(path)
    if(len(sound)>30*1000):
        winl=10*1000
        hwinl=winl/2
        audl=len(sound)
        first = (audl-winl)/4
        second = audl/2
        third = (3*audl-winl)/4
        sound = sound[first-hwinl:first+hwinl] + sound[second-hwinl:second+hwinl] + sound[third-hwinl:third+hwinl]
        
    return sound.export('audioFixed.wav', format="wav")

if(__name__=='__main__'):
    print(mp3_to_wav('audio.mp3'))
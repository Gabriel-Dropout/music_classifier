import librosa
import numpy as np
import joblib
import convert

scaler = joblib.load('/Backend/scaler.pkl')

def load(path):
    path = convert.mp3_to_wav(path)
    return librosa.load(path)

def extract(y, sr):
    feature = []
    #chroma_stft
    chroma_stft = np.abs(librosa.feature.chroma_stft(y))
    feature.append(np.mean(chroma_stft))
    feature.append(np.var(chroma_stft))
    #rms
    rms = librosa.feature.rms(y)
    feature.append(np.mean(rms))
    feature.append(np.var(rms))
    #spectral centroid
    spectral_centroid = librosa.feature.spectral_centroid(y, sr=sr)[0]
    feature.append(np.mean(spectral_centroid))
    feature.append(np.var(spectral_centroid))
    #spectral bandwidth
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y, sr=sr)[0]
    feature.append(np.mean(spectral_bandwidth))
    feature.append(np.var(spectral_bandwidth))
    #rolloff
    spectral_rolloff = librosa.feature.spectral_rolloff(y, sr=sr)[0]
    feature.append(np.mean(spectral_rolloff))
    feature.append(np.var(spectral_rolloff))
    #zero crossing rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y, pad=False)
    feature.append(np.mean(zero_crossing_rate))
    feature.append(np.var(zero_crossing_rate))
    #harmony & preceptr
    y_harm, y_perc = librosa.effects.hpss(y)
    feature.append(np.mean(y_harm))
    feature.append(np.var(y_harm))

    feature.append(np.mean(y_perc))
    feature.append(np.var(y_perc))
    #tempo
    tempo, _ = librosa.beat.beat_track(y, sr=sr)
    feature.append(tempo)
    #mfcc 1~20
    mfcc = librosa.feature.mfcc(y, sr=sr)
    for i, mfcc_i in enumerate(mfcc):
        feature.append(np.mean(mfcc_i))
        feature.append(np.var(mfcc_i))
    
    feature=scaler.transform([feature]).ravel()
    return feature

if(__name__=='__main__'):
    a, b = load('audio.mp3')
    print(extract(a, b))
from flask import Flask, render_template, request, redirect, url_for, Response
from flask_cors import CORS
 
import os

#백엔드 연산 모듈
import classifier
import extract_feature as ef
from audio_from_youtube import get_audio

app = Flask(__name__)
CORS(app)

#음악 업로드 요청
@app.route('/upload', methods = ['POST'])
def upload():
    result = request.files
    
    if 'file' not in result:
        return 'File is missing', 404
    
    file = result.get('file')
    
    y, sr = ef.load(file)
    feature = ef.extract(y, sr)
    pred = classifier.predict(feature)
    my_res = Response(pred)
    return my_res;

#음악 검색 요청
@app.route('/search', methods = ['GET'])
async def search():
    vid = request.args.to_dict().get("v", 'DXGe4mn_2Js')
    print(vid)
    get_audio(vid)
    y, sr = ef.load("audio.mp3")
    feature = ef.extract(y, sr)
    pred = classifier.predict(feature)
    print(pred)
    my_res = Response(pred)
    return my_res;
 
@app.route('/', methods = ['GET'])
def main():
    return "asd";
 
if __name__ == '__main__':
    app.run(port=5000)
from flask import Flask, render_template, request, redirect, url_for, Response
from flask_cors import CORS
 
import os

import classifier
import extract_feature as ef

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods = ['POST'])
def upload():
    result = request.files
    if 'file' not in result:
        print("NO")
        return 'File is missing', 404
    
    file = result.get('file')
    
    #file.save("asdasdasd.wav")
    
    y, sr = ef.load(file)
    feature = ef.extract(y, sr)
    pred = classifier.predict(feature)
    #pred="asd Hello!"
    my_res = Response(pred)
    return my_res;
 
@app.route('/', methods = ['GET'])
def main():
    return "asd";
 
if __name__ == '__main__':
    app.run(port=5000)
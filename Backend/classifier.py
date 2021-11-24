#학습된 모델을 바탕으로 장르를 예측합니다
import joblib

model = joblib.load('/Backend/svc.pkl')

def predict(data):
    return model.predict([data])
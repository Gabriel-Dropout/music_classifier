import joblib

model = joblib.load('Backend/wow.pkl')

def predict(data):
    return model.predict([data])

if(__name__=='__main__'):
    import pandas as pd
    import numpy as np

    #데이터 로드 함수를 정의합니다. 필요한 레이블을 추출하는 1차 전처리 단계를 거칩니다.
    def load_data(path='features_3_sec.csv'):
        #데이터 읽기
        data = pd.read_csv(path)
        
        #인풋 데이터 추출
        data_input = data.drop(columns=['filename', 'length', 'label']).to_numpy()
        #타깃 데이터 추출
        data_target = data['label'].to_numpy()
        
        #정규화
        #from sklearn.preprocessing import MinMaxScaler
        #scaler=MinMaxScaler()
        from sklearn.preprocessing import StandardScaler
        scaler=StandardScaler()
        scaler.fit(data_input)
        data_input=scaler.transform(data_input)
        
        #반환
        return data_input, data_target

    data_input2, data_target2 = load_data(path='Data/features_30_sec.csv')
    import random
    idx = random.randrange(0,len(data_target2))
    rand_input = data_input2[idx]
    rand_target = data_target2[idx]
    print(predict(rand_input), rand_target)
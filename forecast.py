import json
import os

import numpy as np
from keras.models import load_model

# model = load_model('E:\\models\\25042024-223230-e1.h5')
#
# VO2Data=pd.read_csv("data/processedData.csv")
# newData = VO2Data[['energy', 'HR[bpm]']]
# value=newData.iloc[0:49,:].values.reshape(1,49,2)
# prediction = model.predict(value)
# print(prediction)

#读取所需参数
from core.data_processor import DataLoader


def normalise_windows(window_data):
    # newData=[]
    # for i in range(len(window_data)):
    #     newData.append([window_data[i],0])
    # window_data=newData
    # window_data=np.array(window_data).iloc[:,:].reshape(1,10,2)
    #normalised_data = []
    normalised_window = []
    for window in window_data:
        normalised_col = ((float(window) / float(window_data[0])) - 1)
        normalised_window.append([normalised_col,0])
        # normalised_window = []
        # for col_i in range(window.shape[1]):
        #     normalised_col = [((float(p) / float(window[0, col_i])) - 1) for p in window[:, col_i]]
        #     normalised_window.append(normalised_col)
        #normalised_window = np.array(normalised_window).T
        #normalised_data.append(normalised_window)
    return normalised_window[0:9]

def predictSingle(modelName,data):
    model = load_model('E:\\models\\' + modelName + '.h5')#加载模型
    #归一化预测数据
    x_normalize=normalise_windows(data)
    print(x_normalize)

    #反归一化结果数据
    prediction = model.predict(np.array([x_normalize]))

    print(prediction[0][0])
    return prediction[0][0]

def predict(modelName,normal=False):#modelPath,predictData
    configs = json.load(open('config_2.json', 'r'))
    if not os.path.exists(configs['model']['save_dir']): os.makedirs(configs['model']['save_dir'])
    #读取数据
    data = DataLoader(
        os.path.join('data', configs['data']['preFileName']),
        configs['data']['train_test_split'],
        configs['data']['columns']
    )
    data1 = DataLoader(
        os.path.join('data', configs['data']['filename']),
        configs['data']['train_test_split'],
        configs['data']['columns']
    )
    x_normalize, y_normalize = data.get_test_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise1']
    )
    for col_i in range(x_normalize.shape[0]):
        for col_j in range(x_normalize[col_i].shape[0]):
            x_normalize[col_i][col_j][0] = 0

    x, y = data1.get_test_data(
        seq_len=configs['data']['sequence_length'],
        normalise=configs['data']['normalise1']
    )
    x_pre=x
    if normal:
        x_pre=x_normalize
    model = load_model('E:\\models\\'+modelName+'.h5')
    # print('type(x_normalize)')
    # print(type(x_normalize))
    prediction = model.predict(x_pre)
    print(prediction)
    if normal:
        dePrediction=denormalize_windows(x,prediction)
        prediction=dePrediction
        print(dePrediction)
    plot_results(prediction, y,'results_3.png')

def denormalize_windows(x_test,y):
    new_y=[]
    for col_i in range(1,x_test.shape[0]):
        new_y.append([x_test[col_i][0][0]*(x_test[col_i-1][0][0]+1)[0]])
    print(type(y))
    print(y.shape)
    newData=np.array(new_y)
    print(type(newData))
    print(newData.shape)
    print(newData)
    # print("反归一化")
    # print(new_y)
    # print(np.array(new_y))
    return newData


modelName='test'
heartRate=[85,86,86,85,83,82,83,84,82,82]
#predict(modelName,False)
#predictSingle(modelName,heartRate)
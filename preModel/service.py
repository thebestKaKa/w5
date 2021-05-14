import os
import numpy as np

import MyNN.Layer as layer
import MyNN.Activation as active
import MyNN.Optim as optim
import MyNN.Network as net
import MyNN.LossFunc as lfc

import time
from flask import Flask, request, url_for, render_template, redirect, jsonify
import json


def inputVec(warningNum, timeLim, freqLim):
    ret = warningNum
    temp = timeLim
    cnt_time = 0
    cnt_freq = 0
    while 1:
        temp = int(temp / 2)
        if temp != 0:
            ret += 1
            cnt_time += 1
        else:
            ret += 1
            cnt_time += 1
            break
    temp = freqLim
    while 1:
        temp = int(temp / 2)
        if temp != 0:
            ret += 1
            cnt_freq += 1
        else:
            ret += 1
            cnt_freq += 1
            break
    return ret, cnt_time, cnt_freq


def inputVec_simple(warningNum, timeLim, freqLim):
    return int(warningNum + 2), 1, 1


def inputTransfer(warningNum, timeLim, freqLim, vecSize, timeSize, freqSize):
    ret = np.zeros(vecSize, dtype=int)
    ret[warningNum] = 1
    temp = timeLim
    i = 1
    while 1:
        if temp != 0:
            ret[vecSize - freqSize - i] = int(temp % 2)
            temp = int(temp / 2)
            i += 1
        else:
            break
    temp = freqLim
    i = 1
    while 1:
        if temp != 0:
            ret[vecSize - i] = int(temp % 2)
            temp = int(temp / 2)
            i += 1
        else:
            break
    return ret


def inputTransfer_simple(warningNum, timeLim, freqLim, vecSize, timeSize, freqSize):
    ret = np.zeros(vecSize, dtype=int)
    ret[warningNum] = 1
    ret[vecSize - 2] = timeLim
    ret[vecSize - 1] = freqLim

    return ret


MAXWARNINGNUM = 3
MAXTIME = 7
MAXFREQ = 7
vecSize, timeSize, freqSize = inputVec_simple(MAXWARNINGNUM, MAXTIME, MAXFREQ)
WarningList = ['Attack', 'Unsafe', 'USB']
DataBase = []

app = Flask(__name__)


@app.route('/MLP', methods=['POST'])
def methods():
    tpData = request.get_data()
    allData = json.loads(tpData)
    warningInf = allData['warningInf']
    targetIP = allData['targetIP']
    targetPort = allData['targetPort']
    t = int(time.time())

    warning_index = IP_index = port_index = 0

    for i in range(MAXWARNINGNUM):
        if warningInf == WarningList[i]:
            warning_index = i

    flag = True
    for i in range(len(DataBase)):
        if DataBase[i][0] == warning_index and DataBase[i][1] == targetIP and DataBase[i][2] == targetPort:

            stampSets = DataBase[i][3]
            tempTime = np.zeros(MAXTIME)
            t_flag = True
            for j in range(MAXTIME):
                if stampSets[j] == 0:
                    t_flag = False
                    cnt = 0
                    for k in range(j):
                        if stampSets[k] - t <= 42:
                            tempTime[cnt] = stampSets[k]
                            cnt += 1
                    tempTime[cnt] = t
                    cnt += 1
                    DataBase[i][3] = tempTime
                    print(DataBase[i][3])
                    if cnt == 0:
                        freq = 1
                        timeNum = 1
                    else:
                        freq = 7 - int((tempTime[cnt - 1] - tempTime[0]) / cnt)
                        if freq == 0:
                            freq = 1
                        timeNum = cnt
                        data = inputTransfer_simple(warning_index, timeNum, freq, vecSize, timeSize, freqSize)
                        break
            if t_flag:
                data = inputTransfer_simple(warning_index, MAXTIME, MAXFREQ, vecSize, timeSize, freqSize)
            flag = False
            break

    if flag:
        temp = np.zeros(MAXTIME)
        temp[0] = t
        DataBase.append([warning_index, targetIP, targetPort, temp])
        data = inputTransfer_simple(warning_index, 1, 1, vecSize, timeSize, freqSize)
        print(DataBase)
    MLP = net.Network()
    MLP.load()
    ret = MLP.forward(data)
    ret = np.where(ret == np.max(ret))[0][0]

    return str(ret)


if __name__ == "__main__":
    app.run(debug=True)

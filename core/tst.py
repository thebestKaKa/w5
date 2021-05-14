import requests
import time
import json
from flask import Flask,request,url_for,render_template,redirect,jsonify

# ["Attack","Unsafe","USB"]

testData = [
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
    '{"warningInf":"Unsafe","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
]

url = "http://127.0.0.1:5000/MLP"


for i in range(len(testData)):
    time.sleep(5)
    res = requests.post(url=url, data=testData[i])
    lv = int(res.text)
    print(res.text)  # lv
    tpData = json.loads(testData[i])
    # print(tpData)
    # print(tpData['warningInf'])
    headers = {
        "Content-Type": "application/json"
    }
    if tpData['warningInf'] == 'Attack' and lv == 0:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "2062b080-b464-11eb-98e4-8590585d6e25",
            "text": tpData['targetIP']
        }
    elif tpData['warningInf'] == 'Attack' and lv == 1:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "2062b080-b464-11eb-98e4-8590585d6e25",
            "text": tpData['targetIP']
        }
    elif tpData['warningInf'] == 'Attack' and lv == 2:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "2062b080-b464-11eb-98e4-8590585d6e25",
            "text": tpData['targetIP']
        }
    elif tpData['warningInf'] == 'Unsafe' and lv == 0:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "9bbe5640-b45e-11eb-98e4-8590585d6e25",
            "text": tpData['targetPort']
        }
    elif tpData['warningInf'] == 'Unsafe' and lv == 1:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "f87f69b0-b45d-11eb-98e4-8590585d6e25",
            "text": tpData['targetPort']
        }
    elif tpData['warningInf'] == 'Unsafe' and lv == 2:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "56dad6c0-b45e-11eb-98e4-8590585d6e25",
            "text": tpData['targetPort']
        }
    elif tpData['warningInf'] == 'USB' and lv == 0:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "6a5de2d0-b460-11eb-98e4-8590585d6e25",
            "text": tpData['targetPort']
        }
    elif tpData['warningInf'] == 'USB' and lv == 1:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "0ef385c0-b461-11eb-98e4-8590585d6e25",
            "text": tpData['targetPort']
        }
    elif tpData['warningInf'] == 'USB' and lv == 2:
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "33e40120-b461-11eb-98e4-8590585d6e25",
            "text": tpData['targetPort']
        }
    else:
        print("该事件暂未添加剧本 请先配置处置策略！")
        data = {
            "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
            "uuid": "50719e20-b3e8-11eb-afe8-2becb4ed7b2c",
            "text": tpData['targetPort']
        }

    r = requests.post(url="http://192.168.1.4:8888/api/v1/w5/webhook", headers=headers, data=json.dumps(data))
    print(r.json())

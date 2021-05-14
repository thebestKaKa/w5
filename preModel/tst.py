import requests
import time
import json
 #["Attack","Unsafe","USB"]

testData = [
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}',
'{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99"}'
]

url="http://127.0.0.1:5000/MLP"

for i in range(7):
	time.sleep(5)
	res = requests.post(url=url, data=testData[i])
	print(res.text)

	headers = {
    "Content-Type": "application/json"
	}

	data = {
    "key": "9FBBB6BFFAD8426FAE18BFD67139D0DC",
    "uuid": "50719e20-b3e8-11eb-afe8-2becb4ed7b2c",
    "text": '{"warningInf":"Attack","targetIP":"0.0.0.1","targetPort":"80","sourceIP":"192.0.0.1","sourcePort":"99","rankLevel":'+res.text+'}'
	}

	r = requests.post(url="http://192.168.1.4:8888/api/v1/w5/webhook", headers=headers, data=json.dumps(data))


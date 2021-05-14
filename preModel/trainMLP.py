import os
import numpy as np

import MyNN.Layer as layer
import MyNN.Activation as active
import MyNN.Optim as optim
import MyNN.Network as net
import MyNN.LossFunc as lfc



def inputVec(warningNum,timeLim,freqLim):
	ret = warningNum
	temp = timeLim
	while 1:
		temp = int(temp /2)
		if temp != 0:
			ret += 1
		else:
			ret += 1
			break
	temp = freqLim
	while 1:
		temp = int(temp /2)
		if temp != 0:
			ret += 1
		else:
			ret += 1
			break
	return ret

warningNum = 3
timeLim = 7
freqLim = 7
inDim = inputVec(warningNum,timeLim,freqLim)
CrowdGNN = net.Network()
CrowdGNN.appendLayer("Linear_layer",(inDim , 2 * inDim))
CrowdGNN.appendLayer("Relu",1)
CrowdGNN.appendLayer("Linear_layer",(2 * inDim , 3 * inDim))
CrowdGNN.appendLayer("Relu",1)
CrowdGNN.appendLayer("Linear_layer",(3 * inDim , 3))
CrowdGNN.appendLayer("Softmax",2)

data = np.array([
	[1,0,0,0,0,1,0,0,1],
	[0,1,0,0,0,1,0,0,1],
	[0,0,1,0,0,1,0,0,1],
	[1,0,0,1,0,0,0,1,0],
	[0,1,0,1,0,0,0,1,0],
	[0,0,1,1,0,0,0,1,0],
	[1,0,0,1,1,1,1,1,1],
	[0,1,0,1,1,1,1,1,1],
	[0,0,1,1,1,1,1,1,1]
	])

truth = np.array([
	[1,0,0],
	[1,0,0],
	[1,0,0],
	[0,1,0],
	[0,1,0],
	[0,1,0],
	[0,0,1],
	[0,0,1],
	[0,0,1]
	])

CG_optim = optim.Bgd()
CG_optim.set(data,truth,CrowdGNN,lfc.crossEntropy(),0.0001,10000)
CG_optim.train()
CrowdGNN.save()

for i in range(9):
	print(CrowdGNN.forward(data[i]))

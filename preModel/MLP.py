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

def inputVec_simple(warningNum,timeLim,freqLim):
	return int(warningNum+2)

warningNum = 3
timeLim = 7
freqLim = 7
inDim = inputVec_simple(warningNum,timeLim,freqLim)
MLP = net.Network()
MLP.appendLayer("Linear_layer",(inDim , 2 * inDim))
MLP.appendLayer("Relu",1)
MLP.appendLayer("Linear_layer",(2 * inDim , 3 * inDim))
MLP.appendLayer("Relu",1)
MLP.appendLayer("Linear_layer",(3 * inDim , 3))
MLP.appendLayer("Softmax",2)
'''
data1 = np.array([
	[1,0,0,0,0,1,0,0,1],
	[0,1,0,0,0,1,0,0,1],
	[0,0,1,0,0,1,0,0,1],
	[1,0,0,1,0,0,0,1,0],
	[0,1,0,1,0,0,0,1,0],
	[0,0,1,1,0,0,0,1,0],
	[1,0,0,1,1,1,1,1,1],
	[0,1,0,1,1,1,1,1,1],
	[0,0,1,1,1,1,1,1,1],
	[1,0,0,1,0,0,1,0,0],
	[0,1,0,1,0,0,1,0,0],
	[0,0,1,1,0,0,1,0,0],
	[1,0,0,0,1,0,0,1,0],
	[0,1,0,0,1,0,0,1,0],
	[0,0,1,0,1,0,0,1,0]
	])
data = np.array([
	[1,0,0,0,0,1,0,0,1],
	[1,0,0,0,1,0,0,0,1],
	[1,0,0,0,1,0,0,1,0],
	[1,0,0,0,1,0,1,0,0],
	[1,0,0,1,0,0,0,0,1],
	[1,0,0,1,0,0,0,1,0],
	[1,0,0,1,0,0,1,0,0],
	[1,0,0,1,1,0,1,0,0],
	[1,0,0,1,1,1,0,1,0],
	[1,0,0,1,1,1,1,1,1]
	])
truth1 = np.array([
	[1,0,0],
	[1,0,0],
	[1,0,0],
	[0,1,0],
	[0,1,0],
	[0,1,0],
	[0,0,1],
	[0,0,1],
	[0,0,1],
	[0,1,0],
	[0,1,0],
	[0,1,0],
	[0,0,1],
	[0,0,1],
	[0,0,1]
	])
truth = np.array([
	[1,0,0],
	[1,0,0],
	[0,1,0],
	[0,1,0],
	[1,0,0],
	[0,1,0],
	[0,0,1],
	[0,0,1],
	[0,0,1],
	[0,0,1]
	])
'''

data = np.array([
	[1,0,0,0,0],
	[1,0,0,4,0],
	[1,0,0,4,3],
	[1,0,0,2,7],
	[1,0,0,7,7],
	[0,1,0,0,0],
	[0,1,0,4,0],
	[0,1,0,4,3],
	[0,1,0,2,7],
	[0,1,0,7,7],
	[0,0,1,0,0],
	[0,0,1,4,0],
	[0,0,1,4,3],
	[0,0,1,2,7],
	[0,0,1,7,7]
	])
truth=np.array([
	[1,0,0],
	[0,1,0],
	[0,0,1],
	[0,1,0],
	[0,0,1],
	[1,0,0],
	[0,1,0],
	[0,0,1],
	[0,1,0],
	[0,0,1],
	[1,0,0],
	[0,1,0],
	[0,0,1],
	[0,1,0],
	[0,0,1]
	])
CG_optim = optim.Bgd()
CG_optim.set(data,truth,MLP,lfc.crossEntropy(),0.0001,5000)
CG_optim.train()
'''
CG_optim = optim.Bgd()
CG_optim.set(data,truth,MLP,lfc.crossEntropy(),0.0001,1000)
CG_optim.train()
'''
MLP.save()


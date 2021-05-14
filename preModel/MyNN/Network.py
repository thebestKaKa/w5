import numpy as np
from . import Layer
from . import Activation
from . import LossFunc
from . import Optim

class Network():

	def __init__(self):
		super(Network, self).__init__()
		self.structure = []
		self.layers = []
		self.ret = 0
		self.truth = 0
		self.layerCNT = 0

	def appendLayer(self,layername,paras):
		self.structure.append(layername+' : '+str(paras))
		self.layerCNT += 1
		if layername == 'Linear_layer':
			self.layers.append((Layer.Linear_layer(paras[0],paras[1]),'Linear_layer',paras))
			return 1
		if layername == 'Had_graph_layer':
			self.layers.append((Layer.Had_graph_layer(paras[0],paras[1]),'Had_graph_layer',paras))
			return 1
		if layername == 'Relu':
			self.layers.append((Activation.Relu(),'Relu',1))
			return 1
		if layername == 'Softmax':
			self.layers.append((Activation.Softmax(),'Softmax',2))
			return 1

		print("No such layer!")
		return 0

	def showParameters(self):
		for i in range(self.layerCNT):
			self.layers[i][0].showWeights()
		return True

	def showStructure(self):
		for i in self.structure:
			print(i)
		return self.structure

	def showLayers(self):
		print(self.layers)
		return self.layers

	def forward(self,data_in):
		#print("\nForward : ")
		self.ret = data_in
		for i in range(self.layerCNT):
			#print(self.layers[i][1]+": ",self.ret)
			self.ret = self.layers[i][0].forward(self.ret)
		#print("result : ",self.ret)
		return self.ret

	def backward(self,loss,truth):
		#print("\nBackward : ")
		self.truth = truth

		lossVal = loss.forward(self.ret,self.truth)
		error = loss.backward()

		for i in range(self.layerCNT,0,-1):
			#print(self.layers[i-1][1]+" error : \n",error)
			error = self.layers[i-1][0].backward(error)
		return lossVal

	def update(self,alphal):
		for i in range(self.layerCNT):
			flag = self.layers[i][0].update(alphal)
			if not flag:
				return False 
			self.layers[i][0].zeroGradient()
		return True

	def save(self):
		config = []
		for i in range(self.layerCNT):
			config.append(self.layers[i][1])
		f = open('./model/modelConfig.dat','w+')
		for i in range(self.layerCNT):		
			f.write(str(config[i])+'\n')
		f.close()

		for i in range(self.layerCNT):
			if config[i] == 'Linear_layer':
				np.save('./model/Layer'+str(i),self.layers[i][0].W)
		return True

	def load(self):
		f = open('./model/modelConfig.dat','r')
		config = f.readlines()
		lenth = len(config)
		for i in range(lenth):
			config[i] = config[i].strip('\n')
			if config[i] == 'Linear_layer':
				temp = np.load('./model/Layer'+str(i)+'.npy')
				paras = np.shape(temp)
			else:
				paras = 1
			self.appendLayer(config[i],paras)
			if config[i] == 'Linear_layer':
				self.layers[i][0].W = temp
		return True


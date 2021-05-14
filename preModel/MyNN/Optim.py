import numpy as np
from . import Layer
from . import Activation
from . import LossFunc
from . import Optim



class Bgd():
	def __init__(self):
		super(Bgd, self).__init__()
		self.epoch = 0
		self.alphal = 0
		self.dataSet = 0
		self.truthSet = 0
		self.net = 0
		self.lossFunc = 0


	def set(self, dataSet, truthSet, net, lossFunc, alphal, epoch):
		self.dataSet = dataSet
		self.truthSet = truthSet
		self.net = net
		self.lossFunc = lossFunc
		self.epoch = epoch
		self.alphal = alphal
		return True

	def train(self):
		batch = np.shape(self.dataSet)[0]
		error = 0
		for j in range(self.epoch):
			#print("round : ",j)
			lossVal = 0
			for i in range(batch):
				ret = self.net.forward(self.dataSet[i])
				lossVal += self.net.backward(self.lossFunc,self.truthSet[i])
				#if not (j%10):
					#print(ret)
			print(lossVal)
			self.net.update(self.alphal)
		return True


class Sgd():
	pass
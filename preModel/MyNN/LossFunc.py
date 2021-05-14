import numpy as np
#import NN.NN as NN

class crossEntropy():#NN.layer

	def __init__(self):
		super(crossEntropy, self).__init__()		
		self.int_truth = 0
		self.int_pred = 0
		self.ret = 0

	def forward(self,pred,truth):
		self.int_truth = truth
		self.int_pred = pred
		self.ret = -((np.log(pred)).dot(truth))
		return self.ret

	def backward(self):
		error = np.copy(self.int_pred)
		for i in range(np.size(error)):
			error[i] = -self.int_truth[i]/self.int_pred[i]
		return error

	def update(self):
		return True
		
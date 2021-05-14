import numpy as np
from .NN import NN


class Relu(NN.layer):

	def __init__(self):
		super(Relu, self).__init__()
		self.int = 0
		self.opt = 0

		self.grad = 0
		self.error = 0
		
	def forward(self,data_in):
		self.int = data_in
		self.opt = np.maximum(self.int,0)
		return self.opt

	def backward(self,back_error):
		self.grad = self.int * 1
		self.grad = np.where(self.grad<0,self.grad,1)
		self.grad = np.where(self.grad>0,self.grad,0)
		self.error = back_error.dot(np.diag(self.grad))
		return self.error



class Softmax(NN.layer):

	def __init__(self):
		super(Softmax, self).__init__()
		self.int = 0
		self.opt = 0
		self.grad = 0
		self.error = 0

	def forward(self,data_in):
		self.int = data_in
		self.int -= np.max(self.int)
		self.opt = np.exp(self.int)/np.sum(np.exp(self.int))
		return self.opt

	def backward(self,back_error):
		self.grad = (np.diag(self.opt) - np.outer(self.opt,self.opt))
		self.error = back_error.dot(self.grad)
		return self.error
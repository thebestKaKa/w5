import numpy as np
#import NN.NN as NN

class Linear_layer():#NN.layer

	def __init__(self, input_N, output_M):
		super(Linear_layer,self).__init__()
		self.inp = input_N
		self.otp = output_M
		self.W = np.random.random((self.otp,self.inp))

		self.D_in = np.zeros(input_N)
		self.D_out = np.zeros(output_M)
		
		self.G_W =  np.zeros((self.otp,self.inp))
		self.error = 0
	
	def forward(self, data_in):
		self.D_in = data_in
		self.D_out = (self.W).dot(self.D_in)
		#print("Linear Weight : ", self.W)
		return self.D_out

	def backward(self, back_error):
		self.G_W += np.outer(back_error,self.D_in)
		#print("linear grad : \n", self.G_W)
		self.error = ((self.W).T).dot(back_error)
		return self.error

	def update(self, alphal):
		self.W -= alphal * self.G_W
		#print("linear Weight : \n",self.W)
		return True

	def zeroGradient(self):
		self.G_W = np.zeros((self.otp,self.inp))
		return True

	def showWeights(self):
		print("Linear : \n", self.W)
		return True


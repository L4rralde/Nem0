import numpy as np
import matplotlib.pyplot as plt

class variable: 
	def __init__(self, nombre, funcion, x=[], y=[]): 
		self.nombre  = nombre
		self.funcion =funcion
		self.x=x
		self.y=y
		self.max=0
		self.t_max=0
		self.min=0
		self.t_min=0
	
	def valor(self, t): 
		return self.funcion(t) 
	
	def grafica(self, t):
		self.x=np.append(self.x, t)
		self.y=np.append(self.y, self.funcion(t))

	def reset(self):
		self.x=[]
		self.y=[]

	def figura(self, t=None): 
		self.grafica(t)
		plt.figure(num=None, figsize=(11, 10), dpi=80, facecolor='w', edgecolor='k')
		plt.plot(self.x, self.y)
		plt.savefig("static/"+self.nombre+".png")

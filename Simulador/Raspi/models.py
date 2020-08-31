import numpy as np 

def temperatura(t): 
	return np.cos(t)

def presion1(t):
	return (1-np.exp(t*-1))

def presion2(t):
	return (1-0.9*np.exp(t*-2.5))

def humedad(t):
	return (np.sin(t))

varFuncs = [
		("Temperatura", temperatura),
		("Presion1", presion1),
		("Presion2", presion2), 
		("Humedad", humedad)
		]

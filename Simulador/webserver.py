import flask
import numpy as np
import matplotlib.pyplot as plt
from miInstrumento import *

def var1(t):
	f = np.sin(t)  
	return f

def var2(t): 
	f = np.cos(t)
	return f

def var3(t): 
	f = np.tanh(t)
	return f

def var4(t): 
	f = np.sqrt(t)
	return f

def var5(t): 
	f = np.tan(t)
	return f

x=np.linspace(0,10, 1000)

varA = variable("var1", var1)
varA.figura(x)

varB = variable("var2", var2)
varB.figura(x)

varC = variable("var3", var3)
varC.figura(x)

varD = variable("var4", var4)
varD.figura(x)

varE = variable("nameless", var5)
varE.figura(x)

variables=[varA, varB, varC, varD, varE]

app = flask.Flask(__name__)
@app.route('/')
def home(): 
	return "Bienvenido, Emmanuel"

@app.route('/ambiente')
def main():
	return flask.render_template('instrumento.html',  lista=variables)  

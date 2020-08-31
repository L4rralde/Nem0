import flask 
import time 
from models import varFuncs
from instrument import variable 

lVariables = []
for name, func in varFuncs: 
	lVariables.append(variable(name, func))

app = flask.Flask(__name__)
t0 = 0

@app.route('/')
def inicio():
	return '<p>Bienvenido</p><p><a href="http://raspberrypi.local:5000/monitor">Monitor</a></p>'
	#return '<p>Bienvenido</p><p><a href="http://localhost:5000/monitor">Monitor</a></p>'
@app.route('/monitor')
def main():
	global t0
	if(t0==0):
		t = 0
		t0 = time.time()
	else: 
		t = time.time()-t0
	paquete = []

	for var in lVariables: 
		paquete.append(var.empaquetar(t))
	return flask.jsonify(paquete)

if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000)

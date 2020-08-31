import numpy as np 
import struct
import spidev
#import gpiozero as gpz

#micro1 = 
#micro2 =


spi = spidev.Spidev()
spi.max_speed_hz = 10000
spi.mode = 0



class varInterf: 
	def __init__(self, ID, dType=0x1, FOD = 0x1): 
		self.ID = ID
		self.dType = dType
		self.FOD = FOD

"""
dTypes:
	*b'0' : 32-bits int (python default)
	*b'1' : 32-bits float (not python default)
"""

"""
FOD:
	*b'xxx' : xxx+1
"""

"""
Ids: 
	*b'000001' : Temperatura
	*b'000010' : Presion1
	*b'000011' : Presion2
	*b'000100' : Humedad 
	*b'000111' : Posicion 
	*b'000111' : Aceleracion
	*b'001000' : Orientacion
"""
idList = [
			{"Name" : "Temperatura", "OBJ" : varInterf(0x0)},
			{"Name" : "Presion1", "OBJ" : varInterf(0x1) },	
			{"Name" : "Presion2", "OBJ" : varInterf(0x2) },
			{"Name" : "Humedad", "OBJ" : varInterf(0x3) }	
		 ]

class variable:
	def __init__(self, name, function):
		self.name = name
		dicty = next(item for item in idList if item["Name"] == name)
		self.interf = dicty["OBJ"]
		self.idnum = self.interf.ID
		self.function = function
		self.x = 0
		self.y = [0]
		self.json = {	
						"Name" 	: 	self.name, 
						"t"		: 	0, 
						"f(t)"	: 	0
					}
		self.spi = {	
						"Head" : (self.interf.ID<<7 |  self.interf.FOD<<4 | self.idnum) & 0xFF, 
						"Data" : self.y
					}

	def calcular(self, t): 
		valor = self.function(t)
		self.x = t
		self.y = valor 
		self.json["t"] = t
		self.json["f(t)"] = valor
		if(type(valor)==int):
			self.spi["Data"] = [valor&0xFF, (valor>>8)&0xFF, (valor>>16)&0xFF, (valor>>32)&0xFF]
		else:
			valor = np.float32(valor)
			valor = bytearray(struct.pack("f", valor))
			self.spi["Data"] = list(valor)
		return self.function(t)

	def aMicro(self, dato):
		spi.open(0,0)
		receiv = spi.xfer2(dato)
		"""
			Needs development
		"""
		return receiv

	def empaquetar(self, t): 
		dato = self.calcular(t)
		self.aMicro(dato)
		return self.json 

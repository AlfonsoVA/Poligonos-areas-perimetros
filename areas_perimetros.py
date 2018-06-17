# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
clase= uic.loadUiType("areas_perimetros.ui")[0]

class Areas_Perimetros(QtGui.QMainWindow, clase):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)		
		self.setupUi(self)
		self.btn_calcula.clicked.connect(self.calcula)		

# Inicia los calculos.
	def calcula(self): 	
		if self.rad_area.isChecked()== False and self.rad_perim.isChecked()== False:
			print("No ha seleccionado alguna opción de perimetro o area")
		else:		
			self.calcula_circulo(self.line_radio.text())
			self.calcula_elipse(self.line_eje_a.text(), self.line_eje_b.text())
			self.calcula_triangulo(self.line_A.text(), self.line_B.text(), self.line_C.text())
			self.calcula_cuadrado(self.line_lado_cuadrado.text())
			self.calcula_p_h_o(self.line_lado_p_h_o.text(), self.line_apotema.text())				

# Calcula las operaciones sobre un circulo
	def calcula_circulo(self, radio):
		if self.rad_area.isChecked():
			if str(radio)== "":
				pass
			else:
				try:
					r= float(radio)
					self.line_res_cir.setText(str("%.2f" % (3.1416*r*r))) if r>0 else print("ERROR-CIRCULO: El radio no es valido!\n")
				except Exception:
					print("ERROR-CIRCULO: El radio del circulo no es un número!\n")
		elif self.rad_perim.isChecked():
			if str(radio)== "":
				pass
			else:
				try:
					r= float(radio)
					self.line_res_cir.setText(str("%.2f" % (3.1416*r*2))) if r>0 else print("ERROR-CIRCULO: El radio no es valido!\n")
				except Exception:
					print("ERROR-CIRCULO: El radio del circulo no es un número!\n")
			
# Calcula las operaciones sobre una elipse.
	def calcula_elipse(self, a, b):
		if self.rad_area.isChecked():
			if str(a)== "" and str(b)== "":
				pass
			else:
				try:
					eje_a= float(a)
					eje_b= float(b)
					self.line_res_e.setText(str("%.2f" % (3.1416*eje_a*eje_b))) if eje_a>0 and eje_b>0 else print("ERROR-ELIPSE: Al menos uno de los ejes no es valido!\n")
				except Exception:
					print("ERROR-ELIPSE: Al menos uno de los ejes no es un número!\n")
		elif self.rad_perim.isChecked():
			if str(a)== "" and str(b)== "":
				pass
			else:
				try:
					eje_a= float(a)
					eje_b= float(b)
					self.line_res_e.setText(str("%.2f" % (3.1416*(3*(eje_a+eje_b)-((3*eje_a + eje_b)*(eje_a + 3*eje_b))**(0.5))))) if eje_a>0 and eje_b>0 else print("ERROR-ELIPSE: Al menos uno de los ejes no es valido!\n")
				except Exception:
					print("ERROR-ELIPSE: Al menos uno de los ejes no es un número!\n")			

# Calcula las operaciones sobre un triangulo.
	def calcula_triangulo(self, lado_a, lado_b, lado_c):
		if self.rad_area.isChecked():
			if str(lado_a)== "" and str(lado_b)== "" and str(lado_c)== "":
				pass
			else:
				try:
					a= float(lado_a)
					b= float(lado_b)
					c= float(lado_c)
					s= float((a+b+c)/2)
					self.line_res_t.setText(str("%.2f" % (s*((s-a)*(s-b)*(s-c)) )**.5)) if a>0 and b>0 and c>0 else print("ERROR-TRIANGULO: Al menos uno de los lados no es valido!\n")
				except Exception:
					print("ERROR-TRIANGULO: Al menos uno de los lados no es un número!\n")				
				except ValueError:
					print("ERROR-TRIAGULO: El resultado o alguno de los lados no es valido!\n")				

		elif self.rad_perim.isChecked():
			if str(lado_a)== "" and str(lado_b)== "" and str(lado_c)== "":
				pass
			else:
				try:
					a= float(lado_a)
					b= float(lado_b)
					c= float(lado_c)					
					self.line_res_t.setText(str("%.2f"%(a+b+c))) if a>0 and b>0 and b>0 else print("ERROR-TRIANGULO: Al menos uno de los lados no es valido!\n")
				except TypeError:
					print("ERROR-TRIANGULO: Al menos uno de los lados no es un número!\n")
				except ValueError:
					print("ERROR-TRIAGULO: El resultado o alguno de los lados no es valido!\n")

# Calcula las operaciones sobre un cuadrado.
	def calcula_cuadrado(self, lado):
		if self.rad_area.isChecked():
			if str(lado)== "":
				pass
			else:
				try:
					l= float(lado)
					self.line_res_cuad.setText(str("%.2f"%(l*l))) if l>0 else print("ERROR-CUADRADO: El lado del cuadrado no es valido!\n")
				except TypeError:
					print("ERROR-CUADRADO: El lado del cuadrado no es un número!\n")				
		elif self.rad_perim.isChecked():
			if str(lado)== "":
				pass
			else:
				try:
					l= float(lado)
					self.line_res_cuad.setText(str("%.2f"%(l*4))) if l>0 else print("ERROR-CUADRADO: El lado del cuadrado no es valido!\n")
				except Exception:
					print("ERROR-CUADRADO: El lado del cuadrado no es un número!\n")

# Calcula las operaciones sobre polígonos.
	def calcula_p_h_o(self, lado, apotem):
		if str(lado)== "" and str(apotem)== "":
			pass
		else:		
			try:
				l= float(lado)
				a= float(apotem)

				#=========================::: A R E A
				if self.rad_area.isChecked():
					if self.p_h_o.currentText()=="Pentagono":
						self.line_res_p.setText(str("%.2f"%((l*5*a)/2))) if l>0 and a>0 else print("ERROR-PENTAGONO: El lado o el apotema no es valido!\n")
					elif self.p_h_o.currentText()=="Hexagono":
						self.line_res_p.setText(str("%.2f"%(l*6*a)/2)) if l>0 and a>0 else print("ERROR-HEXAGONO: El lado o el apotema no es valido!\n")
					elif self.p_h_o.currentText()=="Heptagono":
						self.line_res_p.setText(str("%.2f"%(l*7*a)/2)) if l>0 and a>0 else print("ERROR-HEPTAGONO: El lado o el apotema no es valido!\n")
					elif self.p_h_o.currentText()=="Octagono":
						self.line_res_p.setText(str("%.2f"%(l*8*a)/2)) if l>0 and a>0 else print("ERROR-OCTAGONO: El lado o el apotema no es valido!\n")

				#=========================::: P E R I M E T R O
				elif self.rad_perim.isChecked():
					if self.p_h_o.currentText()=="Pentagono":
						self.line_res_p.setText(str("%.2f"%(l*5))) if l>0 else print("ERROR-PENTAGONO: El lado no es valido\n")
					elif self.p_h_o.currentText()=="Hexagono":
						self.line_res_p.setText(str("%.2f"%(l*6))) if l>0 else print("ERROR-HEXAGONO: El lado no es valido\n")
					elif self.p_h_o.currentText()=="Heptagono":
						self.line_res_p.setText(str("%.2f"%(l*7))) if l>0 else print("ERROR-HEPTAGONO: El lado no es valido\n")
					elif self.p_h_o.currentText()=="Octagono":
						self.line_res_p.setText(str("%.2f"%(l*8))) if l>0 else print("ERROR-OCTAGONO: El lado no es valido\n")
			except Exception:
				print("ERROR-PENTA-HEXA-HEPTA-OCTAGONO: Al menos uno de los valores del poligono no es un número!\n")


app= QtGui.QApplication(sys.argv)
Ventana= Areas_Perimetros()
Ventana.show()
print("Versión 1.0, limitantes:")
print("* Solo debe ser perimetro o area especificamente para todos los calculos")
print("* TODO ES EN BASE A FIGURAS REGULARES")
app.exec_()
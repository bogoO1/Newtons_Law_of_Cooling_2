import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from pyscript import document
from pyscript import display
import math

shape = document.querySelector("#volume")
sizeElement = document.querySelector("#size")
mediumTempElement = document.querySelector("#mediumTemp")
objectTempElement = document.querySelector("#objectTemp")




# xdata = [.81, 7.33, 60.38, 201.90, 499.28]
# ydata = [-0.002761472, -0.0025480341, -0.0016324848, -0.001214448, -0.0010582512]

# #Recast xdata and ydata into numpy arrays so we can use their handy features
# xdata = np.asarray(xdata)
# ydata = np.asarray(ydata)

# fig, ax = plt.subplots()


# ax.plot(xdata, ydata, 'o')

# def Gauss(x, A, B, C, D, E, F):
# 	y = A + (B - C)/(1 + (x/D)^E)^F
# 	return y

# parameters, covariance = curve_fit(Gauss, xdata, ydata)
# fit_A = parameters[0]
# fit_B = parameters[1]
# fit_C = parameters[2]
# fit_D = parameters[3]
# fit_E = parameters[4]
# fit_F = parameters[5]
# print(fit_A)
# print(fit_B)

# fit_y = Gauss(xdata, fit_A, fit_B, fit_C, fit_D, fit_E, fit_F)
# ax.plot(xdata, ydata, 'o', label='data')
# ax.plot(xdata, fit_y, '-', label='fit')
# ax.legend()

# plot = document.querySelector("#curveFit")
# plot.innerHTML = ""


# display(fig, target = "curveFit")


def getK(shape, size):
	print(size)
	if shape == "Cube":
		y = -0.0009072971 + ((-0.002777166 + 0.0009072971)/pow(1+pow(size/22.86917, 1.289453), 0.6300349))
		return y
	elif shape == "Cylinder":
		y = -0.003220575 - 0.0001079421*size + 0.000004613497*pow(size,2) + 3.636678e-7*pow(size,3) - 1.572577e-8*pow(size,4)
		return y

	return .01


# 	return -(np.log((temp1 - mediumTemp)/(startTemp - mediumTemp))/time1)

#USING 5PL y = -0.0009072977 + (-0.002777166 - -0.0009072977)/(1 + (x/22.86916)^1.289454)^0.6300348	

def onSubmit(event):
	# TODO: check for where the graph hits around zero and then decide the range based on that.
	# TODO: Calculate the equations that relates the k values for each shape and size and then use that to calc K.
	# https://education.molssi.org/python-data-analysis/03-data-fitting/index.html
	if len(sizeElement.value) <= 0 or isinstance(float(sizeElement.value), (float, int)) == False:
		return
	
	if len(mediumTempElement.value) <= 0 or isinstance(float(mediumTempElement.value), (float, int)) == False:
		return

	if len(objectTempElement.value) <= 0 or isinstance(float(objectTempElement.value), (float, int)) == False:
		return

	if len(sizeElement.value) <= 0 or isinstance(float(sizeElement.value), (float, int)) == False:
		return

	size = float(sizeElement.value)
	mediumTemp = float(mediumTempElement.value)
	startTemp = float(objectTempElement.value)
	if size <= 0 or size > 10:
		return
	
	volume = 0
	if shape.value == "Cube":
		volume = pow(size, 3)
	elif shape.value == "Cylinder":
		radius = 1
		volume = size * math.pi * pow(radius,2)

	K = getK(shape.value, volume);

	t = np.arange(0.0,10.0 * 60.0,1.0)
	s = mediumTemp + (startTemp - mediumTemp) * np.exp(K*t)

	fig, ax = plt.subplots()

	ax.plot(t,s)

	ax.set(xlabel = "time (s)", ylabel = "Temperature(F)", title = shape.value + ": K = " + str(K))

	ax.grid

	plot = document.querySelector("#plot")
	plot.innerHTML = ""

	display(fig, target = "plot")
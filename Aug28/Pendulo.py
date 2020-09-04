import numpy as np
import matplotlib.pyplot as plt
from math import sin
import time
import sys

#definimos una variable para registrar el tiempo al que inicia la ejecución del código
timestamp_init = time.time()

#parametros
g = 9.81
l = 1

def Pendulo(t_0,t_fin, n, theta_0, omega_0):
    g = 9.81
    l = 1
    h = t_fin/n
    t = np.arange(t_0,t_fin,h)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    theta[0] = theta_0
    omega[0] = omega_0
    for i in range(len(t)-1):
        theta[i+1] = theta[i] + h*omega[i]
        omega[i+1] = omega[i] + h*(-g/l)*sin(theta[i])
    return theta, omega, t


n = int(float((sys.argv[1])))
t_0 = float(sys.argv[2])
t_fin = float(sys.argv[3])
theta_0 = float(sys.argv[4])
omega_0 = float(sys.argv[5])
theta, omega, t = Pendulo(t_0, t_fin, n, theta_0, omega_0)



plt.plot(t, omega)
plt.plot(t, theta)
plt.title('Pendulo simple con método de Euler')
plt.legend(['omega(t)','theta(t)'], loc='upper left')
plt.xlabel('Tiempo(s)')
plt.ylabel('Ángulo(rad)')
plt.show()

timestamp_final = time.time()
#verificamos el tiempo de ejecucion
time_ex = timestamp_final - timestamp_init
print('El tiempo de ejecución fue de: ',time_ex, 'segundos')

diferencia_ex = time1_ex - time_ex
print('La diferencia entre los tiempos de ejecucion es: ', diferencia_ex)

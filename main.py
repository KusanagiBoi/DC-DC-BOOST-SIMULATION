'''
This program simulates a DC DC boost converter with the input tension between 12V and 15V
and the output tension of 20V and shows a graph of Vout
'''

import matplotlib.pyplot as plt

Vg = 10  # Source voltage
L = 77 * 10 ** (-6)  # inductance
C = 200 * 10 ** (-6)  # capacitance
PWM = 0
Sim_Time = 500 * 10 ** (-3)  # simulation duration in ms
F = 31000  # sets the frequency to 31KHz
dt = 10 * 10 ** (-9)  # the unit used for the integrals
time_passed = dt
Vo = 0
R = 5  # value of the resistor in ohms
Dc = 0.7 # sets the initial duty cycle
PID_Dc = Dc * 255  # the PID works for values between 0 and 255
Il = 0  # initial current in the inductor
i = 0
y = []
X = []
Ts = 1/F  # temporization period
Kp = 5
Ki = 500
target = 20  # target value for the PID
integral = 0
pv_err = 0
while Sim_Time > i:
    if i < 0.5*Sim_Time:
        Vg = 10.0
    else:
        Vg = 15.0  # when half the time of simulation passed, it changes the input voltage to 15V

    if i % (1/F) < Dc/F:
        PWM = 1
    else:
        PWM = 0  # calculates the duty cycle
    if PWM == 1:  # calculates Vo for when the transistor is conducting current
        di = Vg * (1 / L) * dt
        dv = -(Vo / R) * (1 / C) * dt
        y.append(Vo)
        X.append(i * 1000)

    else: # calculates Vo for when the transistor is not conducting current
        di = (Vg - Vo) * (1 / L) * dt
        dv = (-Vo / R + Il) * (1 / C) * dt
        y.append(Vo)
        X.append(i * 1000)

    Il = Il + di
    Vo = Vo + dv
    i += dt

    error = target - Vo  # PID controller
    proportional = error
    integral = integral + error * dt
    derivative = (error - pv_err)/dt
    PID_Dc = Kp * proportional + integral*Ki
    pv_err = error
    Dc = PID_Dc/255

plt.plot(X, y)  # plots Vo
plt.ylabel('Voltage (V)')
plt.xlabel('Time (ms)')
plt.title('Vout')
plt.show()

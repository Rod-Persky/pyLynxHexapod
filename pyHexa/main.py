import serial
from time import sleep
import numpy


hexapod = serial.Serial()
hexapod.baudrate = 115200
hexapod.timeout = 1
hexapod.port = 4
hexapod.open()

# Simplify some things
def setposition(servo, position, power=1000):
    command = '#{}P{}S{}\r'.format(servo, int(position), power)
    hexapod.write(command.encode())
    
def setpower(servo, power=0):
    command = '#{}P{}\r'.format(servo, power)
    hexapod.write(command.encode())


# Lets draw a pattern (a circle)
circle = numpy.empty((2, 100))
circle[0] = numpy.linspace(0, numpy.pi * 2, len(circle[0]))
circle[1] = circle[0]
circle[0] = numpy.sin(circle[0])
circle[1] = numpy.cos(circle[1])
circle[0] = numpy.multiply(circle[0], 200)
circle[1] = numpy.multiply(circle[1], 200)


# Lets ROLL!
hexapod.write('QP0\r'.encode())

for leg in range(0, 3):
    setposition(leg * 3, 1500, 500)
    setposition(leg * 3 + 1, 2500, 500)
    setposition(leg * 3 + 2, 1500, 500)

    setposition(leg * 3 + 16, 1500, 500)
    setposition(leg * 3 + 1 + 16, 2500, 500)
    setposition(leg * 3 + 2 + 16, 1500, 500)

sleep(2)

nPoints = len(circle[0]) - 1

for times in range(0, 0):
    for i in range(0, len(circle[0]) - 1):
        for leg in range(0, 3):
            setposition(leg * 3, 1500 + circle[0][i])
            setposition(leg * 3 + 1, 1500 + circle[1][i])

            setposition(leg * 3 + 16, 1500 + circle[0][nPoints - i])
            setposition(leg * 3 + 1 + 16, 1500 + circle[1][nPoints - i])

        sleep(0.05)

for leg in range(0, 3):
    setposition(leg * 3 + 1, 2100)
    setposition(leg * 3 + 2, 2500)

    setposition(leg * 3 + 1 + 16, 2100)
    setposition(leg * 3 + 2 + 16, 2500)

sleep(2)

for leg in range(0, 3):
    setposition(leg * 3 + 1, 1500, 1000)
    setposition(leg * 3 + 2, 2100, 600)

    setposition(leg * 3 + 1 + 16, 1500, 1000)
    setposition(leg * 3 + 2 + 16, 2100, 600)
    
sleep(8)

# And relax
for leg in range(0, 3):
    setpower(leg * 3)
    setpower(leg * 3 + 1)
    setpower(leg * 3 + 2)

    setpower(leg * 3 + 16)
    setpower(leg * 3 + 1 + 16)
    setpower(leg * 3 + 2 + 16)

hexapod.close()

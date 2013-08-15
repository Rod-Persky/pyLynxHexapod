from time import sleep
import numpy

try:
    import serial
    hexapod = serial.Serial()
    hexapod.baudrate = 115200
    hexapod.timeout = 1
    hexapod.port = 4
    hexapod.open()
except:
    # ToDo: Import pyTTY
    print("Check serial, now using mock")
    from unittest import mock
    hexapod = mock.Mock()
    
try:
    from bottle import route, run, template
except:
    from sys import exit
    exit("Functional Bottle install is required, run pip install bottle")
    

# Simplify some things
leg_number  =  [0,3,6,16,19,22]

joint_reversed = [[False, False, False, True, True, True],
                  [False, False, False, False, False, False],
                  [False, False, False, False, False, False]]

joint_centers = [[2100, 1500, 950, 800, 1400, 2100],
                 [1500, 1500, 1500, 1500, 1500, 1500],
                 [2300, 2300, 2350, 2200, 2240, 2250]]


@route('/setposition/<leg>/<hip_rotation>/<hip_elevation>/<knee_elevation>/<power>')
def web_setposition(**kwargs):
    params = dict()
    
    for key in kwargs:
        params[key] = int(kwargs[key])
    
    setposition(params['leg'], params['hip_rotation'],
                params['hip_elevation'], params['knee_elevation'],
                params['power'])
    
    return template('apiresponse', content='test') # For bottle


def setposition(leg, hip_rotation = None, hip_elevation = None, knee_elevation = None, power=1000):
       
    command = ""
    for joint, value in enumerate([hip_rotation, hip_elevation, knee_elevation]):
        if value is not None:
            if joint_reversed[joint][leg]:
                value = value - (value - joint_centers[joint][leg])
            command =  '{}#{}P{}S{}'.format(command, leg_number[leg] + joint, int(value), power)
            
    command = command + '\r'
    print("doing command", command)

    hexapod.write(command.encode())
    

def setpower(servo, hip_rotation_power = None, hip_elevation_power = None, knee_elevation_power = None):
    command = ""
    
    for position, value in enumerate([hip_rotation_power, hip_elevation_power, knee_elevation_power]):
        if value is not None:
            command =  '{}#{}P{}'.format(command, leg_number[leg] + position, value)
            
    command = command + '\r'
                   
    hexapod.write(command.encode())

# Lets ROLL!
hexapod.write('QP0\r'.encode())

#===============================================================================
# Lets draw a pattern (a circle)
#circle = numpy.empty((2, 100))
#circle[0] = numpy.linspace(0, numpy.pi * 2, len(circle[0]))
#circle[1] = circle[0]
#circle[0] = numpy.sin(circle[0])
#circle[1] = numpy.cos(circle[1])
#circle[0] = numpy.multiply(circle[0], 200)
#circle[1] = numpy.multiply(circle[1], 200)
# for leg in range(0, 3):
#     setposition(leg * 3, 1500, 500)
#     setposition(leg * 3 + 1, 2500, 500)
#     setposition(leg * 3 + 2, 1500, 500)
# 
#     setposition(leg * 3 + 16, 1500, 500)
#     setposition(leg * 3 + 1 + 16, 2500, 500)
#     setposition(leg * 3 + 2 + 16, 1500, 500)
# 
# sleep(2)
# 
# nPoints = len(circle[0]) - 1
# 
# for times in range(0, 0):
#     for i in range(0, len(circle[0]) - 1):
#         for leg in range(0, 3):
#             setposition(leg * 3, 1500 + circle[0][i])
#             setposition(leg * 3 + 1, 1500 + circle[1][i])
# 
#             setposition(leg * 3 + 16, 1500 + circle[0][nPoints - i])
#             setposition(leg * 3 + 1 + 16, 1500 + circle[1][nPoints - i])
# 
#         sleep(0.05)
#
# for leg in range(0, 3):
#     print("leg", leg)
#     setposition(leg * 3 + 1, 2100)
#     setposition(leg * 3 + 2, 2500)
# 
#     setposition(leg * 3 + 1 + 16, 2100)
#     setposition(leg * 3 + 2 + 16, 2500)
# 
# sleep(2)
# 
# for leg in range(0, 3):
#     print("leg", leg)
#     setposition(leg * 3 + 1, 1500, 1000)
#     setposition(leg * 3 + 2, 2100, 600)
# 
#     setposition(leg * 3 + 1 + 16, 1500, 1000)
#     setposition(leg * 3 + 2 + 16, 2100, 600)
#===============================================================================


#===============================================================================
# for leg in range(0, 6):
#     setposition(leg, hip_rotation = joint_centers[0][leg],
#                      hip_elevation = joint_centers[1][leg],
#                      knee_elevation = joint_centers[2][leg],
#                      power = 500)
# 
# sleep(5)
# 
#  
# while(True):
#     for leg in range(0, 3):
#         # Raise leg
#         setposition(leg, hip_elevation = joint_centers[1][leg]+200,     power = 1000)
#         setposition(leg, hip_elevation = joint_centers[1][5 - leg]+200, power = 1000)
#         sleep(.2)
#      
#         # Rotate forward
#         setposition(leg, hip_rotation = joint_centers[0][leg]+200,     power = 1000)
#         setposition(leg, hip_rotation = joint_centers[0][5 - leg]+200, power = 1000)
#         sleep(.2)
#           
#         # Leg down
#         setposition(leg, hip_elevation = joint_centers[1][leg],     power = 500)
#         setposition(leg, hip_elevation = joint_centers[1][5 - leg], power = 500)
#         sleep(.5)
#               
#     # rotate back
#     for leg in range(0, 6):
#         setposition(leg, joint_centers[0][leg]-200, 500)
#         
#     sleep(2)
#  
#  
# # And relax
# for leg in range(0, 6):
#     setpower(leg, 0, 0, 0)
# 
# 
# hexapod.close()
#===============================================================================


run(host='localhost', port=8080)
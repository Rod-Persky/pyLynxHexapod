from bottle import route, run, template

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
    
# Set power to 0
hexapod.write('QP0\r'.encode())

# Simplify some things
leg_number  =  [0,3,6,16,19,22]

joint_reversed = [[False, False, False, True, True, True],
                  [False, False, False, False, False, False],
                  [False, False, False, False, False, False]]

joint_centers = [[2100, 1500, 950, 800, 1400, 2100],
                 [1500, 1500, 1500, 1500, 1500, 1500],
                 [2300, 2300, 2350, 2200, 2240, 2250]]


@route('/set/position/<leg:int>/<hip_rotation:int>/<hip_elevation:int>/<knee_elevation:int>/<power:int>')
def web_setposition(**params):
    
    setposition(params['leg'], params['hip_rotation'],
                params['hip_elevation'], params['knee_elevation'],
                params['power'])
    
    return template('apiresponse', content='test') # For bottle


@route('/set/power/<leg:int>/<hip_rotation_power:int>/<hip_elevation_power:int>/<knee_elevation_power:int>')
def web_setpower(**params):
    
    setposition(params['leg'], params['hip_rotation_power'],
                params['hip_elevation_power'], params['knee_elevation_power'])
    
    return template('apiresponse', content='test') # For bottle


def setposition(leg, hip_rotation = None, hip_elevation = None, knee_elevation = None, power=1000):
       
    command = ""
    for joint, value in enumerate([hip_rotation, hip_elevation, knee_elevation]):
        if value is not None:
            if joint_reversed[joint][leg]:
                value = joint_centers[joint][leg] - (value - joint_centers[joint][leg])
                command =  '{}#{}P{}S{}'.format(command, leg_number[leg] + joint, int(value), power)
                
            else:
                command =  '{}#{}P{}S{}'.format(command, leg_number[leg] + joint, int(value), power)
            
    command = command + '\r'
    print("doing command", command, end = "")

    hexapod.write(command.encode())
    

def setpower(leg, hip_rotation_power = None, hip_elevation_power = None, knee_elevation_power = None):
    command = ""
    
    for position, value in enumerate([hip_rotation_power, hip_elevation_power, knee_elevation_power]):
        if value is not None:
            command =  '{}#{}P{}'.format(command, leg_number[leg] + position, value)
            
    command = command + '\r'
                   
    hexapod.write(command.encode())

from bottle import route, run, template
from time import sleep
from lynxmotion import setposition, setpower

joint_centers = [[2100, 1500, 950, 800, 1400, 2100],
                 [1500, 1500, 1500, 1500, 1500, 1500],
                 [2300, 2300, 2350, 2200, 2240, 2250]]


@route('/go/start')
def stand(): 
    try:
        if not started:
            for leg in range(0, 6):
                setposition(leg, hip_rotation =     joint_centers[0][leg],
                                 hip_elevation =    joint_centers[1][leg],
                                 knee_elevation =   joint_centers[2][leg],
                                 power = 500)
        else:
            for leg in range(0, 6):
                setpower(leg, 0, 0, 0)
    except Exception as inst:
        global started
        started = False
        print(inst)
        
    started = not started

    sleep(1)
    
    return template('apiresponse', content='success')

@route('/go/forward')
@route('/behavior/walk/forwards/<steps:int>')
def walk_forwards(steps=1):
    
      
    for i in range(0, steps):
        for leg in range(0, 6):
            # Set Foot
            setposition(leg, knee_elevation = joint_centers[2][leg], power = 1000)
            
            # Raise leg
            setposition(leg, hip_elevation = joint_centers[1][leg]+200, power = 1000)
            sleep(.2)
          
            # Rotate forward
            setposition(leg, hip_rotation = joint_centers[0][leg]+200, power = 1000)
            sleep(.3)
               
            ## Leg down
            setposition(leg, hip_elevation = joint_centers[1][leg],     power = 500)

        sleep(.5)
                   
        # rotate back
        for leg in range(0, 6):
            setposition(leg, hip_rotation = joint_centers[0][leg]-200, power = 500)
        
    return template('apiresponse', content='success')

    
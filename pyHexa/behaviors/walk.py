
@route('/behavior/stand')
def stand():
    for leg in range(0, 3):
        print("leg", leg)
        setposition(leg * 3 + 1, 2100)
        setposition(leg * 3 + 2, 2500)
    
        setposition(leg * 3 + 1 + 16, 2100)
        setposition(leg * 3 + 2 + 16, 2500)
    
    sleep(2)
    
    for leg in range(0, 3):
        print("leg", leg)
        setposition(leg * 3 + 1, 1500, 1000)
        setposition(leg * 3 + 2, 2100, 600)
    
        setposition(leg * 3 + 1 + 16, 1500, 1000)
        setposition(leg * 3 + 2 + 16, 2100, 600)

@route('/behavior/walk/forwards/<steps:int>')
def walk_forwards(steps):
    for leg in range(0, 6):
        setposition(leg, hip_rotation = joint_centers[0][leg],
                         hip_elevation = joint_centers[1][leg],
                         knee_elevation = joint_centers[2][leg],
                         power = 500)
     
    sleep(5)
     
      
    while(True):
        for leg in range(0, 3):
            # Raise leg
            setposition(leg, hip_elevation = joint_centers[1][leg]+200,     power = 1000)
            setposition(leg, hip_elevation = joint_centers[1][5 - leg]+200, power = 1000)
            sleep(.2)
          
            # Rotate forward
            setposition(leg, hip_rotation = joint_centers[0][leg]+200,     power = 1000)
            setposition(leg, hip_rotation = joint_centers[0][5 - leg]+200, power = 1000)
            sleep(.2)
               
            # Leg down
            setposition(leg, hip_elevation = joint_centers[1][leg],     power = 500)
            setposition(leg, hip_elevation = joint_centers[1][5 - leg], power = 500)
            sleep(.5)
                   
        # rotate back
        for leg in range(0, 6):
            setposition(leg, joint_centers[0][leg]-200, 500)
             
        sleep(2)
      
      
    # And relax
    for leg in range(0, 6):
        setpower(leg, 0, 0, 0)

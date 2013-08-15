  
import numpy
from time import sleep
from lynxmotion import setposition
from bottle import route, run, template
  
@route('/time_wasting/draw_sky_circles/<numtimes:int>')
def draw_sky_circles(numtimes):
    circle = numpy.empty((2, 100))
    circle[0] = numpy.linspace(0, numpy.pi * 2, len(circle[0]))
    circle[1] = circle[0]
    circle[0] = numpy.sin(circle[0])
    circle[1] = numpy.cos(circle[1])
    circle[0] = numpy.multiply(circle[0], 200)
    circle[1] = numpy.multiply(circle[1], 200)
    
    
    #===========================================================================
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
    #===========================================================================
            
    return template('apiresponse', content='test') # For bottle 

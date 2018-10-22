import brickpi
import time
import math
from Utility import Car

interface=brickpi.Interface()
interface.initialize()
Robot = Car(interface)
for i in range(4):
    Robot.moveDistance(40)
    Robot.left90()
interface.terminate()


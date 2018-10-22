import brickpi
import time
import math
from Utility import Car

interface=brickpi.Interface()
interface.initialize()
Robot = Car(interface)

kp_min = float(input("Enter minimum Kp:"))
kp_max = float(input("Enter maximum Kp:"))
increment = float(input("Enter incremental value:"))

for i in range(kp_min, kp_max, increment):
    Robot.motorParams["Left"].pidParameters.k_p = i
    input_angle = float(input("Enter a angle to rotate (in radians): "))
    angle = math.radians(input_angle)
    Robot.wheel_rotate(angle, i)


interface.terminate()


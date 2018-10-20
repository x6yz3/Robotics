import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

motors = [0,1]
speed = 0

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

LeftParams = interface.MotorAngleControllerParameters()
LeftParams.maxRotationAcceleration = 6.0
LeftParams.maxRotationSpeed = 12.0
LeftParams.feedForwardGain = 255/20.0
LeftParams.minPWM = 18.0
LeftParams.pidParameters.minOutput = -255
LeftParams.pidParameters.maxOutput = 255
LeftParams.pidParameters.k_p = 100.0
LeftParams.pidParameters.k_i = 0.0
LeftParams.pidParameters.k_d = 0.0

RightParams = interface.MotorAngleControllerParameters()
RightParams.maxRotationAcceleration = 6.0
RightParams.maxRotationSpeed = 12.0
RightParams.feedForwardGain = 255/20.0
RightParams.minPWM = 18.0
RightParams.pidParameters.minOutput = -255
RightParams.pidParameters.maxOutput = 255
RightParams.pidParameters.k_p = 100.0
RightParams.pidParameters.k_i = 0.0
RightParams.pidParameters.k_d = 0.0

interface.setMotorAngleControllerParameters(motors[0],LeftParams)
interface.setMotorAngleControllerParameters(motors[1],RightParams)

interface.setMotorRotationSpeedReferences(motors, speed)

print "Press Ctrl+C to exit"
while True:
	time.sleep(1)

interface.terminate()

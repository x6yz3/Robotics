import brickpi
import time
import math


interface=brickpi.Interface()
interface.initialize()
# motors [0,1]是predefined 0 对应 motor port_A, 1 对应 motor port_B
motors = [0,1]
#一个brickpi的core是interface 所有的控制 都是基于这个interface进行的
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
#setMotorAngleControllerParameters方法给motor加params
interface.setMotorAngleControllerParameters(motors[0],LeftParams)
interface.setMotorAngleControllerParameters(motors[1],RightParams)
increment_value = 10
pid_max = 100
for i in range(LeftParams.pidParameters.k_p, pid_max, increment_value):
	for j in range(RightParams.pidParameters.k_p, pid_max, increment_value):


logfile_name = "logfile1.txt"
interface.startLogging(logfile_name)
#做一次转弯 以及记录到log中
while True:
	robot_angle = float(input("Enter a angle to rotate (in degree): "))
	wheel_angle = 5.243 * robot_angle/90
	interface.increaseMotorAngleReferences(motors,[wheel_angle, -wheel_angle])

	while not interface.motorAngleReferencesReached(motors) :
		motorAngles = interface.getMotorAngles(motors)
		if motorAngles :
			print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
		time.sleep(0.1)

	print "Destination reached!"
	
interface.stopLogging()
interface.terminate()


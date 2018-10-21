import brickpi
import time
import json

class Car:
    def __init__(self, interface):
        self.interface = interface
        self.motors = [0,1]
        self.motorParams = {}
        # motors [0,1]是predefined 0 对应 motor port_A, 1 对应 motor port_B
        # 一个brickpi的core是interface 所有的控制 都是基于这个interface进行的
        self.interface.motorEnable(self.motors[0])
        self.interface.motorEnable(self.motors[1])

        with open('parameter.json', 'r') as f:
            params = json.load(f)

        self.motorParams['Left'] = self.interface.MotorAngleControllerParameters()
        self.motorParams['Left'].maxRotationAcceleration = params['Left']['maxRotationAcceleration']
        self.motorParams['Left'].maxRotationSpeed = params['Left']['maxRotationSpeed']
        self.motorParams['Left'].feedForwardGain = params['Left']['feedForwardGain']
        self.motorParams['Left'].minPWM = params['Left']['minPWM']
        self.motorParams['Left'].pidParameters.minOutput = params['Left']['pidParameters.minOutput']
        self.motorParams['Left'].pidParameters.maxOutput = params['Left']['pidParameters.maxOutput']
        self.motorParams['Left'].pidParameters.k_p = params['Left']['pidParameters.k_p']
        self.motorParams['Left'].pidParameters.k_i = params['Left']['pidParameters.k_i']
        self.motorParams['Left'].pidParameters.k_d = params['Left']['pidParameters.k_d']

        self.motorParams['Right'] = self.interface.MotorAngleControllerParameters()
        self.motorParams['Right'].maxRotationAcceleration = params['Right']['maxRotationAcceleration']
        self.motorParams['Right'].maxRotationSpeed = params['Right']['maxRotationSpeed']
        self.motorParams['Right'].feedForwardGain = params['Right']['feedForwardGain']
        self.motorParams['Right'].minPWM = params['Right']['minPWM']
        self.motorParams['Right'].pidParameters.minOutput = params['Right']['pidParameters.minOutput']
        self.motorParams['Right'].pidParameters.maxOutput = params['Right']['pidParameters.maxOutput']
        self.motorParams['Right'].pidParameters.k_p = params['Right']['pidParameters.k_p']
        self.motorParams['Right'].pidParameters.k_i = params['Right']['pidParameters.k_i']
        self.motorParams['Right'].pidParameters.k_d = params['Right']['pidParameters.k_d']

        self.interface.setMotorAngleControllerParameters(self.motors[0], self.motorParams['Left'] )
        self.interface.setMotorAngleControllerParameters(self.motors[1], self.motorParams['Right'])

    def moveForward(self, speed):
        self.interface.setMotorRotationSpeedReferences(self.motors, speed)

    def rotate(self, angle):
        wheel_angle = 5.243 * angle/90
        self.interface.increaseMotorAngleReferences(self.motors,[wheel_angle, -wheel_angle])
        while not self.interface.motorAngleReferencesReached(self.motors):
            motorAngles = self.interface.getMotorAngles(self.motors)
            if motorAngles:
                print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
            time.sleep(0.1)

        print "Destination reached!"

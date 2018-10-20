import brickpi
import time
import json

class Car:
    def __init__(self, interface):
        self.interface = interface
        self.motor = [0,1]
        self.motorParams = {}

        self.interface.motorEnable(motors[0])
        self.interface.motorEnable(motors[1])

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

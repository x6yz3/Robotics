# Robotics
MAC address: 80:1f:02:/ab:a6:24
IP address can be found at:https://www.doc.ic.ac.uk/~ajd/robotics/index.cgi
## Week 2
For week 2 lab, we have tasks:
- [x] Show us a Built and Working Pi/BrickPi Robot with Working WiFi and Motors (4 Marks)
- [ ] Controller Tuning (8 Marks)
- [ ] Distance and Rotation Calibration (5 Marks)
- [ ] Driving Accurately in a Square and Observing Drift (9 Marks)
- [ ] Calculating a Covariance Matrix (4 Marks)

### Controller Tuning
For tuning the parameters, we should do several experiments. Firstly, we should test the
robot to go straight to tune parameters such as <i>maxRotationAcceleration,maxRotationSpeed </i></br>
Then, we should set angle (30°, 60°, 90°, 180°), keep track of logfile of reference angle and actual angle,
to plot diagram. We can use "Ziegler-Nichols" heuristic method to tune the PID parameter.</br>
• set ki and kd to zero. Increase kp until the system starts oscillating with period Pu (in seconds)
— remember this gain as ku;</br>
• set kp = 0.6ku, ki = 2kp/Pu, and kd = kpPu/8.</br>

### Calculating a Covariance Matrix
It should be a python file to read from txt files, which contains all 10 times experiment final point(x_i,y_i) result in it.
Then calculate a covariance matrix using these data.


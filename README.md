# Robotics  
MAC address: 80:1f:02: ab:a6:24  
IP address can be found at:https://www.doc.ic.ac.uk/~ajd/robotics/index.cgi  
## Week 2  
For week 2 lab, we have tasks:  
- [x] Show us a Built and Working Pi/BrickPi Robot with Working WiFi and Motors (4 Marks)  
- [ ] Controller Tuning (8 Marks)  
- [ ] Distance and Rotation Calibration (5 Marks)  
- [ ] Driving Accurately in a Square and Observing Drift (9 Marks)  
- [ ] Calculating a Covariance Matrix (4 Marks)  
### Code Refactoring
To improve code readability and reduce complexity. The example code has been refactored. First, it is miscellaneous if we want to add left or right motor's parameter but copy this code block:![enter image description here](https://i.loli.net/2018/10/20/5bcb4d5891a8d.png)
What we did is to build a "json" file which contains all the parameter information in and everytime read from this "json" file.
### Controller Tuning  
For tuning the parameters, we should do several experiments. Firstly, we should test the  
robot to go straight to tune parameters such as <i>maxRotationAcceleration,maxRotationSpeed </i></br>  
Then, we should set angle (30°, 60°, 90°, 180°), keep track of logfile of reference angle and actual angle,  
to plot diagram. We can use "Ziegler-Nichols" heuristic method to tune the PID parameter.</br>  
• set k<sub>i</sub>and k<sub>d</sub> to zero. Increase k<sub>p</sub> until the system starts oscillating with period P<sub>u</sub> (in seconds)  
— remember this gain as k<sub>u</sub>;</br>  
• set k<sub>p</sub> = 0.6k<sub>u</sub>, k<sub>i</sub> = 2k<sub>p</sub>/P<sub>u</sub>, and k<sub>d</sub> = k<sub>p</sub>P<sub>u</sub>/8.</br>  
  
### Calculating a Covariance Matrix  
It should be a python file to read from txt files, which contains all 10 times experiment final point(x<sub>i</sub>,y<sub>i</sub>) result in it.  
Then calculate a covariance matrix using these data.
with open("logs/logs_name.txt", "w+") as f:
    for i in range(10):
        name = "motor_angle_" + str(i)
        f.write(name+'\n')
f.close()


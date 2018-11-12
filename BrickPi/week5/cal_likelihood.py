import math


# points
p_O = [0, 0]
p_A = [0, 168]
p_B = [84, 168]
p_C = [84, 126]
p_D = [84, 210]
p_E = [168, 210]
p_F = [168, 84]
p_G = [210, 84]
p_H = [210, 0]

# walls
w_a = [p_O, p_A, "O-A"]
w_b = [p_A, p_B, "A-B"]
w_c = [p_C, p_D, "C-D"]
w_d = [p_D, p_E, "D-E"]
w_e = [p_E, p_F, "E-F"]
w_f = [p_F, p_G, "F-G"]
w_g = [p_G, p_H, "G-H"]
w_h = [p_H, p_O, "H-O"]

list_wall = [w_a, w_b, w_c, w_d, w_e, w_f, w_g, w_h]


def find_walls(x, y, theta):
    # theta in degrees

    # theta = math.degrees(theta)

    possible_w = list()

    for item in list_wall:
        print("I am doing~~~~~~~~~~~~")
        print(item)
        angle_p1 = math.atan2((item[0][1]-y), (item[0][0]-x))
        angle_p1 = math.degrees(angle_p1)
        if angle_p1 < 0:
            angle_p1+=360
        # print((item[0][1]-y), (item[0][0]-x))

        #angle_p1 = angle_p1 % (2*math.pi)
        angle_p2 = math.atan2((item[1][1]-y), (item[1][0]-x))
        angle_p2 = math.degrees(angle_p2)
        if angle_p2 < 0:
            angle_p2+=360
        #print("hi", (item[1][1]-y),  (item[1][0]-x))
        #angle_p2 = angle_p2 % (2*math.pi)
        print(angle_p1, angle_p2)
        # if theta >= angle_p1
        # if theta in angle_range:
        #     possible_w.append(item)
        # if (theta > angle_p1 and theta < angle_p2) or (theta > angle_p2 and theta < angle_p1):
        print(theta - angle_p1)
        if (theta - angle_p1 <= 0 and theta - angle_p2 >= 0):
            possible_w.append(item)
        elif (theta - angle_p2 <= 0 and theta - angle_p1 >=0):
            possible_w.append(item)
        # if (theta-angle_p1) * (theta - angle_p2) <= 0:
        #     # check if the robot and the wall are parallel..
        #     print('checking, ', math.atan2(item[0][1] - item[1][1], item[0][0] - item[1][0]))
        #     if math.atan2(item[0][1] - item[1][1], item[0][0] - item[1][0])% math.pi != theta % math.pi:
        #         possible_w.append(item)
    return possible_w


def decide_walls():

    pass


if __name__ == "__main__":

    print(find_walls(1, 1, 90))

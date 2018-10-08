# coding=utf-8
import matplotlib.pyplot as plt

from Model1_GBP import simulator_GBP
# from Model2_EquaDiff import simulator_EquaDiff
# from Model3_Gravity import simulator_Gravity

if __name__ == '__main__':
    print "Simulateur à évènements discrets de systèmes hybrides"

    # logs = simulator_GBP.run()
    logs = simulator_GBP.run()
    plt.plot(logs[0], logs[1], drawstyle="steps-post")
    # plt.plot(logs[2], logs[3], drawstyle="steps-post")
    plt.show()

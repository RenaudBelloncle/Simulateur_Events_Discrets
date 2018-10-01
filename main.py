# coding=utf-8
import matplotlib.pyplot as plt

from Model1_GBP import simulator_GBP
from Model2_EquaDiffEuler import simulator_EquaDiffEuler

if __name__ == '__main__':
    print "Simulateur à évènements discrets de systèmes hybrides"

    # logs = simulator_GBP.run()
    logs = simulator_EquaDiffEuler.run()
    plt.plot(logs[0], logs[1], drawstyle="steps-post")
    plt.plot(logs[2], logs[3], drawstyle="steps-post")
    plt.plot(logs[4], logs[5], drawstyle="steps-post")
    plt.show()

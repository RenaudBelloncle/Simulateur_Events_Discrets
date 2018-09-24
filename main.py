# coding=utf-8
import matplotlib.pyplot as plt

from Model2_EquaDiffEuler import simulator

if __name__ == '__main__':
    print "Simulateur à évènements discrets de systèmes hybrides"

    logs = simulator.run()
    plt.plot(logs[0], logs[1], drawstyle="steps-post")
    plt.show()

# coding=utf-8
from Model.Generator import Generator
from Model.Buffer import Buffer
from Model.Processor import Processor
from Model.Dictionary import Dictionary
from Simulator import Simulator
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print "Simulateur à évènements discrets de systèmes hybrides"

    dictionary = Dictionary()

    generator = Generator(dictionary)
    buff = Buffer(dictionary)
    processor = Processor(dictionary)

    dictionary.add_link_component("job", buff)
    dictionary.add_link_component("req", processor)
    dictionary.add_link_component("done", buff)

    simulator = Simulator(20, [generator, buff, processor])
    logs = simulator.run()
    plt.plot(logs[0], logs[1])
    plt.show()
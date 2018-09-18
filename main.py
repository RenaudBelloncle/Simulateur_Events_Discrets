# coding=utf-8
from Model.Generator import Generator
from Model.Buffer import Buffer
from Model.Processor import Processor
from Model.Dictionary import Dictionary
from Simulator import Simulator

if __name__ == '__main__':
    print "Simulateur à évènements discrets de systèmes hybrides"
    dictionary = Dictionary()
    generator = Generator()
    buff = Buffer()
    processor = Processor()
    dictionary.add_link_component("job", buff)
    dictionary.add_link_component("req", processor)
    dictionary.add_link_component("done", buff)
    simulator = Simulator(10, [generator, buff, processor])


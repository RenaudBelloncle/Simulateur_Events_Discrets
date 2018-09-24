from Dictionary import Dictionary
from Model1_GBP.Buffer import Buffer
from Model1_GBP.Generator import Generator
from Model1_GBP.Processor import Processor
from Simulator import Simulator

dictionary = Dictionary()

generator = Generator(dictionary)
buff = Buffer(dictionary)
processor = Processor(dictionary)

dictionary.add_link_component("job", buff)
dictionary.add_link_component("req", processor)
dictionary.add_link_component("done", buff)

simulator_GBP = Simulator(20, [generator, buff, processor])
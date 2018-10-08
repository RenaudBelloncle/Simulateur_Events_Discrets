# coding=utf-8

from AtomicComponent import AtomicComponent
from Event import Event


class Generator(AtomicComponent):

    def __init__(self, name, dictionary):
        super(Generator, self).__init__(name, dictionary)

    def delta_in(self):
        self.current_state = 0
        self.tcomponent = 0
        print "\tGenerator: go to", self.current_state

    def delta_out(self, event):
        pass

    def delta_con(self, event):
        self.delta_out(event)

    def get_ta(self):
        return 2.0 - self.tcomponent

    def lambda_out(self):
        next_state = self.dictionary.get_components("job")
        event = Event("job", "")
        print "\tGenerator: send", event.name, "to", next_state.__class__.__name__
        return [[c, event] for c in self.dictionary.get_components("job")]

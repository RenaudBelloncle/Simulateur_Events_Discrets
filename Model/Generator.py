# coding=utf-8

from AtomicComponent import AtomicComponent
from Model.Event import Event


class Generator(AtomicComponent):
    dictionary = None
    tcomponent = None

    def __init__(self, dictionary):
        super(Generator, self).__init__()
        self.dictionary = dictionary
        self.tcomponent = 0

    def delta_con(self, event):
        self.delta_out(event)

    def delta_out(self, event):
        pass

    def delta_int(self):
        self.current_state = 0
        self.tcomponent = 0
        print "\t\t\tGenerator: go to", self.current_state

    def lambda_out(self):
        next_state = self.dictionary.get_components("job")
        event = Event("job", "")
        print "\t\t\tGenerator: send", event.name, "to", next_state.__class__.__name__
        return [next_state, event]

    def get_ta(self):
        return 2.0 - self.tcomponent

    def increase_time(self, t):
        self.tcomponent = self.tcomponent + t

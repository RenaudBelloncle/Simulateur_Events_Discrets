# coding=utf-8

from AtomicComponent import AtomicComponent
from Event import Event


class Processor(AtomicComponent):

    def __init__(self, dictionary):
        super(Processor, self).__init__(dictionary)

    def delta_int(self):
        if self.current_state == 1:
            self.current_state = 0
            self.tcomponent = 0
        print "\t\t\tProcessor: go to", self.current_state

    def delta_out(self, event):
        if self.current_state == 0:
            self.current_state = 1
            self.tcomponent = 0
        print "\t\t\tProcessor: go to", self.current_state

    def delta_con(self, event):
        self.delta_out(event)

    def lambda_out(self):
        next_state = self.dictionary.get_components("done")
        event = Event("done", "")
        print "\t\t\tProcessor: send", event.name, "to", next_state.__class__.__name__
        return [next_state, event]

    def get_ta(self):
        if self.current_state == 0:
            return float("inf")
        else:
            return 3 - self.tcomponent

    def increase_time(self, t):
        self.tcomponent = self.tcomponent + t

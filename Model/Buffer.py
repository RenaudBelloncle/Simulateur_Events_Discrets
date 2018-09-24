# coding=utf-8

from AtomicComponent import AtomicComponent
from Model.Event import Event


class Buffer(AtomicComponent):
    q = None

    def __init__(self, dictionary):
        super(Buffer, self).__init__(dictionary)
        self.dictionary = dictionary
        self.tcomponent = 0
        self.q = 0

    def delta_con(self, event):
        print "Buffer : Conflit entre un delta_out et un delta_in "
        self.delta_out(event)
        pass

    def delta_out(self, event):
        state = self.current_state
        if state == 0:
            self.current_state = 1
            self.q += 1
            self.tcomponent = 0
        elif state == 1:
            self.current_state = 1
            self.q += 1
            self.tcomponent = 0
        elif state == 2:
            if event[0].get_name() == "job":
                self.current_state = 2
                self.q += 1
                self.tcomponent = 0
            else:
                if self.q == 0:
                    self.current_state = 0
                    self.tcomponent = 0
                else:
                    self.current_state = 1
                    self.tcomponent = 0
        print "\t\t\tBuffer: go to", self.current_state

    def delta_int(self):
        if self.current_state == 1:
            self.current_state = 2
            self.tcomponent = 0
            self.q = self.q - 1
        print "\t\t\tBuffer: go to", self.current_state

    def lambda_out(self):
        next_state = self.dictionary.get_components("req")
        event = Event("req", "")
        print "\t\t\tBuffer: send", event.name, "to", next_state.__class__.__name__
        return [self.dictionary.get_components("req"), event]

    def get_ta(self):
        if self.current_state == 0:
            return float("inf")
        elif self.current_state == 1:
            return 0
        elif self.current_state == 2:
            return float("inf")

    def increase_time(self, t):
        self.tcomponent = self.tcomponent + t

    def get_q(self):
        return self.q

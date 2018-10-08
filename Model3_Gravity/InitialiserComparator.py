from AtomicComponent import AtomicComponent
from Event import Event


class InitialiserComparator(AtomicComponent):
    init = None
    coef = None
    h = None

    def __init__(self, name, dictionary, init, coef, h):
        super(InitialiserComparator, self).__init__(name, dictionary)
        self.init = init
        self.coef = coef
        self.h = h

    def delta_in(self):
        if self.current_state == 0:
            self.current_state = 1
            self.tcomponent = 0
        elif self.current_state == 2:
            self.current_state = 1
            self.tcomponent = 0

    def delta_out(self, event):
        if self.current_state == 1:
            if (event[0].data < self.h) and (event[0].data > -self.h):
                self.current_state = 2
                self.tcomponent = 0

    def delta_con(self, event):
        self.delta_out(event)

    def get_ta(self):
        if self.current_state == 0:
            return 0.0
        elif self.current_state == 1:
            return float("inf")
        elif self.current_state == 2:
            return 0.0

    def lambda_out(self):
        if self.current_state == 0:
            event = Event("v", self.init)
            return [[c, event] for c in self.dictionary.get_components("v")]
        elif self.current_state == 2:
            event = Event("v", self.coef)
            return [[c, event] for c in self.dictionary.get_components("v")]

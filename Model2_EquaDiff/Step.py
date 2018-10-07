from AtomicComponent import AtomicComponent
from Event import Event


class Step(AtomicComponent):
    xi = None
    xf = None
    ts = None

    def __init__(self, name, dictionary, xi, xf, ts):
        super(Step, self).__init__(name, dictionary)
        self.xi = xi
        self.xf = xf
        self.ts = ts

    def delta_in(self):
        if self.current_state == 0:
            self.current_state = 1
            self.tcomponent = 0
        elif self.current_state == 1:
            self.current_state = 2
            self.tcomponent = 0

    def delta_out(self, event):
        pass

    def delta_con(self, event):
        self.delta_out(event)

    def get_ta(self):
        if self.current_state == 0:
            return 0.0
        elif self.current_state == 1:
            return self.ts - self.tcomponent
        else:
            return float("inf")

    def lambda_out(self):
        if self.current_state == 0:
            event = Event("step", self.xi)
            return [[c, event] for c in self.dictionary.get_components("step")]
        elif self.current_state == 1:
            event = Event("step", self.xf - self.xi)
            return [[c, event] for c in self.dictionary.get_components("step")]

from AtomicComponent import AtomicComponent
from Event import Event


class Step(AtomicComponent):
    xi = None
    xf = None
    ts = None

    def __init__(self, dictionary, xi, xf, ts):
        super(Step, self).__init__(dictionary)
        self.xi = xi
        self.xf = xf
        self.ts = ts

    def increase_time(self, t):
        self.tcomponent += t

    def lambda_out(self):
        if self.current_state == 0:
            event = Event("step", self.xi)
            return [self.dictionary.get_components("step"), event]
        elif self.current_state == 1:
            event = Event("step", self.xf)
            return [self.dictionary.get_components("step"), event]

    def get_ta(self):
        if self.current_state == 0:
            return 0
        elif self.current_state == 1:
            return self.ts
        else:
            return float("inf")

    def delta_con(self, event):
        pass

    def delta_out(self, event):
        pass

    def delta_int(self):
        if self.current_state == 0:
            self.current_state = 1
            self.tcomponent = 0
        elif self.current_state == 1:
            self.current_state = 2
            self.tcomponent = 0

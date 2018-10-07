from AtomicComponent import AtomicComponent
from Event import Event


class Initialiser(AtomicComponent):
    init = None

    def __init__(self, name, dictionary, init):
        super(Initialiser, self).__init__(name, dictionary)
        self.init = init

    def delta_in(self):
        if self.current_state == 0:
            self.current_state = 1
            self.tcomponent = 0

    def delta_out(self, event):
        pass

    def delta_con(self, event):
        self.delta_out(event)

    def get_ta(self):
        if self.current_state == 0:
            return 0.0
        elif self.current_state == 1:
            return float("inf")

    def lambda_out(self):
        if self.current_state == 0:
            event = Event("h", self.init)
            return [[c, event] for c in self.dictionary.get_components("h")]

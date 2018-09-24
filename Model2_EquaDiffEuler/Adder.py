# coding=utf-8
from AtomicComponent import AtomicComponent
from Event import Event


class Adder(AtomicComponent):
    e1 = None
    e2 = None
    e3 = None
    e4 = None

    def __init__(self, dictionary):
        super(Adder, self).__init__(dictionary)

    def increase_time(self, t):
        self.tcomponent += t

    def lambda_out(self):
        event = Event("adder", self.e1 + self.e2 + self.e3 + self.e4)
        return [self.dictionary.get_components("adder"), event]

    def get_ta(self):
        if self.current_state == 0:
            return float("inf")
        else:
            return 0

    def delta_con(self, event):
        print "Adder : On a reçu de nouvelles valeurs alors qu'on peut envoyer"
        self.delta_out(event)

    def delta_out(self, event):
        if self.current_state == 0:
            self.current_state = 1
            self.tcomponent = 0
        elif self.current_state == 1:
            self.current_state = 1
            self.tcomponent = 0

    def delta_int(self):
        if self.current_state == 1:
            self.current_state = 0
            self.tcomponent = 0

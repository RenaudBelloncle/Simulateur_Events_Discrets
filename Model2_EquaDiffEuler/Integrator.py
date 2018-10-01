# coding=utf-8
from AtomicComponent import AtomicComponent
from Event import Event


class Integrator(AtomicComponent):
    xdot = None
    x = None
    h = None
    sigma = None

    def __init__(self, name, dictionary, x, h):
        super(Integrator, self).__init__(name, dictionary)
        self.xdot = 0.0
        self.x = x
        self.h = h
        self.sigma = h

    def increase_time(self, t):
        self.tcomponent += t

    def lambda_out(self):
        event = Event("sortie", self.x + self.sigma * self.xdot)
        return [self.dictionary.get_components("sortie"), event]

    def get_ta(self):
        if self.current_state == 0:
            return self.h - self.tcomponent

    def delta_con(self, event):
        print "Adder : On a reçu de nouvelles valeurs alors qu'on peut envoyer"
        self.delta_out(event)

    def delta_out(self, event):
        if self.current_state == 0:
            self.current_state = 0
            self.sigma = self.h - self.tcomponent
            self.x = self.x + self.tcomponent * self.xdot
            self.xdot = event[0].data

    def delta_int(self):
        if self.current_state == 0:
            self.current_state = 0
            self.tcomponent = 0
            self.x = self.x + self.sigma * self.xdot
            self.sigma = self.h

    def get_x(self):
        return self.x

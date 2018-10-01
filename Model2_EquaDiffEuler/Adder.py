# coding=utf-8
import numpy as np

from AtomicComponent import AtomicComponent
from Event import Event


class Adder(AtomicComponent):
    s = None

    def __init__(self, name, dictionary):
        super(Adder, self).__init__(name, dictionary)
        self.s = 0

    def increase_time(self, t):
        self.tcomponent += t

    def lambda_out(self):
        event = Event("adder", self.s)
        return [[c, event] for c in self.dictionary.get_components("adder")]

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
            self.s = self.s + np.sum([e.data for e in event])
            self.tcomponent = 0
        elif self.current_state == 1:
            self.current_state = 1
            self.s = self.s + np.sum([e.data for e in event])
            self.tcomponent = 0

    def delta_int(self):
        if self.current_state == 1:
            self.current_state = 0
            self.tcomponent = 0

    def get_s(self):
        return self.s

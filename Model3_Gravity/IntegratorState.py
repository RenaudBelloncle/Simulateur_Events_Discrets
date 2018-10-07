# coding=utf-8
import numpy as np

from AtomicComponent import AtomicComponent
from Event import Event


class IntegratorState(AtomicComponent):
    qdot = None
    q = None
    delta_q = None
    sigma = None

    def __init__(self, name, dictionary, delta_q):
        super(IntegratorState, self).__init__(name, dictionary)
        self.qdot = 0.0
        self.q = -1.0
        self.delta_q = delta_q
        self.sigma = float("inf")

    def increase_time(self, t):
        self.tcomponent += t

    def lambda_out(self):
        if self.current_state == 1:
            if self.name == "integratorStateVit":
                event_name = "vit"
            else:
                event_name = "pos"
            event = Event(event_name, self.q + self.delta_q * np.sign(self.qdot))
            return [[c, event] for c in self.dictionary.get_components(event_name)]

    def get_ta(self):
        if self.current_state == 0:
            return float("inf")
        elif self.current_state == 1:
            return self.sigma - self.tcomponent

    def delta_con(self, event):
        self.delta_out(event)

    def delta_out(self, event):
        for e in event:
            if e.name == "h" or e.name == "v":
                self.event_init(e)
            elif e.name == "acc" or e.name == "vit":
                self.event_qdot(e)

    def event_init(self, event):
        self.current_state = 1
        self.q = - self.q * event.data
        if self.qdot == 0:
            self.sigma = float("inf")
        else:
            # self.sigma = self.delta_q / np.abs(self.qdot)
            self.sigma = 0
        self.tcomponent = 0

    def event_qdot(self, event):
        self.current_state = 1
        ql = self.q
        self.q = self.q + self.tcomponent * self.qdot
        self.qdot = event.data
        if self.qdot == 0:
            self.sigma = float("inf")
        else:
            self.sigma = (self.delta_q - np.abs(self.q - ql)) / np.abs(self.qdot)
        self.tcomponent = 0

    def delta_in(self):
        if self.current_state == 1:
            self.current_state = 1
            self.tcomponent = 0
            self.q = self.q + self.delta_q * np.sign(self.qdot)
            if self.qdot == 0:
                self.sigma = float("inf")
            else:
                self.sigma = self.delta_q / np.abs(self.qdot)

    def get_q(self):
        return self.q

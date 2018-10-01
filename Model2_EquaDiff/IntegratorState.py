# coding=utf-8
import numpy as np

from AtomicComponent import AtomicComponent
from Event import Event


class IntegratorState(AtomicComponent):
    qdot = None
    q = None
    delta_q = None
    sigma = None

    def __init__(self, name, dictionary, q, delta_q):
        super(IntegratorState, self).__init__(name, dictionary)
        self.qdot = 0.0
        self.q = q
        self.delta_q = delta_q
        self.sigma = float("inf")

    def increase_time(self, t):
        self.tcomponent += t

    def lambda_out(self):
        event = Event("sortie", self.q + self.delta_q * np.sign(self.qdot))
        return [[c, event] for c in self.dictionary.get_components("sortie")]

    def get_ta(self):
        if self.current_state == 0:
            return self.sigma - self.tcomponent

    def delta_con(self, event):
        self.delta_out(event)

    def delta_out(self, event):
        if self.current_state == 0:
            self.current_state = 0
            self.tcomponent = 0
            ql = self.q
            self.q = self.q + self.tcomponent * self.qdot
            self.qdot = event[0].data
            self.sigma = (self.delta_q - np.abs(self.q - ql)) / np.abs(self.qdot)

    def delta_in(self):
        if self.current_state == 0:
            self.current_state = 0
            self.tcomponent = 0
            self.q = self.q + self.delta_q * np.sign(self.qdot)
            self.sigma = self.delta_q / np.abs(self.qdot)

    def get_q(self):
        return self.q

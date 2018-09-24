# coding=utf-8

from AtomicComponent import AtomicComponent
from Model import Dictionary


class Processor(AtomicComponent):
    tcomponent = None

    def __init__(self):
        pass

    def delta_con(self):
        pass

    def delta_out(self):
        if self.current_state == 0:
            self.current_state = 1

    def delta_int(self):
        if self.current_state == 1:
            self.current_state = 0

    def lambda_out(self):
        return Dictionary.get_components("Done")

    def get_ta(self):
        if self.current_state == 0:
            return float("inf")
        else:
            return 3

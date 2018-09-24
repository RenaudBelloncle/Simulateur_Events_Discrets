# coding=utf-8

from abc import ABCMeta, abstractmethod


class AtomicComponent:
    __metaclass__ = ABCMeta
    current_state = None

    @abstractmethod
    def __init__(self):
        self.current_state = 0

    @abstractmethod
    def delta_int(self):
        pass

    @abstractmethod
    def delta_out(self, event):
        pass

    @abstractmethod
    def delta_con(self):
        pass

    @abstractmethod
    def get_ta(self):
        pass

    @abstractmethod
    def lambda_out(self):
        pass

# coding=utf-8

from abc import ABCMeta, abstractmethod


class AtomicComponent:
    __metaclass__ = ABCMeta
    name = None
    current_state = None
    dictionary = None
    tcomponent = None

    @abstractmethod
    def __init__(self, name, dictionary):
        self.name = name
        self.current_state = 0
        self.dictionary = dictionary
        self.tcomponent = 0

    @abstractmethod
    def delta_in(self):
        pass

    @abstractmethod
    def delta_out(self, event):
        pass

    @abstractmethod
    def delta_con(self, event):
        pass

    @abstractmethod
    def get_ta(self):
        pass

    @abstractmethod
    def lambda_out(self):
        return []

    @abstractmethod
    def increase_time(self, t):
        pass

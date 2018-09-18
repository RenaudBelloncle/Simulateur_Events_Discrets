from abc import ABCMeta, abstractmethod


class AtomicComponent:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def dela_int(self):
        pass

    @abstractmethod
    def dela_out(self):
        pass

    @abstractmethod
    def dela_con(self):
        pass

    @abstractmethod
    def get_ta(self):
        pass

    @abstractmethod
    def lambda_out(self):
        pass

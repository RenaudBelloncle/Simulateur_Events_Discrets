# coding=utf-8

from AtomicComponent import AtomicComponent


class Processor(AtomicComponent):
    dictionary = None
    tcomponent = None

    def __init__(self, dictionary):
        super(Processor, self).__init__()
        self.dictionary = dictionary

    def delta_con(self, event):
        pass

    def delta_out(self, event):
        if self.current_state == 0:
            self.current_state = 1

    def delta_int(self):
        if self.current_state == 1:
            self.current_state = 0

    def lambda_out(self):
        return self.dictionary.get_components("Done")

    def get_ta(self):
        if self.current_state == 0:
            return float("inf")
        else:
            return 3

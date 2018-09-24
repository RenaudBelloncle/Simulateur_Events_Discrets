# coding=utf-8

from AtomicComponent import AtomicComponent


class Generator(AtomicComponent):

    dictionary = None
    tcomponent = None

    def __init__(self, dictionary):
        super(Generator, self).__init__()
        self.dictionary = dictionary
        self.tcomponent = 0

    def delta_con(self, event):
        pass

    def delta_out(self, event):
        pass

    def delta_int(self):
        self.current_state = 0

    def lambda_out(self):
        return self.dictionary.get_components("job")

    def get_ta(self):
        return 2.0

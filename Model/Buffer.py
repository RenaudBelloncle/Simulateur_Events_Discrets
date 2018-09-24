# coding=utf-8

from AtomicComponent import AtomicComponent


class Buffer(AtomicComponent):
    dictionary = None
    tcomponent = None
    q = None

    def __init__(self, dictionary):
        super(Buffer, self).__init__()
        self.dictionary = dictionary
        self.tcomponent = 0
        self.q = 0

    def delta_con(self):
        # TODO : Réfléchir à comment implémenter le delta_con
        pass

    def delta_out(self, event):
        state = self.current_state
        if state == 0:
            self.current_state = 1
            self.q += 1
        elif state == 1:
            self.current_state = 1
            self.q += 1
        elif state == 2:
            if event.get_name() == "job":
                self.current_state = 2
                self.q += 1
            else:
                if self.q == 0:
                    self.current_state = 0
                else:
                    self.current_state = 1

    def delta_int(self):
        if self.current_state == 1:
            self.current_state = 2
        else:
            pass

    def lambda_out(self):
        return self.dictionary.get_components("req")

    def get_ta(self):
        if self.current_state == 0:
            return float("inf")
        elif self.current_state == 1:
            return 0
        elif self.current_state == 2:
            return float("inf")

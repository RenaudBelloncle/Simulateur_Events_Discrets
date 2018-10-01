from AtomicComponent import AtomicComponent


class Output(AtomicComponent):

    def __init__(self, name, dictionary):
        super(Output, self).__init__(name, dictionary)

    def delta_int(self):
        pass

    def delta_out(self, event):
        pass

    def delta_con(self, event):
        pass

    def get_ta(self):
        pass

    def lambda_out(self):
        return []

    def increase_time(self, t):
        pass

from AtomicComponent import AtomicComponent
from Dictionary import Dictionary


class Generator(AtomicComponent):
    tcomponent = None

    def __init__(self):
        self.tcomponent = 0

    def delta_con(self):
        pass

    def delta_out(self):
        pass

    def delta_int(self):
        self.current_state = 0

    def lambda_out(self):
        return Dictionary.get_components("job")

    def get_ta(self):
        return 2.0

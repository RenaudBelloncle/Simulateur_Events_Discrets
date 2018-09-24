# coding=utf-8

import numpy as np

from Model1_GBP.Buffer import Buffer


class Simulator:
    tfinal = None
    components = None

    def __init__(self, tfinal, components):
        self.tfinal = tfinal
        self.components = components

    def init_step(self):
        ta_comp = [c.get_ta() for c in self.components]
        tmin = np.min(ta_comp)
        print "\ttmin :", tmin

        imms = [c for c in self.components if c.get_ta() == tmin]
        print "\timms :", [c.__class__.__name__ for c in imms]

        return tmin, imms

    def process_time(self, tmin, imms):
        impact_event = [i.lambda_out() for i in imms]
        impact = [ie[0] for ie in impact_event]
        print "\t\timpact :", [c.__class__.__name__ for c in impact]

        for c in self.components:
            if (c not in impact) and (c in imms):
                c.delta_int()
            elif (c in impact) and (c not in imms):
                event = [ie[1] for ie in impact_event if ie[0] == c]
                c.delta_out(event)
            elif (c in impact) and (c in imms):
                event = [ie[1] for ie in impact_event if ie[0] == c]
                c.delta_con(event)
            else:
                c.increase_time(tmin)

    def run(self):
        t = 0.0
        buf = [c for c in self.components if isinstance(c, Buffer)][0]
        arg_in_time = [[0], [0]]

        while t < self.tfinal:
            print "Init Etape", t, "/", self.tfinal
            tmin, imms = self.init_step()

            print "\tEtape", t + tmin, "/", self.tfinal
            self.process_time(tmin, imms)

            arg_in_time[0].append(t + tmin)
            arg_in_time[1].append(buf.get_q())

            t = t + tmin

        return arg_in_time

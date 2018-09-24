# coding=utf-8

import numpy as np

from Model.Buffer import Buffer


class Simulator:
    tfinal = None
    components = None

    def __init__(self, tfinal, components):
        self.tfinal = tfinal
        self.components = components

    def process_time(self):
        pass

    def run(self):
        t = 0.0
        buf = [c for c in self.components if isinstance(c, Buffer)][0]
        q_in_time = [[t, buf.get_q()]]

        while t < self.tfinal:
            print "Init Etape", t, "/", self.tfinal

            ta_comp = [c.get_ta() for c in self.components]
            tmin = np.min(ta_comp)
            print "\ttmin :", tmin

            imms = [c for c in self.components if c.get_ta() == tmin]
            print "\timms :", [c.__class__.__name__ for c in imms]

            q_in_time.append([t+tmin, buf.get_q()])
            print "\t q:", q_in_time

            print "\tEtape", t + tmin, "/", self.tfinal
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

            t = t + tmin

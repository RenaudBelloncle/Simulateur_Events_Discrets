# coding=utf-8

import numpy as np


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
        print "\tImminent Components :", [c.name for c in imms]

        return tmin, imms

    def process_time(self, tmin, imms):
        impact_event = [i.lambda_out() for i in imms]
        impact = [ie[0] for ie in impact_event]
        print "\tImpacted Components :", np.unique([c.name for c in impact])

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
        from Model2_EquaDiffEuler import Integrator

        t = 0.0
        # buf = [c for c in self.components if isinstance(c, Buffer)][0]
        integrator = [c for c in self.components if isinstance(c, Integrator)][0]
        arg_in_time = [[0], [0]]

        while t < self.tfinal:
            print "State initialisation -", t, "/", self.tfinal
            tmin, imms = self.init_step()

            print "State process -", t + tmin, "/", self.tfinal
            self.process_time(tmin, imms)

            # arg_in_time[0].append(t + tmin)
            # arg_in_time[1].append(buf.get_q())
            arg_in_time[0].append(t + tmin)
            arg_in_time[1].append(integrator.get_x())

            t = t + tmin

        return arg_in_time

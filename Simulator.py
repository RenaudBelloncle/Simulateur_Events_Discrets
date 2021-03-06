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

        imms = [c for c in self.components if c.get_ta() == tmin]

        return tmin, imms

    def process_time(self, tmin, imms):
        impact_event = [lo for i in imms for lo in i.lambda_out()]
        impact = [ie[0] for ie in impact_event]

        for c in self.components:
            if (c not in impact) and (c in imms):
                c.delta_in()
            elif (c in impact) and (c not in imms):
                event = [ie[1] for ie in impact_event if ie[0] == c]
                c.delta_out(event)
            elif (c in impact) and (c in imms):
                event = [ie[1] for ie in impact_event if ie[0] == c]
                c.delta_con(event)
            else:
                c.increase_time(tmin)

    def run(self):
        # from Model1_GBP import Buffer
        # from Model2_EquaDiff import Adder
        # from Model2_EquaDiff import IntegratorTime
        # from Model2_EquaDiff import IntegratorState
        from Model3_Gravity import IntegratorState

        t = 0.0
        # buf = [c for c in self.components if isinstance(c, Buffer)][0]
        # arg_in_time = [[], []]

        # adder = [c for c in self.components if isinstance(c, Adder)][0]
        # integrator_time = [c for c in self.components if isinstance(c, IntegratorTime)][0]
        # integrator_state = [c for c in self.components if isinstance(c, IntegratorState)][0]
        # arg_in_time = [[], [], [], [], [], []]

        integrator_vit = [c for c in self.components if isinstance(c, IntegratorState)][0]
        integrator_pos = [c for c in self.components if isinstance(c, IntegratorState) and c != integrator_vit][0]
        arg_in_time = [[], [], [], []]

        while t < self.tfinal:
            tmin, imms = self.init_step()

            self.process_time(tmin, imms)

            # arg_in_time[0].append(t + tmin)
            # arg_in_time[1].append(buf.get_q())

            # arg_in_time[0].append(t + tmin)
            # arg_in_time[1].append(adder.get_s())
            # arg_in_time[2].append(t + tmin)
            # arg_in_time[3].append(integrator_time.get_x())
            # arg_in_time[4].append(t + tmin)
            # arg_in_time[5].append(integrator_state.get_q())

            arg_in_time[0].append(t + tmin)
            arg_in_time[1].append(integrator_vit.get_q())
            arg_in_time[2].append(t + tmin)
            arg_in_time[3].append(integrator_pos.get_q())

            t = t + tmin

        return arg_in_time

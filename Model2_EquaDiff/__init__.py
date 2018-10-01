# coding=utf-8

from Dictionary import Dictionary
from Model2_EquaDiff.Step import Step
from Model2_EquaDiff.Adder import Adder
from Model2_EquaDiff.IntegratorTime import IntegratorTime
from Model2_EquaDiff.IntegratorState import IntegratorState
from Model2_EquaDiff.Output import Output
from Simulator import Simulator

dico = Dictionary()

s1 = Step("step1", dico, 1.0, -3.0, 0.65)
s2 = Step("step2", dico, 0.0, 1.0, 0.35)
s3 = Step("step3", dico, 0.0, 1.0, 1.0)
s4 = Step("step4", dico, 0.0, 4.0, 1.5)
adder = Adder("adder", dico)
integrator_time = IntegratorTime("integratorTime", dico, 0.0, 10e-4)
integrator_state = IntegratorState("integratorState", dico, 0.0, 10e-4)
output = Output("output", dico)

dico.add_link_component("step", [adder])
dico.add_link_component("adder", [integrator_time, integrator_state])
dico.add_link_component("sortie", [output])

simulator_EquaDiff = Simulator(2, [s1, s2, s3, s4, adder, integrator_time, integrator_state])

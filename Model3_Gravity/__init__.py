# coding=utf-8
from Dictionary import Dictionary
from Model3_Gravity.Constant import Constant
from Model3_Gravity.IntegratorState import IntegratorState
from Model3_Gravity.Output import Output
from Simulator import Simulator

dico = Dictionary()

c = Constant("constant", dico, -9.81)
integrator_vit = IntegratorState("integratorStateVit", dico, 0.0, 0.1)
integrator_pos = IntegratorState("integratorStatePos", dico, 10.0, 0.001)
output = Output("output", dico)

dico.add_link_component("acc", [integrator_vit])
dico.add_link_component("vit", [integrator_pos])
dico.add_link_component("pos", [output])

simulator_Gravity = Simulator(2, [c, integrator_vit, integrator_pos])

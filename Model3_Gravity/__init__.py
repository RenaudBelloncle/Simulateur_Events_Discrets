# coding=utf-8
from Dictionary import Dictionary
from Model3_Gravity.InitialiserComparator import InitialiserComparator
from Model3_Gravity.Constant import Constant
from Model3_Gravity.Initialiser import Initialiser
from Model3_Gravity.InitialiserComparator import InitialiserComparator
from Model3_Gravity.IntegratorState import IntegratorState
from Simulator import Simulator

dico = Dictionary()

c = Constant("constant", dico, -9.81)
integrator_vit = IntegratorState("integratorStateVit", dico, 0.1)
integrator_pos = IntegratorState("integratorStatePos", dico, 0.001)
pos_initialiser = Initialiser("posInitialiser", dico, 10.0)
vit_initialiser = InitialiserComparator("vitInitialiser", dico, 0.0, 0.8)

dico.add_link_component("acc", [integrator_vit])
dico.add_link_component("vit", [integrator_pos])
dico.add_link_component("pos", [vit_initialiser])
dico.add_link_component("v", [integrator_vit])
dico.add_link_component("h", [integrator_pos])

simulator_Gravity = Simulator(10, [pos_initialiser, vit_initialiser, c, integrator_vit, integrator_pos])

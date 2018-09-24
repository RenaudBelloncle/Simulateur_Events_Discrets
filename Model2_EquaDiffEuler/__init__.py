from Dictionary import Dictionary
from Model2_EquaDiffEuler.Adder import Adder
from Model2_EquaDiffEuler.Integrator import Integrator
from Simulator import Simulator
from Step import Step

dico = Dictionary()

s1 = Step(dico, 1, -3, 0.65)
s2 = Step(dico, 0, 1, 0.35)
s3 = Step(dico, 0, 1, 0.65)
s4 = Step(dico, 0, 4, 1.5)
adder = Adder(dico)
integrator = Integrator(dico, 0, 10e-4)

dico.add_link_component("step", adder)
dico.add_link_component("adder", integrator)
dico.add_link_component("sortie", None)

simulator = Simulator(2, [s1, s2, s3, s4, adder, integrator])

# Simple particle diffusion example in one dimension
#
# calculate mean displacement of 1000 particles after 1000 steps of step size 1

from statistics import mean
import miniabm
import random

displacement = miniabm.agents().crt(1000, x=0).set(1000, x=lambda x: x + random.choice([-1, 1])).tell('x')

print(mean(displacement))

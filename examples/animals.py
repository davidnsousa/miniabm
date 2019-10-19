# Simple example of natural selection
#
# different species have different reproducibility
# at each time-step one of the animals with highest reproducibility will reproduce
# animals can live 20 time-steps at most

import miniabm
import random

animals = miniabm.agents()

# create 3 animals of 3 different species
# set whatever attributes you wish
animals().crt(3, species=1, color='blue')
animals().crt(3, species=2, color='green')
animals().crt(3, species=3, color='red')

# in what follows, various examples are provided on how to set or change attributes
# (note that all of them could have already been set with .crt())
# to set or change attributes selectively use:
# .w(), .other(), .who(), .w_min(), .w_max(), .n_of(), .clone() followed by .set()
# lambda functions can be used to set or change attributes dynamically
# you can combine and repeat all of these methods in any order you wish
animals().w(species=1).set(weight=10)
animals().w(species=lambda x: x > 1, color='green').set(weight=5)
animals().w(species=lambda x: x not in [1, 2]).set(weight=7)
animals().w(color='blue').set(size=2)
animals().w(color='blue').other().set(size=4)
animals().set(age=lambda x: random.randint(0, 20))
animals().w(species=1).set(reproducibility=random.randint(0, 100))
animals().w(species=2).set(reproducibility=random.randint(0, 100))
animals().w(species=3).set(reproducibility=random.randint(0, 100))


# change objects one by one selectively with .slist()
for x in animals().slist():
    # assume all agents live exactly 100 years
    x.lifetime = 20 - x.age

# use .show() to print attributes of objects under selection
print("population:")
animals().show()

timesteps = range(10)
for t in timesteps:
    # increase age and decrease energy
    animals().set(age=lambda x: x + 1, lifetime=lambda x: x - 1)
    # use .remove() to kill animals with no energy
    animals().w(lifetime=0).remove()
    # use .n_of(1) to choose one animal to breed from those with highest reproducibility
    # use .ids() to extract the id of the chosen one
    chosen_one = animals().w_max('reproducibility').n_of(1).ids()
    # use .who() combined with .clone() to clone tho chosen one
    # cloning the chosen one gives its clone the same attributes
    # reset the clone's age and energy
    animals().who(chosen_one).clone(1).set(age=0, lifetime=100)

print("population after 10 timesteps:")
animals().show()
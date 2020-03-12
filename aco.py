import time
import numpy as np
import random
from aco_functions import *
from preprocessing import *

ants = []



rule_matrix = get_matrix()

#print(get_cutpoint(rule_matrix[0][0][0],cols))

for ant in ants:
    build_solution()
    update_pheromone()


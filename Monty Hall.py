#!/usr/bin/env python3

import random
import numpy as np
import argparse


def switch(winning_door):
    # This function first checks if the winning door is the one selected.
    # If so, a switch will always result in a loss, so 0 is returned. Otherwise,
    # A random door that's not the successful one or the one selected is
    # "opened" by removing it from the list. Then, a random new door is selected
    # from the remaining options, and the program checks if the new door is the
    # one that corresponds with a success.

    if door_choice == winning_door:
        return 0

    # Picks a door to "open" from the available options.
    removable_doors = list(range(doors))
    removable_doors.remove(door_choice)
    removable_doors.remove(winning_door)
    removed_door = random.randint(0, len(removable_doors) - 1)

    # Removes the opened door, randomly picks a new choice, and checks success.
    pickable_doors = list(range(doors))
    pickable_doors.remove(door_choice)
    pickable_doors.remove(removable_doors[removed_door])
    new_choice = random.randint(0, len(pickable_doors) - 1)
    return int(pickable_doors[new_choice] == winning_door)


# Creates the description for the program and sets arguments to take.
parser = argparse.ArgumentParser(description="""
This program takes three arguments which are different parameters
used in the simulation of the Monty-Hall problem. The first argument
is an integer, n, the number of trials used in the simulation. The
second is an integer which specifies the total number of doors to be
used in the simulation. The third is the door which the user selects
as a door to be chosen for each simulation.
""")

parser.add_argument('n', type=int, help='number of trials used in the Monty Hall problem simulation')
parser.add_argument('doors', type=int, help='the number of doors used in the simulation')
parser.add_argument('door_choice', type=int, help='the index of the door chosen by the user')
args = parser.parse_args()

n, doors, door_choice = args.n, args.doors, args.door_choice

# Creates two arrays to track the successes for both the case in which the user switches the door
# and in the case when the door is not switched. In the case of no switching, opening a door does
# not impact the result, so the removal is not calculated.
no_switch_array = np.empty(0)
switch_array = np.empty(0)
for i in range(n):
    # Picks a random winning door for each trial and runs both cases
    winning_door = random.randint(0, doors - 1)
    no_switch_array = np.append(no_switch_array, int(door_choice == winning_door))
    switch_array = np.append(switch_array, switch(winning_door))

# Calculates the probability of success for each case
no_switch_success = np.sum(no_switch_array)/no_switch_array.size
switch_success = np.sum(switch_array)/switch_array.size
print('Probability of success with no switch:', no_switch_success)
print('Probability of success with a random switch:', switch_success)

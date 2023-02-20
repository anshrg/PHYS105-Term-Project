# Monty Hall Problem Simulation
PHYS105 (Introduction to Scientific Computing) Term Project; Monty
Hall problem simulation and analysis

The template for this assignment was generated via Github Classroom, so the 
original private project cannot be made public or forked. Here, I reproduce 
my work to make it public. Final commit on original project was on March 14,
2022. Published February 19, 2023.

The Monty Hall problem is a puzzle in statistics and
probability derived from the premise of an old game show (and is
named after its host). It considers a contestant facing
three unopened doors - a prize lies behind one door with nothing
beyond the others. In the show, after the contestant makes a
selection, the host opens one of the remaning doors that does not
contain the prize. The player then has the opportunity to switch
to the remaining unopened door or to stick with their choice.

Surprisingly, there is actually a strategic advantage to switching
to the unopened door instead of keeping the original choice. In fact,
with three doors, the odds of success double if the contestant switches.
To understand this unexpected result, this program simulates the result
of a generalized Monty Hall problem with a free number of doors.

To compare odds, the program runs both the cases in which the player does
and does not decide to switch. If the player does not switch, it doesn't
matter if a door is opened, since the strategy is already determined. In
the switching case, the program opens an empty door (excluding the player's 
original choice and the winning door) and randomly makes a new choice for 
the player. This simulation is run for a number of trials and the final
probability of success for both cases is returned to the user.

The program accepts three parameters: n - the number of trials, doors - the
number of doors, and door_choice - the door the user chooses for each trial.

As one might expect, as the number of doors increases, the relative
success of the switching strategy goes down. This is because the key piece
of information that aids the strategy (the opening of a door) is less
valuable as the number of options to switch to goes up. Still, the
strategy gives a significant boost in odds for 5 and even 10 doors.

In the future, the simulation could be generalized further by allowing
for more than one successful door, more than one choice by the player,
and by creating a non-binary situation in which each door could have
one of multiple (>2) outcomes instead of just success or failure.

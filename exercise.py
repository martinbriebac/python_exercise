
# Exercise 1
# Create a new file named exercise.py
# Print "Hello World!"  


# print('Hello World!')


# Exercise 2 Guido's Gorgeous Lasagna
'''
PREPARATION_TIME = 2
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

print(bake_time_remaining(50))

def preparation_time_in_minutes(layers):
    """Calculate preparation time.

    :param layers: int - time it takes for each layer.
    :return: int - how many layers times PREPARATION_TIME.

    This function takes how many layers have been done and multiplies for the time it takes to prepare one layer
    """

    return PREPARATION_TIME * layers

print(preparation_time_in_minutes(3))

def elapsed_time_in_minutes(layers, time):
    """Calculate time elapsed.

    :param layers: func - preparation_time_in minutes.
    :param time: int - time elapsed.

    This function calculates how much time has elapsed in minutes.
    """

    return preparation_time_in_minutes(layers) + time

print(elapsed_time_in_minutes(3, 50))
'''

# Exercise 3 Ghost Gobble Arcade Game

"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """

    return power_pellet_active and touching_ghost



def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """

    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """

    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

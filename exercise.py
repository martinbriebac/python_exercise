
# Exercise 1
# Create a new file named exercise.py
# Print "Hello World!"  


# print('Hello World!')


# Exercise 2 Guido's Gorgeous Lasagna

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
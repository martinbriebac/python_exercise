
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

'''
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

'''

# Exercise 4 Currency Exchange

"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



# def exchange_money(budget, exchange_rate):
#     """

#     :param budget: float - amount of money you are planning to exchange.
#     :param exchange_rate: float - unit value of the foreign currency.
#     :return: float - exchanged value of the foreign currency you can receive.
#     """

#     return budget / exchange_rate


# def get_change(budget, exchanging_value):
#     """

#     :param budget: float - amount of money you own.
#     :param exchanging_value: float - amount of your money you want to exchange now.
#     :return: float - amount left of your starting currency after exchanging.
#     """

#     return budget - exchanging_value


# def get_value_of_bills(denomination, number_of_bills):
#     """

#     :param denomination: int - the value of a bill.
#     :param number_of_bills: int - total number of bills.
#     :return: int - calculated value of the bills.
#     """

#     return denomination * number_of_bills


# def get_number_of_bills(amount, denomination):
#     """

#     :param amount: float - the total starting value.
#     :param denomination: int - the value of a single bill.
#     :return: int - number of bills that can be obtained from the amount.
#     """

#     return amount // denomination


# def get_leftover_of_bills(amount, denomination):
#     """

#     :param amount: float - the total starting value.
#     :param denomination: int - the value of a single bill.
#     :return: float - the amount that is "leftover", given the current denomination.
#     """

#     return amount % denomination


# def exchangeable_value(budget, exchange_rate, spread, denomination):
#     """

#     :param budget: float - the amount of your money you are planning to exchange.
#     :param exchange_rate: float - the unit value of the foreign currency.
#     :param spread: int - percentage that is taken as an exchange fee.
#     :param denomination: int - the value of a single bill.
#     :return: int - maximum value you can get.
#     """

#     spread_percentage = spread /100 * exchange_rate
#     new_rate = spread_percentage + exchange_rate
#     max_currency = budget / new_rate
#     number_of_bills = max_currency // denomination
#     max_value = int(number_of_bills) * denomination
    
#     return max_value


# Exercise 5 Little Sister's Essay

"""Functions to help edit essay homework using string manipulation."""


# def capitalize_title(title):
#     """Convert the first letter of each word in the title to uppercase if needed.

#     :param title: str - title string that needs title casing.
#     :return: str - title string in title case (first letters capitalized).
#     """

#     return title.title()

# capitalize_title('a clash of KINGS')
# print(capitalize_title('a clash of KINGS'))

# def check_sentence_ending(sentence):
#     """Check the ending of the sentence to verify that a period is present.

#     :param sentence: str - a sentence to check.
#     :return: bool - return True if punctuated correctly with period, False otherwise.
#     """

#     return sentence.endswith('.')


# def clean_up_spacing(sentence):
#     """Verify that there isn't any whitespace at the start and end of the sentence.

#     :param sentence: str - a sentence to clean of leading and trailing space characters.
#     :return: str - a sentence that has been cleaned of leading and trailing space characters.
#     """

#     return sentence.strip()


# def replace_word_choice(sentence, old_word, new_word):
#     """Replace a word in the provided sentence with a new one.

#     :param sentence: str - a sentence to replace words in.
#     :param old_word: str - word to replace.
#     :param new_word: str - replacement word.
#     :return: str - input sentence with new words in place of old words.
#     """

#     return sentence.replace(old_word, new_word)

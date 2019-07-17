import sys
import random
"""Let's figure out what to eat."""
"""Need to figure out web scraping to use yelp searches."""


def gameStart():
    """Start the game."""
    while True:
        intro_msg = '\nSo you don\'t want to cook the food at home. Is that correct?'
        intro_msg += '\nEnter y/n: '
        intro_q = input(intro_msg)
        if intro_q == 'n':
            sys.exit()
        elif intro_q == 'y':
            print('\n')
            break
        else:
            print('Invalid answer, try again.')
            continue


gameStart()

old_walking = [
            'Pacheco\'s', 'Michin Dak', 'Boo\'s', 'Pho24', 'Ktown Pho',
            'My Thai', 'Gogobop', 'Bulgogi Hut', 'Guelaguetza',
            'Kang Ho-Dong Baekjeong', 'Myung In Dumplings'
            ]
new_walking = [
            'La Ddong Go', 'Beverly Soon Tofu House', 'Slurpin Ramen',
            'BCD', 'Wako Donksu', 'Tokyo Hamburg'
            ]
delivery_options = {
            'Domino\'s': 'Pizza and Wings', 'Prime Pizza': 'Grandma',
            'My Thai': 'Chicken Curry and Orang e Chicken',
            }


def oldWalkingOptions():
    """Provide old walking options with random import."""
    wo_msg = '\nWalk to: '
    print(wo_msg)
    walking_selection = random.choice(old_walking)
    print(walking_selection)


def newWalkingOptions():
    """Provide new walking options with random import."""
    wo_msg = '\nWalk to: '
    print(wo_msg)
    walking_selection = random.choice(new_walking)
    print(walking_selection + '\n')
    # Need to figure out how to pop this into a new list.


def deliveryOptions():
    """Provide delivery options with dict."""
    food, order = random.choice(list(delivery_options.items()))
    print('\nOrder from ' + food + ' and get ' + order + '.\n')
    print('Don\'t think, just order it, you\'re wasting time.')


# Decide whether to go or deliver.
while True:
    god_msg = 'Do you feel like walking or too high/tired and need delivery? '
    god_msg += '\nEnter "walk" or "too high" or "tired": '
    god_q = input(god_msg)
    if god_q == 'walk':
        new_or_old_msg = '\nDo you want to try something new or same old? '
        new_or_old_msg += '\nEnter "new" or "old": '
        new_or_old_q = input(new_or_old_msg)
        if new_or_old_q == 'new':
            newWalkingOptions()
            break
        elif new_or_old_q == 'old':
            oldWalkingOptions()
            break
    elif god_q == 'too high' or god_q == 'tired':
        deliveryOptions()
        break

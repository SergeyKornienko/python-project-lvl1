"""introduction."""

import prompt

"""intro function"""


def welcome_user():

    name = prompt.string('May I have your name? ')

    print('Hello, {}!'.format(name))

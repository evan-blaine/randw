import random
from os.path import abspath, join, dirname

__title__ = 'randw'
__license__ = 'MIT'
__author__ = 'Evan Adams'
__version__ = '0.0.3'

path = lambda fname: abspath(join(dirname(__file__), fname))

F = {
    'adj': path('data/adjectives.txt'),
    'noun': path('data/nouns.txt'),
}

def get_words(fname) -> str:
    line = random.choice(open(fname).readlines())
    return line.strip()

def adj():
    """
    PARAMS:
    NONE
    """
    return get_words(F['adj'])

def noun():
    """
    PARAMS:
    NONE
    """
    return get_words(F['noun'])

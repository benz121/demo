import sys
import random
#import mechanize
#import cookielib
import time
import random

SOURCE_FILE='useragents.txt'

def get():
    f = open(SOURCE_FILE)
    agents = f.readlines()
    g=random.choice(agents)
    return g
    print(g)
"""
def getAll():
    f = open(SOURCE_FILE)
    agents = f.readlines()
    return [a.strip() for a in agents]
"""
get()

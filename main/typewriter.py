#Necesary modules for it no to shit itself
import time
import sys
def typeffect(sentence, type_delay):
    #Pretty much, using sys, makes as if someone were writing anything you tell it to print. Really cool...
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

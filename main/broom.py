import os

def sweep():
    # Variable command depending on your OS, not a big deal.
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

#This function clears the terminal to leave space for some new text to appear on screen. 
        
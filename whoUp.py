import subprocess
import random
import time
from pyfiglet import figlet_format


# A fun way to pick who will present thier solutions to the class instead of having to random pick yourself.
def whoUpDawg():
    names = [
        'Andrea', 'Xiao', 'Daramy', 'Garuz', 'Stilwell', 'Niko', 'Sung',
        'Daniel', 'Rainer', 'Rashaan'
    ]
    who = f'figlet -w 120 -f cybermedium "{names[random.randrange(10)]}"'
    clear = subprocess.call('clear', shell=True)
    sendIt = subprocess.call(who, shell=True)


whoUpDawg()

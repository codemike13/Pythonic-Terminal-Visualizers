import subprocess
import sys
import time
from termcolor import colored

#A terminal visual that demos the scanning process of a for loop looking for a substring in a supplied string


def finder(strng, substring):
    summ = 0

    for i in range(len(strng)):
        if i + 1 < len(strng):
            if strng[i:i + len(substring)] == substring:
                summ += 1
                print(f'Found {colored(summ,"green")} matches')
                print(strng[0:i] +
                      colored(strng[i:i + len(substring)], "green") +
                      strng[i + len(substring):])
                print(" " * i + substring)
                time.sleep(.5)
                clear = subprocess.call('clear', shell=True)
            else:
                print(f'Found {colored(summ,"green")} matches')
                print(strng)
                print(" " * i + substring)
                time.sleep(.2)
                clear = subprocess.call('clear', shell=True)
    time.sleep(3)


finder('hellohelloelellhelllllllelloooellottttell', 'ell')
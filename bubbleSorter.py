import subprocess
import time
from termcolor import colored
import random

# First in terminal, run commmand ---> pip install termcolor
# -This library allows the terminal to display colored text.
#
# To use bubble show:
# randNum ---> Enter the amount of random numbers you want generated , they will be read into a list then, randomized by the random.shuffle() method
# speed   ---> Enter in seconds , miliseconds or nanoseconds the speed of the visualizer loop.


def bubbleShow(randNum, speed):
    lst = []
    temp = 0
    sort_Progress = ''  # Used to playback progress as nums being sorted.
    unsorted_Lst = ''  # A copy of the original unsorted list.
    outter = 0  # A copy of the 'i' in outter loop + 1 for cleaner code read

    # This loop fills a list with the amount of numbers you want to sort
    for i in range(randNum):
        lst.append(str(i))

    # The list is then randomized using the .shuffle(list,string,tuple) method from class random.
    random.shuffle(lst)

    # The newly shuffled copied into a holder list for playback later.
    for i in lst:
        unsorted_Lst += str(i) + ' '

    # Here we have two loops an inner and outter loop:
    #
    # - Otter loop will run as many times as there is numbers to sort -0r- until they are sorted,
    #   some list finish faster if randomness of numbers isnt as "random" :-) .
    #
    #   -The InneR loop begins to swap the numbers in a "Am I bigger than number to right of me?" manner.
    #
    #       - If I am lets swap spots.
    #
    #                 -But-
    #
    #       - If next number is Bigger
    #           - Last big number stays in spot
    #           - New Bigger number begins asking the question "Am I bigger"
    #
    #                 (-InneR loop END-)
    #
    #           - Once InneR loop ends
    #
    #    -(OutteR loop starts new iteration until the "Am I bigger then next" ? no longer applies)-
    #
    #  Return result of sort.

    for i in range(len(lst)):
        if i + 1 < len(lst):
            for j in range(len(lst)):
                if j + 1 < len(lst):
                    if int(lst[j]) > int(lst[j + 1]):
                        temp = lst[j]
                        lst[j] = lst[j + 1]
                        lst[j + 1] = temp
                        for k in lst:
                            if lst.index(k) == j + 1:
                                sort_Progress += colored(k, 'green') + ' '
                            else:
                                sort_Progress += k + ' '
                        temp = sort_Progress
                        outter = i + 1
                        print(
                            f'{randNum} psuedo random intergers were generated, and cast into a bubble sorter below:\n'
                        )
                        print(
                            f'{colored("Outter Loop","green")}:\t\t {i} \n\t{colored("Inner Loop","yellow")}:\t {j}\n\nSort progress: {sort_Progress}'
                        )

                        sort_Progress = ''
                        time.sleep(speed)
                        clear = subprocess.call('clear', shell=True)
    return f'Sort completed in {colored(outter,"green")} loops.\n\nThis is the unsorted list: \n\n{colored(str(unsorted_Lst),"red")}\n\nHere is the result of the sort:\n\n{str(temp)}'


# Example
print(bubbleShow(10, .8))

# let combinedArray = false;
#     let t0 = performance.now();
#
#     while (!combinedArray) {
#         for (let i = 0; i < array.length; i++) {
#             combinedArray = true
#             current_number = array[i]
#             next_number = array[i + 1]
#             if (current_number > next_number) {
#                 combinedArray = false
#                 // current number is bigger
#                 // so current number needs to be in the index of next_number
#                 array[i + 1] = current_number
#                 array[i] = next_number
#             }
#         }
#     }
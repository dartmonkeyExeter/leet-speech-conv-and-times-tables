# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

my_list = [3, 6, 7, 4, 8, 9, 10, 5, 2, 1]


def bubble_sort(my_list):
    length = len(my_list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(length-1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
        length -= 1  # Reduce the range of iterations in subsequent passes
        if not swapped:  # Early termination if no swaps were made
            break
    print(my_list)


def is_sorted(my_list):
    for i in range(len(my_list)):
        if my_list[i] < my_list[i-1]:
            return False
    return True


def bogo_sort(my_list):
    while not is_sorted(my_list):
        random.shuffle(my_list)
    return my_list

def main():
    bubble_sort(my_list)
    bogo_sort(my_list)

if __name__ == '__main__':
    main()



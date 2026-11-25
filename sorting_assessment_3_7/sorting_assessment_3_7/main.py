"""
Assessment 3.7: Sorting Algorithms
Name   : Linus Kerk Eubil M. Siarot
Method : Insertion Sort
"""

FULL_NAME = "Linus Kerk Eubil M. Siarot"


def build_unsorted_array(full_name):
    """Keep letters only (symbols/spaces excluded), discard duplicate
    letters, and keep the original order of first appearance."""
    unsorted = []
    for ch in full_name.lower():
        if not ch.isalpha():      # exclude symbols (".") and spaces
            continue
        if ch in unsorted:        # discard duplicate letters
            continue
        unsorted.append(ch)
    return unsorted


def insertion_sort(arr):
    """Sort a list ascending (A to Z) using Insertion Sort.
    Returns a NEW list so the unsorted array stays untouched."""
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]   # shift larger element right
            j -= 1
        result[j + 1] = key             # insert key in its position
    return result


def main():
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = insertion_sort(unsorted_array)

    print("Full Name      :", FULL_NAME)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)


if __name__ == "__main__":
    main()

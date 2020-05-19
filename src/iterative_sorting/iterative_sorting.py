def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i

        while j > 0 and current < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # loop through all items that come after the current index
        for j in range(cur_index + 1, len(arr)):
            # Find the item with the smallest value
            if arr[j] < arr[smallest_index]:
                # replace the smallest index
                smallest_index = j
        # Swap the item that is located in the current index with the smallest
        # item that we located during our loop
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     swapped = True
#     last_num = len(arr) - 1
#     while last_num > 0 and swapped:
#         swapped = False
#         for i in range(last_num):
#             if arr[i] > arr[i + 1]:
#                 swapped = True
#                 temp = arr[i]
#                 arr[i] = arr[i + 1]
#                 arr[i + 1] = temp
#         last_num = last_num - 1

#     return arr


# def bubble_sort(arr):
#     for passnum in range(len(arr) - 1, 0, -1):
#         for i in range(passnum):
#             if arr[i] > arr[i + 1]:
#                 temp = arr[i]
#                 arr[i] = arr[i + 1]
#                 arr[i + 1] = temp
#     return arr

def bubble_sort(arr):
    # We want to stop passing through the list
    # as soon as we pass through without swapping any elements
    swapped = True
    # largest elements in an iteration end up at the end of the array
    # the first time we pass through, the position n is the largest element
    # the second time, n - 1 is the second largest element etc etc
    # so with each iteration, we can look at one less element than before
    num_of_iterations = 0
    while swapped:
        swapped = False
        for i in range(len(arr) - num_of_iterations - 1):
            if arr[i] > arr[i + 1]:
                # Swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        num_of_iterations += 1
    return arr
# STRETCH: implement the Count Sort function below
# requires us to know the max value that we will be sorting
# The max argument is so we can specify the max value
# Total range of data we are sorting sits between 0 and maximum value


def count_sort(arr, maximum=-1):
    if len(arr) == 0:  # O(1)
        return arr  # O(1)
    # if max value is not specified, we will take the max vale from the input array
    if maximum == -1:  # O(1)
        maximum = max(arr)  # O(n)
    # make a bunch of buckets
    buckets = [0 for _ in range(maximum + 1)]  # O(max)

    for x in arr:  # O(n)
        if x < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        buckets[x] += 1  # O(1)
    # we have the counts of every value in our input array
    # loop through our buckets, starting at the smallest index
    j = 0
    # This loop is reversing the tallying we did in the previous loop
    for i in range(len(buckets)):  # O(n)
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1
    return arr

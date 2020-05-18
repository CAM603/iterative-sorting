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
    swapped = True
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


def count_sort(arr, maximum=-1):
    # Your code here

    return arr

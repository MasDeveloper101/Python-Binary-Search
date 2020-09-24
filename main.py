main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_item = 8


def binarySearch(list_, search_item):
    low_index = 0
    high_index = len(list_) - 1

    while True:

        mid_index = int((low_index + high_index) / 2)
        print("The mid index is " + str(mid_index))

        if search_item < list_[mid_index]:
            high_index = mid_index - 1

        elif search_item > list_[mid_index]:
            low_index = mid_index + 1

        else:
            return list_[mid_index]
            break


print(binarySearch(main_list, search_item))

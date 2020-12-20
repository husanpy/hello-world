def selection_sort(unsorted_list, rev=False):
    """Currently works only for numbers and letters"""
    if rev:
        for i in range(len(unsorted_list) - 1):
            for j in range(i + 1, len(unsorted_list)):
                if unsorted_list[i] < unsorted_list[j]:
                    tmp_var = unsorted_list[i]
                    unsorted_list[i] = unsorted_list[j]
                    unsorted_list[j] = tmp_var
        sorted_list = unsorted_list
    else:
        for i in range(len(unsorted_list) - 1):
            for j in range(i + 1, len(unsorted_list)):
                if unsorted_list[i] > unsorted_list[j]:
                    tmp_var = unsorted_list[i]
                    unsorted_list[i] = unsorted_list[j]
                    unsorted_list[j] = tmp_var
        sorted_list = unsorted_list
    return sorted_list

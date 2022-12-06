def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    else:
        max_val = 0
        for val in int_list:
            if val > max_val:
                max_val = val
        return max_val


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    if len(int_list) == 1:
        return int_list
    return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    if low > high:
        return None
    elif len(int_list) == 0:
        return None
    elif len(int_list) == 1:
        if int_list[0] == target:
            return 0
        else:
            return None
    else:
        midpoint = (low + high) // 2
        if target == int_list[midpoint]:
            return midpoint
        elif target > int_list[midpoint]:
            return bin_search(target, midpoint + 1, high, int_list)
        else:
            return bin_search(target, low, midpoint - 1, int_list)


# Signature: Maybe_List -> None
# Purpose: Reverse the original input list
def reverse_list_mutate(int_list):
    '''Reverses a list, mutates the input list, returns None
   If list is None, raises ValueError'''
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    if len(int_list) == 1:
        return int_list
    num = len(int_list) - 1
    if len(int_list) > 1:
        for i in range(len(int_list)):
            int_list.append(int_list[num])
            num -= 1
        for j in range(len(int_list) // 2):
            int_list.pop(0)

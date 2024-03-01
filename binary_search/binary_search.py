

def binary_search(list: List(),item:int)->int:
    """
    This function performs a binary search on a sorted input array.

    Parameters:
    input_array (list): A sorted list of integers.
    value (int): The value to search for in the input array.

    Returns:
    int: The index of the value in the array if found, otherwise -1.
    """
    
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__=="__main__":
    my_list = [1,3,5,7,9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
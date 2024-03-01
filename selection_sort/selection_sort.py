

def findSmallest(arr: list)->int:
    """
    This function finds the smallest element in an array and returns its index.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The index of the smallest element in the array.
    """
    
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index=i
    return smallest_index

def selectionSort(arr:list)->list:  
    """
    This function sorts an array using the selection sort algorithm.

    Parameters:
    arr (list): A list of integers to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """
    
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__=="__main__":
    print(selectionSort([5,3,6,2,10]))
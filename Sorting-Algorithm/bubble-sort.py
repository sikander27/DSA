# Bubble sort in Python
# Time Complexity	 
# Best	O(n)
# Worst	O(n2)
# Average	O(n2)
# Space Complexity	O(1)
# Stability	Yes

def bubbleSort(array,types = ["Asc","Desc"]):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    swapped = False
    for j in range(0, len(array) - i - 1):
      # compare two adjacent elements
      # change > to < to sort in descending order 
            ?????
            ?????
            ????
            
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True

    # If array is not swapped, it means it's already sorted
    if not swapped:
        break

data = [-2, 45, 0, 11, -9]

bubbleSort(data)


print('Sorted Array in Ascending Order:')
print(data)

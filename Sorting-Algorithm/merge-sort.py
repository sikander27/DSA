# Time Complexity	 
# Best	O(n*log n)
# Worst	O(n*log n)
# Average	O(n*log n)
# Space Complexity	O(n)
# Stability	Yes

def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while(i < len(L) and j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


    
array = [6, 5, 12, 10, 9, 1]
mergeSort(array)
print(array)


    
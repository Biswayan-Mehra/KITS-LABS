
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0 # left arr
        j = 0 # right arr
        k = 0 # merged arr
        while(i< len(left_arr) and j<len(right_arr)):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1  


def radix_sort(a):
    num = 0
#---------------------------------------------------------------------------------------
    # finding the largest value
    max = a[0]
    for x in a:
        if x>max:
            max=x   # now the largest value is set at max
#---------------------------------------------------------------------------------------
    # now we need to find the number of digits in the max value
    while (max>0):
        num +=1
        max = max/10  # by doing thing we can find the number of digits in max
#---------------------------------------------------------------------------------------
    # now we need to make B a 3d array with 10 sub sections
    for x in range(0,num):
        B = [[] for _ in range(10)]
        for number in a:            # for every number in a
            temp = number//10**(x)%10      # short cut to get the last second last and soo on at evey itration
            B[temp].append(number)         # add the number to the correct slot
        # take all the values from b and keep in a
        i=0
        for x in range(0,10):
            for j in range(len(B[x])):
                a[i] = B[x][j]
                i+=1 
#---------------------------------------------------------------------------------------

def quick_sort(arr,left,right):
    if left<right:
        partison_pos = partison(arr,left,right)
        quick_sort(arr,left,partison_pos-1)
        quick_sort(arr,partison_pos+1,right)
def partison(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

'''
# MERGE SORT
print("Real array: "+str(array_1))
merge_sort(array_1)
print("sortted with merge: "+str(array_1))
'''

'''
# RADIX SORT
print("Real array: "+str(array_1))
radix_sort(array_1)
print("sorted with radix: "+str(array_1))
'''

'''
# QUICK SORT
print("Real array: "+str(array_1))
quick_sort(array_1,0,len(array_1)-1)
print("sorted with Quick Sort: "+str(array_1))
'''
array_1 = [45,112,232,31,53,731,121,22,42]
# Paste which ever sort u want to do

print("Real array: "+str(array_1))
quick_sort(array_1,0,len(array_1)-1)
print("sorted with Quick Sort: "+str(array_1))

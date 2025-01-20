def naive_search(l,n):
    for i in range(len(l)):
        if l[i] == n:
            return i
    return -1


def binary_search(l, n, low_index = None, high_index = None):
    if high_index == None:
        high_index = len(l) - 1
    
    if low_index == None:
        low_index = 0

    if low_index > high_index:
        return -1
    
    mid_point = (low_index + high_index)//2
    if l[mid_point] == n:
        return mid_point
        
    elif n > l[mid_point]:
        return binary_search(l,n,mid_point + 1, high_index) 
    else:
        return binary_search(l,n,low_index, mid_point -1) 

l = [1,2,34,56,7,8,9,0,11,12,13]
n = (9)
print(binary_search(l, n))
print(naive_search(l, n))
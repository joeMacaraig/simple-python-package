def median (arr): 
    arr.sort()
    if len(arr) % 2 == 0: 
        mid  = len(arr)//2
        return ((arr[mid] + arr[mid - 1]) / 2)
    else: 
        return arr[len(arr)//2]

def mean(arr): 
    sum = 0
    for i in arr: 
        sum += i
    return sum / len(arr)
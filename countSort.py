def countingSort(arr):
    # Write your code here
    count = [0]*100
    
    for num in arr:
        count[num]+=1
        
    return count

print(countingSort([1,1,3,2,1]))
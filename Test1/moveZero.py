def q(nums):
    n = len(nums)
    c = 0
    for i in range(n):
        if nums[i] != 0:
            nums[c] = nums[i]
            c +=1
    while c<n:
        nums[c] = 0
        c +=1
        
    
        
        
        
nums = [0,1,0,3,12]
q(nums)
print(nums)
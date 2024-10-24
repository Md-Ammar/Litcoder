def max_alternating_sum(nums):
    even_sum = 0  
    odd_sum = 0   

    for num in nums:
        
        new_even_sum = max(even_sum, odd_sum + num)
        new_odd_sum = max(odd_sum, even_sum - num)

        
        even_sum, odd_sum = new_even_sum, new_odd_sum

    
    return even_sum

nums = [4, 2, 5, 3]
print(max_alternating_sum(nums))
# Problem
# Given an array of integers (positive and negative) find the largest continuous sum. 
  
  # TEST:
  large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
  # Start: 1
  # End: 10
  # 29
  
  
  # ==========================================================================
  #Default Answer:
  def large_cont_sum1(arr): 
    
    current_sum = max_sum = arr[0]
    
    for i in arr[1:]:
        
        current_sum = max(current_sum+i, i)
        max_sum = max(current_sum, max_sum)
        
    return max_sum

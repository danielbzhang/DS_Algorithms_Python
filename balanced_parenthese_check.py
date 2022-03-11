def balance_check(s):
    
    open_list = ["(", "[", "{"]
    close_list = [")", "]", "}"]
    
    stack = []
    
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            position = close_list.index(i)
            if ((len(stack) > 0) and (open_list[position] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
            
    if len(stack) == 0:
        return True
    return False
  
  # ================================================================================
  
  def balance_check1(s):
    
    opening = set('([{')
    matching = set([('(',')'), ('[',']'), ('{','}')])
    
    stack = []
    
    if len(stack)%2 != 0:
        return False
    
    for i in s:
        if i in opening:
            stack.append(i)
        else:
            last = stack.pop()
            if (last, i) not in matching:
                return False
            
    return len(stack) == 0
  
  # TEST:
  balance_check1('[]')
  balance_check1('[](){([[[]]])}')
  balance_check1('()(){]}')

def compress(s):
    
    count = {}
    i = 0
    
    while i<len(s):
        if s[i] not in count:
            count[s[i]] = 1
        else:
            count[s[i]] += 1
        i += 1
    result = [k+str(v) for k, v in count.items()]
    return ''.join(result)
  
  # TEST:
  compress('AAAABBBBCCCCddaaaE')
  # 'A4B4C4d2a3E1'
  
  # ================================================================================
  def compress1(s):
    
    r = ''
    l = len(s)
    count = 1
    
    if l == 0:
        return ''
    elif l == 1:
        return s+str(1)
    
    start = s[0]
    i = 1
    
    while i<l:
        if s[i] == s[i-1]:
            count += 1
        else:
            r += s[i-1]+str(count)
            count = 1
            
        i += 1
        
    r += s[i-1]+str(count)
        
    return r

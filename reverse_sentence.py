
def rev_sentence(s):
  
  length = len(s)
  words = []
  space = [' ']
  
  i = 0
  while i<length:
    if s[i] not in space:
      start = i
      
      while i<length and s[i] not in space:
        i += 1
        
      words.append(start:i)
      
    i += 1
    
  return ' '.join(reversed(words))

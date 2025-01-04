def is_balanced(string : str)-> bool:
  stack = []
  mapping = {')':'(', '}':'{', ']' : '['}
  for ch in string:
    if ch in mapping:
      top = stack.pop() if stack else "#"
      if mapping[ch] != top:
        return False
    else:
      stack.append(ch)
  return not stack


print(is_balanced("(){}[]"))
print(is_balanced("(){}[]]"))

      
        
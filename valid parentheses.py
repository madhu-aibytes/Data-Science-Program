'''def valid_parentheses(s):
    changed = True
    while changed:
        changed = False
        if "()" in s:
            s = s.replace("()", "")
            changed = True
        if "{}" in s:
            s = s.replace("{}", "")
            changed = True
        if "[]" in s:
            s = s.replace("[]", "")
            changed = True
    if s == "":
        return True
    else:
        return False
s = input("Enter parentheses string: ")

if valid_parentheses(s):
    print("Valid")
else:
    print("Not valid")'''
    
    
    
    
def valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():  # if it's an opening bracket
            stack.append(char)
        elif char in mapping.keys():   # if it's a closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
s = input("Enter parentheses string: ")
if valid_parentheses(s):
    print("Valid")
else:
    print("Not valid")
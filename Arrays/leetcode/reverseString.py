"""
create a function that reverses a string 
"""

def str_reverse(s):
    if not isinstance(s, str):
        return "Type Mismtach"
    str_rev = ""
    for index in range(len(s)-1, -1, -1):
        str_rev += s[index]
    return str_rev

def str_reverse_v2(s):
    if not isinstance(s, str):
        return "Type Mismatch"
    return s[::-1]

print(str_reverse("234"))
print(str_reverse_v2(123)) 
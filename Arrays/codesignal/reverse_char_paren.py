"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";

"""

def solution(inputString):
    
    # split the string into those with brackets and those without brackets
    # better approach is to use a stack
        # keep adding elements to the result list until a '(' is encountered
        # and then add elements to stack until a ')' is encountered
        # append the stack content to the result and then empty stack
        # repeat
    
    stack = []
    result = []
    
    for c in inputString:
        if c != ')':
            result.append(c)
            if c == '(':
                stack.append(c) 


    print(f"stack: {stack}\nresult: {result}")

solution("foo(bar)baz(blim)")
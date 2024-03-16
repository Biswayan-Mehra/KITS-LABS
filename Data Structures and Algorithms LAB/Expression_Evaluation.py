# a/b+c*d
infix = input("Infix Expression: ")
postfix = ''
stack = []
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
for x in infix:
    if x.isalnum():
        postfix += x
    elif x == '(':
        stack.append('(')
    elif x == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != '(' and priority[x] <= priority[stack[-1]]:
            postfix += stack.pop()
        stack.append(x)
while stack:
    postfix += stack.pop()
print("Postfix Expression: "+postfix)

stack = []
expression = []
expression[:0] = postfix

for i in range(len(expression)):
    if expression[i].isalpha():
        print(f"Value of {expression[i]}:", end=" ")
        expression[i] = input()

for i in expression:
    if i not in priority:
        stack.append(i)
    else:
        x = int(stack.pop())
        y = int(stack.pop())
        if i == '+':
            value = y+x
        elif i == '-':
            value = y-x
        elif i == '*':
            value = y*x
        elif i == '/':
            value = y/x
        elif i == '^':
            value = y**x
        stack.append(value)
print(''.join(map(str, stack)))

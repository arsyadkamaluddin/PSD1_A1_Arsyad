class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.items:
            return self.items.pop()
    def peek(self):
        if self.size():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def dis(self):
        return self.items
def urutan(operator):
    match operator:
        case "+":
            return 1
        case "-":
            return 1
        case "*":
            return 2
        case "/":
            return 2
        case __ :
            return 0
def infixToPostfix(infix):
    output = ""
    infix = infix.split()
    stack = Stack()

    for char in infix:
        if char.isalnum():  # Operand
            output += char
        else:
            if urutan(char)>urutan(stack.peek()) or stack.size()==0 or char=="(":
                stack.push(char)
            elif char==")":
                while stack.peek()!="(":
                    output += stack.pop()
                stack.pop()
            else:
                output += stack.pop()
                stack.push(char)

    while stack.size():
        output += stack.pop()

    return output
    
nilai = "4 * ( 5 * 6 + 5 ) - 7"
print(f"Infix -> %s",nilai)
print(f"Postfix -> %s",infixToPostfix(nilai))
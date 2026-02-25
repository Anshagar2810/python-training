class Node:
    def __init__(self, data= None):
        self.value = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def isEmpty(ansh):
        return (ansh.top == None)
    def size(ansh):
        return ansh.length
    

    def push(ansh, data):
        temp = Node(data)
        temp.next = ansh.top
        ansh.top = temp

    def pop(ansh):
        if ansh.isEmpty():
            return "stack is empty"
        temp = ansh.top
        ansh.top = ansh.top.next
        return temp.value

    def peek(ansh):
        if ansh.isEmpty():
            return "stack is empty"
        return ansh.top.value
    

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
while (not s1.isEmpty()): 
    print(s1.pop(), end=" ")
print()
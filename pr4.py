l=[]
print("Enter 1. for Push")
print("Enter 2. for Pop")
print("Enter 3. for Exit")
size=int(input("Enter size of stack: "))
while True:
    c=int(input("Enter your choice: "))
    if c==1:
        if size==len(l):
             print("Stack Overflow")
        else:
            elm=int(input("Enter an element into the stack:"))
            l.append(elm)
            print(l)
    elif c==2:
        if len(l)==0:
            print("Stack is empty")
        else:
            l.pop()
            print(l)
    elif c==3:
        print("Exit from stack")
    break

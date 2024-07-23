class Stack:
    def __init__(self):
        self.items=[]
        self.top=-1
    def push(self,data):
        self.items.append(data)
        self.top+=1
    def pop(self):
        self.top-=1
        self.items.pop()
    def isEmpty(self):
        return self.top==-1
    def peek(self):
        if not self.isEmpty():
            return self.items[self.top]
    def display(self):
        return self.items
st=Stack()
operators=['+','-','*','/']
list1=[x for x in input()]
print(list1)
for i in list1:
    if i not in operators:
        st.push(int(i))
    else:
        temp1=st.peek()
        st.pop()
        temp2=st.peek()
        st.pop()
        if i=='+':
            result=temp2+temp1
        elif i=='-':
            result=temp2-temp1
        elif i=='*':
            result=temp2*temp1
        elif i=='/':
            result=temp2/temp1
        st.push(result)
result=st.display()
print(*result)

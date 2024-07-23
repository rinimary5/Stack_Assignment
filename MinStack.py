class MinStack:
    def __init__(self):
        self.items=[]
        self.top1=-1

    def push(self,data):
        self.items.append(data)
        self.top1+=1


    def pop(self):
        self.items.pop()
        self.top1-=1
    def top(self):
        if self.top1!=-1:
            return self.items[self.top1]
    def getMin(self):
        print(self.top1)
        mini=self.items[0]
        size=self.top1
        while(size>-1):
            if self.items[size]<mini:
                mini=self.items[size]
            size=size-1
        return mini
mst=MinStack()
mst.push(-2)
mst.push(0)
mst.push(-1)
print(mst.getMin())
mst.pop()
print(mst.top())

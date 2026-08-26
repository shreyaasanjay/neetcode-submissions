class MinStack:

    def __init__(self):
        self.stack = []
        self.mins=[]
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        elif val<self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])
        
    def pop(self) -> None:
        del self.stack[-1]
        del self.mins[-1]
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.mins[-1]

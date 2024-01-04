class MyStack:

    def __init__(self):
        self.data = []
        
    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        tmp = self.data.pop(-1)
        return tmp

    def top(self) -> int:
        return self.data[-1]
        
    def empty(self) -> bool:
        return not self.data

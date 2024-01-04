class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)
        
    def pop(self) -> int:
        tmp = self.data[0]
        self.data = self.data[1:]
        return tmp

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return not self.data

class TextEditor:

    def __init__(self):
        self.leftList = []
        self.rightList = []

    def addText(self, text: str) -> None:
        for char in text:
            self.leftList.append(char)

    def deleteText(self, k: int) -> int:
        counter = 0
        while len(self.leftList) > 0 and counter != k:
            self.leftList.pop()
            counter += 1
        
        return counter

    def cursorLeft(self, k: int) -> str:
        counter = 0
        while len(self.leftList) > 0 and counter != k:
            val = self.leftList.pop()
            self.rightList.append(val)
            counter += 1
        
        idx = min(10, len(self.leftList))

        return "".join(self.leftList[len(self.leftList) - idx:])

    def cursorRight(self, k: int) -> str:
        counter = 0
        while len(self.rightList) > 0 and counter != k:
            val = self.rightList.pop()
            self.leftList.append(val)
            counter += 1
        
        idx = min(10, len(self.leftList))

        return "".join(self.leftList[len(self.leftList) - idx:])
        

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
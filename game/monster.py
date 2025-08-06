class Visitor:

    def __init__(self,name, type, Ans):
        self.type = type
        self.name = name
        self.Ans = Ans

    def get_info(self):
        return f"{self.name} said:  {self.Ans} "
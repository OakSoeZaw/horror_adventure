class Visitor:

    def __init__(self,name, type, Ans,note,introState):
        self.type = type
        self.name = name
        self.Ans = Ans
        self.note = note
        self.introState = introState

    def get_info(self):
        return f"{self.name} said:  {self.Ans} "

    def get_note(self):
        return self.note

    def introduceState(self):
        return self.introState
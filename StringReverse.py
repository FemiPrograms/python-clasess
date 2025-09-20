class word:
    def __init__(self,s='YOUTUBE'):
        self.s = s
    def reverse(self):
        self.s = self.s[::-1]
        return self.s
ok = word()
print(ok.reverse())
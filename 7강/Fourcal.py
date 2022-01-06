class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first ** self.second
        return result

a=MoreFourCal(4,2)
print(a.add())
print(a.pow())
print(a.div())
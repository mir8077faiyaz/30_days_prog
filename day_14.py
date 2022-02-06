class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def __inti__(self,arr):
        self.__elements=arr
    #self.maximumDifference=0
    def computeDifference(self):
        max=0
        min=101
        for i in self.__elements:
            if(i>=max):
                max=i
            if(i<=min):
                min=i
        
        self.maximumDifference=max-min

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
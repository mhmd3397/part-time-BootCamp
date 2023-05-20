'''
This module is for assignment Users with class MathDojo: in Coding Dojo
Mohammed Eleyan
18-05-2023
'''


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!

md1 = MathDojo()
y = md1.add(5, 4, 3, 2, 1).subtract(3, 2, 1).result
print(y)

md2 = MathDojo()
z = md2.add(6, 7, 8, 9).subtract(5, 4, 3, 2, 1).result
print(z)

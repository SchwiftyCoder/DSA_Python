class Recursion:
    def factorial(self, num: int) -> int:
        if num == 0:  # base case
            return 1
        else:
            return num * self.factorial(num - 1)

    def arithmeticSum(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return num + self.arithmeticSum(num - 1)


sol = Recursion()

print(sol.factorial(4))
print(sol.arithmeticSum(4))

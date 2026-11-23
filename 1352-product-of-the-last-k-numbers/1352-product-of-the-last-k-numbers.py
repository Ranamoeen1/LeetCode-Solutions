class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.last_zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = len(self.prefix)
            self.prefix.append(1)
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix) - 1
        start = n - k + 1
        if self.last_zero >= start:
            return 0
        if start == 0:
            return self.prefix[-1]
        return self.prefix[-1] // self.prefix[start - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)



# class ProductOfNumbers:

#     def __init__(self):
#         self.prefix = [1]

#     def add(self, num: int) -> None:
#         if num == 0:
#             self.prefix = [1]
#         else:
#             self.prefix.append(self.prefix[-1] * num)

#     def getProduct(self, k: int) -> int:
#         n = len(self.prefix) - 1
#         if k > n:
#             return 0
#         return self.prefix[-1] // self.prefix[-1 - k]


# # Your ProductOfNumbers object will be instantiated and called as such:
# # obj = ProductOfNumbers()
# # obj.add(num)
# # param_2 = obj.getProduct(k)
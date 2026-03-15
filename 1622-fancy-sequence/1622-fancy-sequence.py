class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.n = 10**5 + 10  # max size
        self.tree = [0] * (4 * self.n)  # values
        self.lazy_mul = [1] * (4 * self.n)  # pending multiply
        self.lazy_add = [0] * (4 * self.n)  # pending add
        self.size = 0  # current sequence length
        
    def _push_down(self, node, left, right):
        """Push lazy tags to children"""
        if self.lazy_mul[node] != 1 or self.lazy_add[node] != 0:
            mid = (left + right) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            
            # Apply to left child
            self.lazy_mul[left_child] = self.lazy_mul[left_child] * self.lazy_mul[node] % self.MOD
            self.lazy_add[left_child] = (self.lazy_add[left_child] * self.lazy_mul[node] + self.lazy_add[node]) % self.MOD
            
            # Apply to right child  
            self.lazy_mul[right_child] = self.lazy_mul[right_child] * self.lazy_mul[node] % self.MOD
            self.lazy_add[right_child] = (self.lazy_add[right_child] * self.lazy_mul[node] + self.lazy_add[node]) % self.MOD
            
            # Reset current node
            self.lazy_mul[node] = 1
            self.lazy_add[node] = 0
    
    def _update_range(self, node, left, right, q_left, q_right, mul_val, add_val):
        """Range update: multiply by mul_val then add add_val"""
        if q_left > right or q_right < left:
            return
        
        if q_left <= left and right <= q_right:
            self.lazy_mul[node] = self.lazy_mul[node] * mul_val % self.MOD
            self.lazy_add[node] = (self.lazy_add[node] * mul_val + add_val) % self.MOD
            return
            
        self._push_down(node, left, right)
        mid = (left + right) // 2
        self._update_range(2*node, left, mid, q_left, q_right, mul_val, add_val)
        self._update_range(2*node+1, mid+1, right, q_left, q_right, mul_val, add_val)
    
    def _query_point(self, node, left, right, idx):
        """Query single point"""
        if left == right:
            # Apply pending operations to get actual value
            return (self.tree[node] * self.lazy_mul[node] + self.lazy_add[node]) % self.MOD
            
        self._push_down(node, left, right)
        mid = (left + right) // 2
        
        if idx <= mid:
            return self._query_point(2*node, left, mid, idx)
        else:
            return self._query_point(2*node+1, mid+1, right, idx)
    
    def _point_update(self, node, left, right, idx, val):
        """Set a single point (for append)"""
        if left == right:
            self.tree[node] = val
            return
            
        self._push_down(node, left, right)
        mid = (left + right) // 2
        
        if idx <= mid:
            self._point_update(2*node, left, mid, idx, val)
        else:
            self._point_update(2*node+1, mid+1, right, idx, val)

    def append(self, val: int) -> None:
        self.size += 1
        # First apply all pending lazy operations to new position
        # Then set the value
        self._point_update(1, 1, self.n, self.size, val)
        
    def addAll(self, inc: int) -> None:
        if self.size > 0:
            self._update_range(1, 1, self.n, 1, self.size, 1, inc)
        
    def multAll(self, m: int) -> None:
        if self.size > 0:
            self._update_range(1, 1, self.n, 1, self.size, m, 0)
        
    def getIndex(self, idx: int) -> int:
        if idx >= self.size:
            return -1
        return self._query_point(1, 1, self.n, idx + 1)  # +1 for 1-based indexing


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)



# class Fancy:

#     def __init__(self):
#         self.MOD = 10**9 + 7
#         self.arr = []  # stores base values
#         self.mul = 1   # current global multiplier
#         self.add = 0   # current global addend
        
#     def append(self, val: int) -> None:
#         # base = (val - add) / mul = (val - add) * inv(mul) mod MOD
#         inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
#         base = (val - self.add) * inv_mul % self.MOD
#         self.arr.append(base)
        
#     def addAll(self, inc: int) -> None:
#         self.add = (self.add + inc) % self.MOD
        
#     def multAll(self, m: int) -> None:
#         self.mul = self.mul * m % self.MOD
#         self.add = self.add * m % self.MOD
        
#     def getIndex(self, idx: int) -> int:
#         if idx >= len(self.arr):
#             return -1
#         return (self.arr[idx] * self.mul + self.add) % self.MOD


# # Your Fancy object will be instantiated and called as such:
# # obj = Fancy()
# # obj.append(val)
# # obj.append(val)
# # obj.addAll(inc)
# # obj.multAll(m)
# # param_4 = obj.getIndex(idx)
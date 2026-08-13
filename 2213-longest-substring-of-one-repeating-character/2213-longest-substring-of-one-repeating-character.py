class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        
        # Segment Tree attributes stored as parallel arrays
        self.max_len = [0] * (4 * self.n)
        self.prefix_len = [0] * (4 * self.n)
        self.suffix_len = [0] * (4 * self.n)
        self.prefix_char = [''] * (4 * self.n)
        self.suffix_char = [''] * (4 * self.n)
        self.size = [0] * (4 * self.n)
        
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _merge(self, node: int, left_child: int, right_child: int):
        self.prefix_char[node] = self.prefix_char[left_child]
        self.suffix_char[node] = self.suffix_char[right_child]
        self.size[node] = self.size[left_child] + self.size[right_child]
        
        # Max length is at least the max of left and right children
        self.max_len[node] = max(self.max_len[left_child], self.max_len[right_child])
        
        # Update prefix length
        self.prefix_len[node] = self.prefix_len[left_child]
        if (self.prefix_len[left_child] == self.size[left_child] and 
                self.suffix_char[left_child] == self.prefix_char[right_child]):
            self.prefix_len[node] += self.prefix_len[right_child]
            
        # Update suffix length
        self.suffix_len[node] = self.suffix_len[right_child]
        if (self.suffix_len[right_child] == self.size[right_child] and 
                self.suffix_char[left_child] == self.prefix_char[right_child]):
            self.suffix_len[node] += self.suffix_len[left_child]
            
        # Update max length considering boundary overlap
        if self.suffix_char[left_child] == self.prefix_char[right_child]:
            self.max_len[node] = max(
                self.max_len[node], 
                self.suffix_len[left_child] + self.prefix_len[right_child]
            )

    def _build(self, node: int, l: int, r: int):
        if l == r:
            ch = self.s[l]
            self.max_len[node] = 1
            self.prefix_len[node] = 1
            self.suffix_len[node] = 1
            self.prefix_char[node] = ch
            self.suffix_char[node] = ch
            self.size[node] = 1
            return
        
        mid = (l + r) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        
        self._build(left_child, l, mid)
        self._build(right_child, mid + 1, r)
        self._merge(node, left_child, right_child)

    def update(self, node: int, l: int, r: int, idx: int, ch: str):
        if l == r:
            self.s[idx] = ch
            self.prefix_char[node] = ch
            self.suffix_char[node] = ch
            return
        
        mid = (l + r) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        
        if idx <= mid:
            self.update(left_child, l, mid, idx, ch)
        else:
            self.update(right_child, mid + 1, r, idx, ch)
            
        self._merge(node, left_child, right_child)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = SegmentTree(s)
        ans = []
        n = len(s)
        
        for ch, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, n - 1, idx, ch)
            # Root node (index 1) always contains global max length
            ans.append(tree.max_len[1])
            
        return ans
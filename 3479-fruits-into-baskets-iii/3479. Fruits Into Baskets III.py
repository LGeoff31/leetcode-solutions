class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        if not fruits or not baskets:
            return -1

        size = len(fruits)
        if size != len(baskets):
            return -2

        tree = [0] * (4 * size)
        self.buildTree(tree, baskets, 0, 0, size - 1)
        count = 0

        for fruit in fruits:
            if not self.placeFruit(tree, 0, 0, size - 1, fruit):
                count += 1

        return count

    def buildTree(self, tree: List[int], baskets: List[int], i: int, low: int, high: int):
        if low == high:
            tree[i] = baskets[low]
            return

        mid = (low + high) >> 1
        left = 2 * i + 1
        right = left + 1

        self.buildTree(tree, baskets, left, low, mid)
        self.buildTree(tree, baskets, right, mid + 1, high)

        tree[i] = max(tree[left], tree[right])

    def placeFruit(self, tree: List[int], i: int, low: int, high: int, value: int) -> bool:
        if tree[i] < value:
            return False

        if low == high:
            tree[i] = 0
            return True

        mid = (low + high) >> 1
        left = (i << 1) + 1
        right = left + 1

        if tree[left] >= value:
            found = self.placeFruit(tree, left, low, mid, value)
        else:
            found = self.placeFruit(tree, right, mid + 1, high, value)

        tree[i] = max(tree[left], tree[right])
        return found
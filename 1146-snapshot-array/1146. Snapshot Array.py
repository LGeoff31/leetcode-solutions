class SnapshotArray:

    def __init__(self, length: int): 
        self.snapshots = [[[0, 0]] for _ in range(length)]
        print(self.snapshots)
        self.number_snapshots = 0

    def set(self, index: int, val: int) -> None:
        self.snapshots[index].append([self.number_snapshots, val])
        
    def snap(self) -> int:
        self.number_snapshots += 1
        return self.number_snapshots - 1
        
    def get(self, index: int, snap_id: int) -> int:
        # Binary search for the right snap_id number, then binary search 
        idx = bisect_right(self.snapshots[index], [snap_id, 1e9])
        return self.snapshots[index][idx - 1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
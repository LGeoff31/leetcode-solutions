class Node:
    def __init__(self, val, name): 
        self.val = val
        self.name = name
        self.children = defaultdict(list) # name: Node

class FileSystem:
    def __init__(self):
        self.parent = Node(0, "")
        
    def createPath(self, path: str, value: int) -> bool:
        lst = path.split("/")[1:]
        curr = self.parent
        for idx, name in enumerate(lst):
            if name in curr.children:
                curr = curr.children[name]
            else:
                if idx != len(lst) - 1: return False
                new_node = Node(value, name)
                curr.children[name] = new_node
        return len(curr.children) > 0

    def get(self, path: str) -> int:
        curr = self.parent
        print(curr)
        lst = path.split("/")[1:]
        for idx, name in enumerate(lst):
            if name in curr.children:
                curr = curr.children[name]
            else:
                return -1
        return curr.val

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
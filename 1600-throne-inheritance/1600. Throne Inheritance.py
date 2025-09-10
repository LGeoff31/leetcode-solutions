class ThroneInheritance:
    def __init__(self, kingName: str):
        self.elder = kingName
        self.parent = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.parent[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def dfs(name):
            if not self.parent[name]:
                if name not in self.dead:
                    order.append(name)
                return
            if name not in self.dead:
                order.append(name)
            for child in self.parent[name]:
                dfs(child)
        dfs(self.elder)
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
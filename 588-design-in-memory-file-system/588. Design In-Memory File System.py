class Node:
    def __init__(self):
        self.content = ""
        self.children = {}

class FileSystem:
    def __init__(self):
        self.parent = Node()

    def ls(self, path: str) -> List[str]:
        curr = self.parent
        directories = path.split("/")
        for d in directories:
            if d == "": continue
            curr = curr.children[d] # We should always have this path, since gave valid path

        if curr.content:
            # If path is file path
            return [d]
        else:
            # If path is directory path
            return sorted(list(curr.children))

    def mkdir(self, path: str) -> None:
        curr = self.parent
        directories = path.split("/") # Learn how to filter array to avoid /
        for d in directories:
            if d == "": continue
            if d not in curr.children:
                curr.children[d] = Node()
            curr = curr.children[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.parent
        directories = filePath.split("/")
        for d in directories:
            if d == "": continue
            if d not in curr.children:
                curr.children[d] = Node()
            curr = curr.children[d]
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.parent
        directories = filePath.split("/")
        for d in directories:
            if d == "": continue
            curr = curr.children[d]
        return curr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
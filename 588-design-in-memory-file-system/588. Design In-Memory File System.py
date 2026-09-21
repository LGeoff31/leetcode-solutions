class FileSystem:
    def __init__(self):
        self.root_directory = {}
        self.content = {} # "/a/b": "Hello"
        
    def ls(self, path: str) -> list[str]:
        curr = self.root_directory
        if path == "/":
            return sorted(curr.keys())

        for directory in path.split("/")[1:]:
            if directory not in curr:
                return []
            curr = curr[directory]
        
        if len(curr) == 0 and path in self.content:
            return [path.split("/")[-1]]
        return sorted(curr.keys())
        
    def mkdir(self, path: str) -> None:
        curr = self.root_directory

        for directory in path.split("/")[1:]:
            if directory not in curr:
                curr[directory] = {}
            curr = curr[directory]


    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root_directory

        for directory in filePath.split("/")[1:]:
            if directory not in curr:
                curr[directory] = {}
            curr = curr[directory]

        if filePath not in self.content:
            self.content[filePath] = content
        else:
            self.content[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.content[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
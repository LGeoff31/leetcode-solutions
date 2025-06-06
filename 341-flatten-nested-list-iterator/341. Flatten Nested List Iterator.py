# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nestedList):
            flatten_lst = []
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    flatten_lst.append(nestedList[i].getInteger())
                else:
                    flatten_lst.extend(flatten(nestedList[i].getList()))
            return flatten_lst
        self.flatten_lst = flatten(nestedList)
        self.idx = 0


    def next(self) -> int:
        self.idx += 1
        return self.flatten_lst[self.idx - 1]
        
    
    def hasNext(self) -> bool:
        return self.idx < len(self.flatten_lst)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
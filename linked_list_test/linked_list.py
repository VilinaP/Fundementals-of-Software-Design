# Linked List
# Prof. O & CPTR-215
# 2025-12-04 first draft

"""A linked list is either
- empty, or
- a node which contains ("has")
    a data item and
    a linked list
"""

from abc import ABC # Abstract Base Class

class LinkedList(ABC):
    def from_list(items: list) -> "LinkedList":
        'Builds a LinkedList from the contents of items.'
        if items == []:
            return EmptyList()
        else: 
            return ListNode(items[0], LinkedList.from_list(items[1:]))


class EmptyList(LinkedList):
    def __repr__(self) -> str:
        return "EmptyList()"
    
    def __str__(self) -> str:
        return "<>"
    
    def comma_str(self) -> str:
        return ""
    
    def __len__(self) -> int:
        return 0
    
    def __getitem__(self, index: int):
        raise IndexError("list index out of range")
    
    def __add__(self, other: LinkedList) -> LinkedList:
        return other
    
    def count_of (self, item, count: int = 0) -> int:
        return count
    
    def index_of(self, item) -> int:
        raise ValueError(f'{item} is not in list')
    
    def replace(self, old, new) -> LinkedList:
        return self
    
    def without(self, item) -> LinkedList:
        raise ValueError(f'{item} is not in list')
    
    def joined_with(self, item) -> str:
        return ''
    
    def joined_help(self, item) -> str:
        return ''
    
    def reversed(self) -> str:
        return EmptyList()\
    
    def insert(self, item) -> LinkedList:
        return ListNode(item, EmptyList())
    
    def sorted(self) -> LinkedList:
        return self
    
    def merge_with(self, other: LinkedList) -> LinkedList:
        return other

class ListNode(LinkedList):
    def __init__(self, data, rest: LinkedList):
        super().__init__()
        self.data = data
        self.rest = rest

    def __repr__(self) -> str:
        return f"ListNode({self.data}, {repr(self.rest)})"
    
    def __str__(self) -> str:
        return f"<{str(self.data)}{self.rest.comma_str()}>"
    
    def comma_str(self) -> str:
        return f", {self.data}{self.rest.comma_str()}"
    
    def __len__(self) -> int:
        return 1 + len(self.rest)
    
    def __getitem__(self, index: int):
        if index == 0:
            return self.data
        else:
            return self.rest[index - 1]
        
    def __add__(self, other: LinkedList) -> LinkedList:
        return ListNode(self.data, self.rest + other)
    
    def count_of(self, item, count: int = 0) -> int:
        if self.data == item:
            count += 1
        return self.rest.count_of(item, count)
    
    def index_of(self, item) -> int:
        
        if item == self.data:
            return 0
        else:
            return 1 + self.rest.index_of(item)
      
    def replace(self, old, new) -> LinkedList:
        if old == new:
            return self
        else:
            if self.data == old:
                return ListNode(new, self.rest.replace(old, new))
                
            else: 
                return ListNode(self.data, self.rest.replace(old, new))
            
    def without(self, item) -> LinkedList:
        if self.data == item:
            return self.rest
        else: 
            return ListNode(self.data, self.rest.without(item))
        
    def joined_with(self, separator: str) -> str:
        return f'{self.data}{self.rest.joined_help(separator)}'
        
    def joined_help(self, separator: str) -> str:
        return f'{separator}{self.data}{self.rest.joined_help(separator)}'

    def reversed(self) -> LinkedList:
        return self.rest.reversed() + ListNode(self.data, EmptyList())
    
    def insert(self, item) -> LinkedList:
        if self.data > item:
            return ListNode(item, ListNode(self.data, self.rest))
        else:
            return ListNode(self.data, EmptyList()) + self.rest.insert(item) 
    
    def sorted(self) -> LinkedList:
        return self.rest.sorted().insert(self.data)
    
    def merge_with(self, other: LinkedList) -> LinkedList:
        my_list = self + other
        return my_list.sorted()
        
if __name__ == "__main__":
    import doctest
    doctest.testfile("linked_list_test.txt")

    empty_list = EmptyList()
    nums1 = ListNode(5, EmptyList())
    list_with_empty = ListNode(EmptyList(), nums1)
    
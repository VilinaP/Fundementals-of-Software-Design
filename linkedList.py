'''A linked list is either 
- empty
- node which contains data item and another (linked) list
'''
from abc import ABC #Abstract base class

class LinkedList(ABC):
    pass

class EmptyList(LinkedList):
    def __init__(self) -> None:
        super().__init__() 

    def __str__(self) -> str:
        return '<>'
    
    def __repr__(self) -> str:
        return "EmptyList()"
    
    def __len__(self) -> int:
        return 0
    
    def __getitem__(self, index: int):
        raise IndexError('list index out of range')
    
    def __add__(self, other: LinkedList):
        return other

class ListNode(LinkedList):
    def __init__(self, data, rest: LinkedList) -> None:
        super().__init__()
        self.data = data
        self.rest = rest

    def __str__(self) -> str:
        return f'<{self.data}, {self.rest.comma_str()}>'
    
    def comma_str(self) -> str:
        return f', {self.data}, {self.rest.comma_str()}'

    def __repr__(self) -> str:
        return f'ListNode({self.data}, {self.rest})' #self.rest keeps running the recursion for __repr__ in the ListNode (polimorphism | type1)

    def __len__(self) -> int:
        return 1 + len(self.rest)
    
    def __getitem__(self, index :int):
        if index == 0:
            return self.data
        else:
            return self.rest[index-1]
        
    def __add__(self, other: LinkedList):
        return ListNode(self.data, self.rest + other)

    
if __name__ == "__main__":
    no_nums = EmptyList()
    nums1 = ListNode(5, EmptyList())
    list_with_empty = ListNode(EmptyList(), nums1)
    


#ListNode(EmptyList(), ListNode(5, EmptyList()))
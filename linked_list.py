# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value=None, next=None):   # 这里我们 root 节点默认都是 None，所以都给了默认值
        self.value = value
        self.next = next

    def __str__(self):
        """方便你打出来调试，复杂的代码可能需要断点调试"""
        return '<Node: value {}, next {}>'.format(self.value, self.next)

class LinkedList(object):
    """ 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """
        :param maxsize: int or None, 如果是 None，无限扩充
        """
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0
        

    def __len__(self):
        return self.length
        

    def append(self, value):    # O(1)
        if self.maxsize is not None and len(self) >=self.maxsize:
            raise Exception ('linked list is full')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length +=1
     
        

    def appendleft(self, value):
        


    def __iter__(self):


    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
     

    def remove(self, value):    # O(n)
        """ 删除包含值的一个节点，将其前一个节点的 next 指向被查询节点的下一个即可
        :param value:
        """
      

    def find(self, value):    # O(n)
        """ 查找一个节点，返回序号，从 0 开始
        :param value:
        """
      

    def popleft(self):    # O(1)
        """ 删除第一个链表节点
        """
     

    def clear(self):
   

    def reverse(self):
        """反转链表"""
       


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))

def test_single_node():
    # https://github.com/PegasusWang/python_data_structures_and_algorithms/pull/21
    ll = LinkedList()
    ll.append(0)
    ll.remove(0)
    ll.appendleft(1)
    assert list(ll) == [1]

def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_single_node()
#    test_linked_list()
#    test_linked_list_append()
#    test_linked_list_reverse()
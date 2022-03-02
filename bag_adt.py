# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:28:02 2022

@author: zongyue.liu
"""

class Bag(object):

    def __init__(self, maxsize=10):
        self._items= list()
        self.maxsize=maxsize


    def add(self, item):
        if self.__len__()>=self.maxsize:
            raise Exception('bag is full')
            
        self._items.append(item)


    def remove(self, item):
        self._items.remove(item)


    def __len__(self):
        return len(self._items)


    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag(maxsize=2)

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)


if __name__ == '__main__':
    test_bag()
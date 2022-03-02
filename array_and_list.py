# 实现定长的 Array ADT，省略了边界检查等

class Array(object):

    def __init__(self, size=32):
        self.size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]       


    def __setitem__(self, index, value):
        self._items[index] = value


    def __len__(self):
        return len(self._items)


    def clear(self, value=None):
        for item in self._items:
            item = None


    def __iter__(self):
        for item in self._items:
            yield item



def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10
    
test_array()
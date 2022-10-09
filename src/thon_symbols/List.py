class List(list):
    def push(self, item):
        self.insert(0, item)
    def first(self, types, b=True, n=1):
        k = n
        ret = []
        for item in self:
            if isinstance(item, types) == b:
                k -= 1
                ret.append(item)
                if not k:
                    break
        if n > 1:
            return ret
        return ret[0]
    @property
    def sum(self):
        if not self:
            return 0
        return sum(self[1:], start=self[0])
    @property
    def product(self):
        ret = 1
        for item in self:
            ret *= item
        return ret
    def removeAll(self, item):
        while item in self:
            self.remove(item)
    @property
    def repeat(self):
        class RepeatingList(List):
            def __init__(self, lst):
                self.lst = lst
                super().__init__(lst)
            def __iter__(self):
                while True:
                    for i in self.lst:
                        yield i
        return RepeatingList(self)
        

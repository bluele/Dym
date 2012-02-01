#-*- coding:utf-8 -*-

from ngram import NGram

__all__ = ('Dym',)

class Dym():
    
    def __init__(self, candidates, default_num=1):
        '''
        @param candidates: list or tuple: list for candidate string
        @param default_num: int: the default number of candidate string to show
        '''
        if isinstance(candidates, list) or isinstance(candidates, tuple):
            self.index = _Indexer(candidates, default_num)
        else:
            raise TypeError("You specify 'list' or 'tuple' for parameter 'candidates'")
        self.default_num = default_num
        
    def parse(self, opt, num):
        '''
        @param opt: str: target string
        @param num: int: the number of cacndidate string to show
        '''
        return self.index.parse(opt, num)

class _Indexer():

    def __init__(self, lst, default_num):
        '''
        @param lst: list or tuple: target list
        @param default_num: int: the default number of candidate string to show
        '''
        self.lst = lst
        self.index = NGram()
        for i in lst:
            self.index.add(i)
        self.default_num = default_num
        
    def parse(self, opt, num=None):
        '''
        @param: opt: str: target string
        @param: num: int: the number of candidate string to show
        '''
        _num = self.default_num
        if num is not None: _num = num
        return [item[0] for item in sorted(self.index.search(opt), cmp=lambda x,y:cmp(y[1], x[1]))[:_num]]
    

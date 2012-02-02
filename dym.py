#-*- coding:utf-8 -*-

from ngram import NGram

__all__ = ('Dym',)

class Dym():
    
    def __init__(self, candidates, default_num=1, default_score=0.30):
        '''
        @param candidates: list or tuple: list for candidate string
        @param default_num: int: the default number of candidate string to show
        @param default_score: float: similarity of string limit
        '''
        if isinstance(candidates, list) or isinstance(candidates, tuple):
            self.index = _Indexer(candidates)
        else:
            raise TypeError("You specify 'list' or 'tuple' for parameter 'candidates'")

        self.default_num = default_num
        self.default_score = default_score
        
    def parse(self, opt, num=None, score=None):
        '''
        @param opt: str: target string
        @param num: int: the number of cacndidate string to show
        @param score: float: similarity of string limit
        '''
        if num is None:
            num = self.default_num
        if score is None:
            score = self.default_score
        return self.index.parse(opt, num, score)

class _Indexer():

    def __init__(self, lst):
        '''
        @param lst: list or tuple: target list
        '''
        self.lst = lst
        self.index = NGram()
        for i in lst:
            self.index.add(i)
        
    def parse(self, opt, num, score):
        def parse_score(lst, score):
            for item in lst:
                if item[1] >= score:
                    yield item
        '''
        @param: opt: str: target string
        @param: num: int: the number of candidate string to show
        @param score: float: similarity of string limit
        '''
        return [item[0] for item in sorted(parse_score(self.index.search(opt), score), cmp=lambda x,y:cmp(y[1], x[1]))[:num]]
    

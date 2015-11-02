#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

def timeit(func):
    def handle_args(*args, **kwargs):
        print func.__name__+' strat'
        start = time.clock()
        ret = func(*args, **kwargs)
        end =time.clock()
        print func.__name__+' is end, used:', end - start
        return ret
    return handle_args
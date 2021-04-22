# -- coding: utf-8 --
"""
Created on Thu Mar 25 12:47:32 2021

@author: isnan
"""


def stack_baru():
    lis = []
    return lis


def push(S, data):
    #addTail => topnya adalah tail,
    #addHead => topnya adalah head,
    S.append(data)


def pop(S):
    #removeTail => topnya adalah tail,
    #removeHead => topnya adalah head,
    if len(S) > 0:
        S.pop()


def peek(S):
    return S[-1]


def display(S):
    print(S)


def length(S):
    return len(S)


stack = stack_baru()
push(stack, "kambing")
push(stack, "sapi")
push(stack, "ayam")
display(stack)
pop(stack)
display(stack)

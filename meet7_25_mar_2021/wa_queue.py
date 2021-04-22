# -- coding: utf-8 --
"""
Created on Thu Mar 25 13:02:21 2021


"""

def queue_baru():
    lis = []
    return lis

def enqueue(S, data):
    #addTail
    S.append(data)

def dequeue(S):
    #removeHead
    if len(S)>0:
        S.pop(0)

def display(S):
    print(S)

def length(S):
    return len(S)

q = queue_baru()
enqueue(q, "kambing")
enqueue(q, "sapi")
enqueue(q, "ayam")
display(q)
dequeue(q)
display(q)

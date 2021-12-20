from collections import deque

MAX_LEN = 5

lifo =deque(maxlen=MAX_LEN)


def push(element):
    global lifo
    lifo.appendleft(element)
    


def pop():
    global lifo 
    return lifo.popleft()
     
    
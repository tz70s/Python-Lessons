#!/usr/bin/env python3
import stack
import queue

opset = {'*','+','(',")"}

def readinfix():
    fh = open("infix.txt")
    li = []
    li += fh.read()
    print (li)
    return li

def eval():
    evlist = readinfix()
    postlist = []
    st = stack.Stack()
    for op in evlist:
        if op in opset:
            st.push(op)
        else:
            postlist.append(op)

            if st.isEmpty:
                continue
            else:
                postlist.append(st.pop())

    print (postlist)

if __name__ == "__main__":
    eval()

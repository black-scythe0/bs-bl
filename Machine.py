#!/usr/python3 


def enum(Reset=False):
    global n
    if Reset:
        n = -1
    n +=1
    return n


PPUSH = enum(Reset=True)
PPLUS = enum()
PMINUS = enum()
PPOP = enum()
PDUMP = enum()
EMPTY = enum()


def Push(x):
    return (PPUSH, x)
def Plus():
    return (PPLUS,)
def Minus():
    return (PMINUS,)
def Pop(x):
    return (PPOP, x)
def Dump():
    return (PDUMP,)
def Empty():
    return (EMPTY,)
    
def interpreter(program):
    stack = []
    for op in program:
        if op[0] == 0:
           a = stack.append(op[1])
          
        elif op[0] == 1:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
            print(stack.pop())  
        elif op[0] == 2:
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
            print(stack.pop())
        elif op[0] == 3:
           print(list(op).pop())
        elif op[0] == 6:
            remove( stack )           

def compiler():
    assert False, "implimentation due"



if __name__ == '__main__':
    program = [
        Push(90),
#        Push(10),
 #       Minus(),
        Empty(),
#        Push(0),
        Push(80),
        Plus(),
        Pop(10),
        Pop(10)
    ]

    interpreter(program)

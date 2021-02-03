
s = []

def add(x):
    global s
    if x not in s:
        s.append(x)

def remove(x):
    global s
    if x in s:
        temp = s.index(x)
        del s[temp]

def check(x):
    global s
    if x in s:
        print(1)
    else:
        print(0)

def toggle(x):
    global s
    if x in s:
        remove(x)
    else:
        add(x)

def all_():
    global s
    s = [i for i in range(1, 21)]

def empty():
    global s
    s = []


m = int(input())
op = []

for i in range(m):
    a = input()
    a = a.split(' ')
    

        


print(op)

    
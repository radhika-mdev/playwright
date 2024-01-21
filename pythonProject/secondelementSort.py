list1=[(1,2),(4,1),(2,3),(6,0)]

def secondelem(elem):
    return elem[1]

list1.sort(key=secondelem)

print(list1)
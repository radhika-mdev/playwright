
list1=['a',1,'b',2,'c',3]

val={}

val={list1[i]:list1[i+1] for i in range(0,len(list1),2)}
print(val)
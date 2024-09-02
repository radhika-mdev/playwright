l1=[1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]

res=[num for num in l1 if l1.count(num)>1]
print (set(res))
# test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# res=dict()
# for dat in test_list:
#    res[tuple(test_list[:2])]=tuple(test_list[2:])
#    print(str(res))

rad={"1":"a","2":"b"}

print(len(rad))

rad["3"]="c"
rad1={"4":"d"}
rad.update(rad1)
rad.pop("1")

del rad["2"]
print(rad)

numb=[1,3,5,7]
di=dict()
for i in numb:
   new=i*5
   di[i]=new
print(di)
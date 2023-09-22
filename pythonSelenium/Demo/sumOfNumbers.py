#[1,2,3,9,5,5,8]  total=10
def searchnum(n,k):
    pair={}
    for i in n:
        num=k-i
        if num in n and i !=num:
            pair[num]=i
        elif num in n and i ==num and n.count(num)>1:
            pair[num]=i
        else:
            pass
    return pair
print(searchnum([1,2,3,9,5,8],10))
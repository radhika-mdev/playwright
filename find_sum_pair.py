def find_sumPair (A, n, K):
    result=[]
    for i in range(0, n ):
        #print("loop1")
        for j in range( i+1, n):
            #print("loop2")
            for k in range(j+1,n):
                #print("loop3")
                if(A[i]+A[j]+A[k] == K):
                    #print(A[i],A[j],A[k])
                    result.append((A[i],A[j],A[k]))


    return result


print(find_sumPair([3,7,1,2,8,4,5,9],8,15))


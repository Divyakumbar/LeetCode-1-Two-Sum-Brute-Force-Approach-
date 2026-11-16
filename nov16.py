#finding indices of ele in given list so that it makes target
l=[2,7,11,15]
target=17
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            print(i,j)
ls = [1,2,5,2,6,7,3]

k=4

for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i] +ls[j] == k:
            print(ls[i],ls[j])
li = [10,25,5,40,36,80,100]
# n = len(li)
# for i in range(n):
#     for j in range(i+1,n):
#         if li[i]>li[j]:
#             li[i],li[j]=li[j],li[i]
li.sort()
print(li)



def a_fun(ls):
 print(ls)
 return ls[2]


ls = [[1,55,5],[3,3,1],[2,4,3]]
ls.sort(key=a_fun)
print(ls)
# def fun(a,b):
#  return a+b

# fun = lambda a,b:a+b

# print(fun(5,3))


def a_fun(ls):
 print(ls)
 return ls[2]


ls = [[1,55,5],[3,3,1],[2,4,3]]
ls.sort(key=lambda ls:ls[0])
print(ls)
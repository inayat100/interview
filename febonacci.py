# def febonacci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
  
def febonacci():
    a,b=0,1
    while a<=13:
        print(a)
        a,b=b,a+b
        
      
# f1 = febonacci()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))


febonacci()
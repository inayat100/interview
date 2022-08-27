# s = "nitin"

# if s == s[::-1]:
#     print("yes",s)
# else:
#     print("no it is no")

s = "nitin"
l = len(s)
x = 0
for i in range(l):
    
    if s[i] != s[l-i-1]:
        x=1
        break
    print(i)
if x == 0:
    print("yes")
else:
    
    print("no")
        
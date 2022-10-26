n = 12345
r = 0
while n != 0:
 d = n % 10
 r = r*10 + d
 n = n // 10
print(r)

#########################

n = 12345
s = str(n)
print(s[::-1])
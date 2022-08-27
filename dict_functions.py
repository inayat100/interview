#py min same work list and tuple
#py max same work list and tuple
#py sum same work list and tuple
#py 1 len() this is return lenth of dict 
#py 2 any() it's check any key existin dist and it's return ture and false
#py 3 all() it's check all key existin dist and it's return ture and false
#py 4 sorted() it's return a sorted dict keys list

# 5 keys() it's return all keys to the dict
# 6 values() it's return all values to the dict
# 7 items() it's retuen key and value tuple list 
# 8 get() it's find by using key if get then return that value another return None
# 9 clear() it's clear all key valus in dict and empty dict
# 10 copy() it's copy dicts in another variable
# 11 pop() it's remove the value by using key and return remove value
# 12 popitem() it's remove last item of dict
# 13 fromkey() by using this function we can give the same value multiple keys
# 14 update() its used for the add two  dict or append like a list

# 1 len() this is return lenth of dict 

# d ={1:"one",2:"two",3:"three",4:"fore",5:"five"}
# l = len(d)
# print(d)
# print(l)

# 2 any() it's check the any key of dict valute ture and it's return ture and false

# d ={1:"one",2:"two",3:"three",4:"fore",5:"five"}
# l = any(d)
# print(d)
# print(l)

# 3 any() it's check any key existin dist and it's return ture and false

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# l = all(d)
# print(d)
# print(l)

# 4 sorted() it's return a sorted dict keys list

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# l = sorted(d)
# print(d)
# print(l)

# 5 keys() it's return all keys to the dict

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# l = d.keys()
# print(d)
# print(l)

# 6 keys() it's return all values to the dict

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# l = d.values()
# print(d)
# print(l)

# 7 items() it's retuen key and value tuple list 

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# l = d.items()
# print(d)
# print(l)

# 8 get() it's find by using key if get then return that value another return None

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# l = d.get(7,10)#pass any defalt value 10 return when the value is not finded
# print(d)
# print(l)

# 9 clear() it's clear all key valus in dict and empty dict

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# d.clear()
# print(d)

# 10 copy() it's copy dicts in another variable

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# c = d.copy()
# print(c)

# 11 pop() it's remove the value by using key and return remove value

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# print(d.pop(2))
# print(d)

# 12 popitem() it's remove last item of dict

# d ={1:"one",3:"three",4:"fore",2:"two",5:"five"}
# print(d.popitem())
# print(d)

# 13 fromkey() by using this function we can give the same value multiple keys
# key = ['a','i','o','e','u']
# valu = "vovles"
# d = dict.fromkeys(key,valu)
# print(d)

# 14 update() its used for the add two  dict or append like a list

# d1 = {1:"one",2:"two",3:"three"}
# d2 = {"name":"inayat","roo":202,"city":"saidpur"}
# d1.update(d2)
# print(d1)
#py 1 len() total number of elemments in a list
#py 14 sorted() it is sort list of items default increasing order return sorting listj
#py 15 min() return minimum element of the list
#py 16 max() return maximum element of the list
#py 17 sum() return sum all list elements use only for integers 
#py all
#py any

#2 list() convert in list as a type (str,list,tuple)
#3 index()returns the index of first matched item
#4 append()adds an items to the end of the list,not return any value,modifies the original list
#5 extend() used for adding multiple elements at the end to a list ,no return values
#6 insert() this is used for insert an element at any index position in list
#7 pop() this used for remove the item from the list if not have index then specali pop remove last elementsj and return deleted elemrnt
#8 remove()
# it's is remove first given matched item
#9 clear() this remove all items in the list list will be empty
#10 del() used for deleted multiple items also using slicing by using indexing it candelet entire list 
#11 count() returs the counts of items if item is not in the list the return 0
#12 reverse() it is reverse the list items
#13 sort() it is sort list of items default increasing order not return sorting list

# 1 len() total number of elemments in a list

# l = [1,2,5,3,5,5]
# print(len(l))

# 2  list() convert in list as a type (str,list,tuple)

# s = "inayat" 
# s1 = list(s)
# print(s1)

#3 index()returns the index of first matched item

# l = [1,2,5,3,5,5]
# ind = l.index(5)
# print(ind)

#4 append()adds an items to the end of the list,not return any value,modifies the original list

# l = [1,2,5,3,5,5]
# l.append(4)
# l.append([4,6,7,8])
# print(len(l))

#5 extend() used for adding multiple elements at the end to a list ,no return values

# l = [1,2,5,3,5,5]
# l.extend([4,6,7,8])
# print(len(l))

#6 insert() this is used for insert an element at any index position in list

# l = [1,2,5,3,5,5]
# l.insert(2,3)
# print(l)

#7 pop() this used for remove the item from the list if not have index then specali pop remove last elements and return deleted elemrnt

# l = [1,2,5,3,5,5]
# t=l.pop(2)
# print(t,l)

#8 remove() it's is remove first given matched item

# l = [1,2,5,3,5,5]
# l.remove(2)
# print(l)

#9 clear() this remove all items in the list list will be empty

# l = [1,2,5,3,5,5]
# l.clear()
# print(l)

#10 del() used for deleted multiple items also using slicing by using indexing it candelet entire list 

# l = [1,2,5,3,5,15]
# del l[:3]
# print(l)

#11 count() returs the counts of items if item is not in the list the return 0

# l = [1,2,5,3,5,5]
# con = l.count(5)
# print(l)
# print(con)

#12 reverse() it is reverse the list items

# l = [1,2,5,3,5,5]
# l.reverse()
# print(l)

#13 sort() it is sort list of items default increasing order not return sorting list

# l = [1,2,5,3,5,5]
# l.sort() # reverse=True use for  decreasing order
# print(l)

#14 sorted() it is sort list of items default increasing order return sorting list

# l = [1,2,5,3,5,5]
# t = sorted(l) # reverse=True use for  decreasing order
# print(l)
# print(t)

#15 min() return minimum element of the list

# l = [1,2,5,3,5,5]
# t = min(l)
# print(l)
# print(t)

#16 max() return maximum element of the list

# l = [1,2,5,3,5,5]
# t = max(l)
# print(l)
# print(t)

#17 sum() return sum all list elements use only for integers

# l = [1,2,5,3,5,5]
# t = sum(l)
# print(l)
# print(t)
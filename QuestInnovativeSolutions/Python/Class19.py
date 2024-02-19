#access set item
#cannot access by index position
# a={2,3,4,2,4,1,5}
# for i in a:
#     print(i)
    
#add items to set
# add()
# a={2,3,4,2,4,6,1}
# a.add(5)
# print(a)

#update()
# b={8,9,7}
# a.update(b)
# print(a)

#remove item from a set
#remove()
# a={2,3,4,2,4,6,1}
# a.remove(4)     #if the item not present in the set it returns "keyerror"
# print(a)

# # Discard()
# a={2,3,4,2,4,6,1}
# a.discard(4)     #if the item not present in the set it willnot returns error
# print(a)

#pop()

# a={2,3,4,2,4,6,1}
# a.pop()     #it remove the first element from the list
# print(a)

#clear          -->clear the set values

# a={2,3,4,2,4,6,1}
# a.clear()
# print(a)

#del()

#Join two sets

# a={'abc','def'}
# b={1,2,3,4}
# c=a.union(b)
# print(c)

"""or"""
#we can add more than two sets using operator ex:a|b|c

# a={'abc','def'}
# b={1,2,3,4}
# c=a|b
# print(c)

#intersection

a={"abc","def","ghi"}
b={1,2,3,4,"abc","def"}
join=a.intersection(b)
print(join)

#using operator
a={"abc","def"}
b={1,2,3,4,"abc"}
j=a&b
print(j)

#difference
# a={"abc","def","ghi"}
# b={1,2,3,4,"abc","ghi"}
# join=b.difference(a)
# print(join)

# a={"abc","def","ghi"}
# b={1,2,3,4,"abc","ghi"}
# join=a-b
# print(join)

#symmetric difference
a={"abc","def","ghi"}
b={1,2,3,4,"abc","ghi"}
join=a.symmetric_difference(b)
print(join)

a={"abc","def","ghi"}
b={1,2,3,4,"abc","ghi"}
join=b^a
print(join)
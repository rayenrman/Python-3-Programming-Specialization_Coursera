lst = ['a', 'b', 'c']
print('lst:', lst)
first_type = type(lst[0])
for item in lst:
    print(item, type(item))
    assert type(item) == first_type


lst2 = ['d', 'e', 'f', 17]
print('lst2:', lst2)
first_type = type(lst2[0])
for item in lst2:
    print(item, type(item))
    assert type(item) == first_type

# AssertionError at line 14: assert type(item) == first_type 
#                            when item == 17
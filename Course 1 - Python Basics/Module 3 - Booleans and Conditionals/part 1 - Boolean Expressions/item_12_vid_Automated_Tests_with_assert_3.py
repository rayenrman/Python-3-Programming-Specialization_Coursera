lst = ['a', 'b', 'c']
print('lst:', lst)
assert len(lst) < 4

lst2 = ['d', 'e', 'f', 17]
print('lst2:', lst2)
assert len(lst2) < 4   # AssertionError

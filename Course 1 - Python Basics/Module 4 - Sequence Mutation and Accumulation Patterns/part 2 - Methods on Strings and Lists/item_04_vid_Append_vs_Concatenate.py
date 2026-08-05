origlist = [45, 32, 88]
print('origlist     :', origlist)
print('id(origlist) :', id(origlist))
aliaslist = origlist
print('aliaslist    :', aliaslist)
print('id(aliaslist):', id(aliaslist))
origlist += ['cat']
print('origlist     :', origlist)
print('id(origlist) :', id(origlist))
print('aliaslist    :', aliaslist)
print('id(aliaslist):', id(aliaslist))
print('aliaslist is origlist:', aliaslist is origlist)
origlist.append('dog')
print('origlist     :', origlist)
print('id(origlist) :', id(origlist))
print('aliaslist    :', aliaslist)
print('id(aliaslist):', id(aliaslist))
print('aliaslist is origlist:', aliaslist is origlist)
origlist = origlist +  ['cow']
print('origlist     :', origlist)
print('id(origlist) :', id(origlist))
print('aliaslist    :', aliaslist)
print('id(aliaslist):', id(aliaslist))
print('aliaslist is origlist:', aliaslist is origlist)

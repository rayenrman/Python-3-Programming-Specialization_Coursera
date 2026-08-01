julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print('julia   :', julia)
print('julia[:]:', julia[:])
print('type(julia[:]):', type(julia[:]))
print('len(julia[:]):', len(julia[:]))
print('julia[2]:', julia[2])
print('type(julia[2]):', type(julia[2]))
print('julia[2:6]:', julia[2:6])
print('len(julia):', len(julia))
print('julia[5:8]:', julia[5:8])

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print('julia:', julia)
print('type(julia):', type(julia))

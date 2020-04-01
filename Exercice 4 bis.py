def listSum(l):
    if len(l) == 0 :
        return 0
    return int(l[0]) + listSum(l[1:])

print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11

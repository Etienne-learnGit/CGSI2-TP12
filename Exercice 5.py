def product(a, b) :
    if b == 0 :
        return 0
    return a + product(a, b-1)

print(product(5,2)) # 10
print(product(9,3)) # 27

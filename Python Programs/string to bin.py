a = 'A'
b = bin(ord(a))
print(b)
p = [bool(int("0"))]
for i in b[2:]:
    p.append(bool(int(i)))
print(len(p))
print(type(p[0:3]))
print(p[0:3])

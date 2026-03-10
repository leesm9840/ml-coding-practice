a = 3
b = 4

print(a ** b)
print(a ** 3)

print(a % b)
print(7 % 3)

print(a // b)
print(7 // 3)

s1 = 'Hello Python'
print(s1)

s3 = '''Hello
Python'''
print(s3)

head = "Python"
tail = "is fun"
print(head + tail)

print(head * 2)
print("=" * 5)

a = "Now is better than never"
print(a[0])
print(a[4])
print(a[-1])
print(a[-2])

b = a[0] + a[1] + a[2]
print(b)

print(a[4:6])
print(a[19:])
print(a[:3])
print(a[7:-11])

a = "Python"
print(a.count('p'))

print(a.find('y'))
print(a.find('p'))
print(a.index('y'))

b= ","
c= b.join('Abcd')
print(c)

print(a.upper())
print(a.lower())

d = "               py                  "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

a = "Pithon"

a = "Python is difficult."
print(a.replace("difficult", "funny"))
print(a)

print(a.split())

b = "a, b, c, d"
print(b)
print(b.split(','))

a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']]

print(d[0])
print(d[2])
print(d[3][-1])

print(d[0:3])

print(a+b)
print(b[0] + " hi~ ^^;")

print(a * 3)

a[2] = 99
print(a)

a[1:2] = ['a', 'b', 'c']
print(a)

a[-1] = ['d', 'e', 'f']
print(a)

del a[-1]
print(a)

a.append(5)
print(a)

b.sort()
print(a)

a = [3, 4, 1, 9]
a.reverse()
print(a)

print(a.index(9))

a.insert(0, 99)
print(a)

a.remove(99)
print(a)

b = [1, 2, 3]
print(b.pop())
print(b)

print(b.pop(0))
print(b)

a = [2, 1, 0, 2, 3, 2, 4, 2]
print(a.count(2))

t1 = (1, )
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4), ('Life', 'is'))

print(t4[0])
print(t4[3][-1])

t4[0:3]

print(t1 + t2)

t2 * 10

dic = {'name':'Hong', 'phone':'01012345678', 'birth':'0814'}

dic[1] = 'a'
print(dic)

dic['pet'] = 'dog'
print(dic)

del dic[1]
print(dic['phone'])
print(dic['name'])

print(dic.keys())
print(list(dic.keys()))

for key in dic.keys():
    print(dic[key])

print(dic.values())
print(list(dic.values()))

for key, value in dic.items():
    print()





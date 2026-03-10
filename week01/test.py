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
print(dic)

print(dic['phone'])
print(dic['name'])

print(dic.keys())
print(list(dic.keys()))

for key in dic.keys():
    print(dic[key])

print(dic.values())
print(list(dic.values()))

print(dic.items())

for key, value in dic.items():
    print(key + ":" + value)

dic.clear()
print(dic)

s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2)
s3 = set([4, 5, 6, 7, 8, 9])
print(s3)

print(s2 | s3)
print(s2.union(s3))

print(s2 - s3)
print(s3 - s2)
print(s2.difference(s3))
print(s3.difference(s2))

s2.add(7)
print(s2)

s2.update([6, 7, 8, 9, 10])
print(s2)

s2.remove(7)
print(s2)

s2 = set([1, 2, 3, 4, 5, 6, 3, 1, 6])
print(s2)

x = 3
y = 2
print(x == y)
print(x != y)
print(x >= y)

money = 1300
if money >= 1200 and money < 3500:
    print('버스를 탈 수 있습니다.')

print(1 in [1, 2, 3])
print(x in [1, 2, 3])
print(x not in [1, 2, 3])
print('a' in ['a', 'b', 'c', 'd'])
print('i' not in 'Python')

if money >= 10:
    pass
else:
    print('저금하자!')

test_list = ['one', 'two', 'three']
for i in test_list:
    x = i + '!'
    print(x)

number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1

    if score > 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다."%number)

i = 0
while i < 5:
    i += 1
    print('*' * i)

def sum1(a, b):
    x = a + b
    return x




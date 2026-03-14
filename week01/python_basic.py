a = 3
b =4

# ì§??ˆ˜?Š¹
print(a ** b)
print(a ** 3)

# ?‚˜ë¨¸ì?? ?—°?‚°
print(a % b)
print(7 % 3)

# ?‚˜?ˆ—?…ˆ ëª? êµ¬í•˜ê¸?
print(a // b)
print(7 // 3)

s1 = 'Hello Python'
print(s1)

s3 = '''Hello 
Python'''
print(s3)

head = "Python"
tail = " is fun"
print(head + tail)

# ë¬¸ì?—´ ê³±í•˜ê¸?
print(head * 2)
print("=" * 5)

# ë¬¸ì?—´ ?¸?±?‹±
a = "Now is better than never"
print(a[0])
print(a[4])
print(a[-1])
print(a[-2])

# ë¬¸ì?—´ ?Š¬?¼?´?‹±
b = a[0] + a[1] + a[2]
print(b)

print(a[4:6])
print(a[19:])
print(a[:3])
print(a[7:-11])

# ë¬¸ì ê°œìˆ˜ ê³„ì‚°
a = "Python"
print(a.count('p'))

# ë¬¸ì ?œ„ì¹? ?™•?¸
print(a.find('y'))
print(a.find('p'))
print(a.index('y'))
# print(a.index('p')) # ?˜¤ë¥? ë°œìƒ

# ë¬¸ì ?‚½?…
b = ","
c = b.join('Abcd')
print(c)

# ????†Œë¬¸ì ë³??™˜
print(a.upper())
print(a.lower())

# ê³µë°± ? œê±?
d = "           py          "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

# ë¬¸ì?—´ ?ˆ˜? • (ë¶ˆê???Š¥)
a = "Python"
# a[1] = 'y'    #?˜¤ë¥? ë°œìƒ

# ë¬¸ì?—´ ë°”ê¾¸ê¸?
a = "Python is difficult."
print(a.replace("difficult", "funny"))
print(a)

# ë¬¸ì?—´ ?‚˜?ˆ„ê¸?
print(a.split())

b = "a, b, c, d"
print(b)
print(b.split(','))

# ë¦¬ìŠ¤?Š¸ ë§Œë“¤ê¸?
a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']]

# ë¦¬ìŠ¤?Š¸ ?¸?±?‹±
print(d[0])
print(d[2])
print(d[3][-1])

# ë¦¬ìŠ¤?Š¸ ?Š¬?¼?´?‹±
print(d[0:3])

# ë¦¬ìŠ¤?Š¸ ?Š¬?¼?´?‹±
print(a + b)
print(b[0] + " hi~ ^^;")
# print(a[0] + " hi~ ^^;")  # ?˜¤ë¥? ë°œìƒ

# ë¦¬ìŠ¤?Š¸ ë°œìƒ
print(a * 3)

# ë¦¬ìŠ¤?Š¸ ?ˆ˜? •
a[2] = 99
print(a)

a[1:2] = ['a', 'b', 'c']
print(a)

a[-1] = ['d', 'e', 'f']
print(a)

# ?‚­? œ
del a[-1]
print(a)

# ?›?†Œ ì¶”ê??
a.append(5)
print(a)

# ?›?†Œ ? •? ¬
b.sort()
print(a)

# ?›?†Œ ?ˆœ?„œ ?’¤ì§‘ê¸°
a = [3, 5, 1, 9]
a.reverse()
print(a)

# ?›?†Œ ?œ„ì¹? ?™•?¸
print(a.index(9))

# ?›?†Œ ?‚½?…
a.insert(0, 99)
print(a)

# ?›?†Œ ?‚­? œ
a.remove(99)
print(a)

b = [ 1, 2, 3]
print(b.pop())
print(b)

print(b.pop(0))
print(b)

# ?Š¹? • ?›?†Œê°’ì˜ ê°œìˆ˜
a = [2, 1, 0, 2, 3, 2, 4, 2]
print(a.count(2))

# ?Šœ?”Œ ë§Œë“¤ê¸?
t1 = (1, )
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4), ('Life', 'is'))

# ?Šœ?”Œ ?¸?±?‹±
print(t4[0])
print(t4[3][-1])

# ?Šœ?”Œ ?Š¬?¼?´?‹±
t4[0:4]

# ?Šœ?”Œ ?—°ê²?
print(t1 + t2)
# print(t1 + "hi~ ^^;")     # ?˜¤ë¥? ë°œìƒ

#?Šœ?”Œ ë°˜ë³µ
t2 * 10

# ?Šœ?”Œ ?ˆ˜? •(ë¶ˆê???Š¥)
# t2[2] = 99    # ?˜¤ë¥? ë°œìƒ

# ?”•?…”?„ˆë¦? ë§Œë“¤ê¸?
dic = {'name':'Hong', 'phone':'01012345678', 'birth':'0814'}

# ?›?†Œ ì¶”ê??
dic[1] = 'a'
print(dic)

dic['pet'] = 'dog'
print(dic)

# ?›?†Œ ?‚­? œ
del dic[1]
print(dic)

# ?›?†Œ?˜ value êµ¬í•˜ê¸?
print(dic['phone'])
print(dic['name'])

# key?˜ ë¦¬ìŠ¤?Š¸ ë§Œë“¤ê¸?
print(dic.keys())
print(list(dic.keys()))

for key in dic.keys():
    print(dic[key])

# value?˜ ë¦¬ìŠ¤?Š¸ ë§Œë“¤ê¸?
print(dic.values())
print(list(dic.values()))

# key, value ?Œ êµ¬í•˜ê¸?
print(dic.items())

for key, value in dic.items():
    print(key + ":" + value)

# ?›?†Œ ?‚­? œ
dic.clear()
print(dic)

# ì§‘í•© ë§Œë“¤ê¸?
s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2)
s3 = set([4, 5, 6, 7, 8, 9])
print(s3)

#êµì§‘?•© ?—°?‚°
print(s2 & s3)
print(s2.intersection(s3))

# ?•©ì§‘í•© ?—°?‚°
print(s2 | s3)
print(s2.union(s3))

# ì°¨ì§‘?•© ?—°?‚°
print(s2 - s3)
print(s3 - s2)
print(s2.difference(s3))
print(s3.difference(s2))

# ?›?†Œ ?•œ ê°? ì¶”ê??
s2.add(7)
print(s2)

# ?›?†Œ ?—¬?Ÿ¬ ê°? ì¶”ê??
s2.update([6, 7, 8, 9, 10])
print(s2)

# ?Š¹? • ?›?†Œ ? œê±?
s2.remove(7)
print(s2)

s2 = set([1, 2, 3, 4, 5, 6, 3, 1, 6])
print(s2)

# ë¹„êµ ?—°?‚°?
x = 3
y = 2
print(x == y)
print(x != y)
print(x >= y)

# ì¡°ê±´?˜ ?—°ê²?
money = 1300
if money >= 1200 and money < 3500:
    print('ë²„ìŠ¤ë¥? ?ƒˆ ?ˆ˜ ?ˆ?Šµ?‹ˆ?‹¤.')

# ê·¸ë£¹ ?ë£Œí˜•?˜ ?›?†Œ?¸ì§? ê²??‚¬?•˜ê¸?
print(1 in [1, 2, 3])
print(x in [1, 2, 3])
print(x not in [1, 2,3])
print('a' in ['a', 'b', 'c', 'd'])
print('i' not in 'Python')

# ?•„ë¬? ê²ƒë„ ?•˜ì§? ?•Šê²? ?„¤? •
if money >= 10:
    pass
else:
    print('???ê¸ˆí•˜?!')

"""# 4. ë°˜ë³µë¬?"""

# for ë°˜ë³µë¬?1
test_list = ['one', 'two', 'three']
for i in test_list:
    x = i + '!'
    print(x)

# for ë°˜ë³µë¬?2
number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1

    if score > 60:
        print("%dë²? ?•™?ƒ??? ?•©ê²©ì…?‹ˆ?‹¤." %number)
    else:
        print("%dë²? ?•™?ƒ??? ë¶ˆí•©ê²©ì…?‹ˆ?‹¤." %number)

#while ë¬?
i =0
while i < 5:
    i += 1
    print('*' * i)

# ?•¨?ˆ˜ ? •?˜
def sum1(a, b):
    x = a + b
    return x

def sum2(*args):
    x = 0
    for i in args:
        x += i
    return x

# ?•¨?ˆ˜ ?˜¸ì¶?
a = 5
b = 3
print(sum1(a, b))
print(sum1(3, 5))
print(sum2(1, 2, 3, 4, 5))
print(sum2(2, 3.5, 10))

"""## ?‚´?¥ ?•¨?ˆ˜"""

# ?ˆ«? x?˜ ? ˆ???ê°’ì„ ë°˜í™˜
print(abs(-3.5))

# ê·¸ë£¹ ?ë£Œí˜•?˜ ë³??ˆ˜ x?˜ ëª¨ë“  ?›?†Œê°? ì°?(0?´ ?•„?‹Œ ê°?)?´ë©? True ë°˜í™˜
print(all([1, 2, 3, 4]))
print(all([4, -2, 0.0, 4]))

# ê·¸ë£¹ ?ë£Œí˜•?˜ ë³??ˆ˜ x?˜ ?›?†Œ ì¤? ?•˜?‚˜?¼?„ ì°¸ì´ë©? True ë°˜í™˜
print(any([1, 2, 3 , 4]))
print(any([4, -2, 0.0, 4]))

# ?•„?Š¤?‚¤ì½”ë“œ ê°’ì— ????•œ ë¬¸ì ì¶œë ¥
print(chr(97))
print(chr(48))

# ë¬¸ì?— ????•œ ?•„?Š¤?‚¤ì½”ë“œ ê°? ì¶œë ¥
print(ord('a'))
print(ord('0'))

# ê°ì²´ xê°? ê°?ì§? ë©¤ë²„ ë³??ˆ˜??? ë©¤ë²„ ?•¨?ˆ˜ ë³´ì—¬ì£¼ê¸°
print(dir([1, 2, 3]))
print(dir({'1':'a'}))
print(dir(1))

print(int('3'))         # xë¥? ? •?ˆ˜ ?˜•?ƒœë¡? ë°˜í™˜
print(str(3))           # xë¥? ë¬¸ì?—´ ?˜•?ƒœë¡? ë°˜í™˜

# xë¥? ë¦¬ìŠ¤?Š¸ë¡? ë°˜í™˜
print(list("Python"))
print((1, 2, 3))

# xë¥? ?Šœ?”Œë¡? ë°˜í™˜
print(tuple("Python"))
print(tuple([1, 2, 3]))

# xë¥? ?ë£Œí˜•?„ ë°˜í™˜
print(type("abc"))
print(type(a))

# ê°„ë‹¨?•œ ?‚½?…?˜• ?•¨?ˆ˜ ?ƒ?„±
sum = lambda a, b: a + b

print(sum(3, 5))

# ìµœë??, ìµœì†Œê°? ë°˜í™˜
print(max([1, 4, 2, 8, 6]))
print(max("Python"))

print(min([1, 4, 2, 8, 6]))
print(min("Python"))

# x?˜ y? œê³? ê²°ê³¼ê°? ë°˜í™˜
print(pow(2, 4))

# ?‚¬?š©? ?…? ¥?œ¼ë¡? ë°›ì?? ê°’ì„ ë¬¸ì?—´ë¡? ë°˜í™˜1
c = input("ê°’ì„ ?…? ¥?•´ì£¼ì„¸?š”:")
print(c)

# ?‚¬?š©? ?…? ¥?œ¼ë¡? ë°›ì?? ê°’ì„ ë¬¸ì?—´ë¡? ë°˜í™˜2
c = input("? •?ˆ˜ë¥? ?…? ¥?•˜?„¸?š”: ")
print(c)

# ?…? ¥ ë°›ì?? ?ˆ«??— ?•´?‹¹?˜?Š” ë²”ìœ„?˜ ê°’ì„ ë°˜í™˜
print(range(5))
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10 ,2)))

for i in range(5, 20, 3):
    print(i)

# ?…? ¥ê°? s?˜ ê¸¸ì´ë¥? ë°˜í™˜
len('Python')

print(sorted([3, 0, 2, 1]))
print(sorted('Python'))

# ?Œ¨?‚¤ì§?, ëª¨ë“ˆ ?‚¬?š©
# Request('http://www.sunmoon.ac.kr')   # ?˜¤ë¥? ë°œìƒ

import urllib.request
urllib.request.Request('http://www.sunmoon.ac.kr')

import pandas
pandas.DataFrame()

from datetime import datetime
datetime.now()

# ?ŒŒ?¼ ê°ì²´ ?ƒ?„±
f = open('example.txt', 'w')
print(f)

# ?ŒŒ?¼ ?‹«ê¸?
f.close()

# ?”¼?¼ ?“°ê¸?
f = open('example.txt', 'w')
for i in range(1, 6):
    data = '%dë²ˆì§¸ ì¤„ì…?‹ˆ?‹¤. \n' % i
    f.write(data)
f.close()

# ?ŒŒ?¼?— ?‚´?š© ì¶”ê???•˜ê¸?
f = open('example.txt', 'w')
for i in range(6, 11):
    data = '%dë²ˆì§¸ ì¤? ì¶”ê???•©?‹ˆ?‹¤. \n' % i
    f.write(data)
f.close()

# ?ŒŒ?¼ ëª¨ë“œ 'r' - readline()
f = open('example.txt', 'r')


while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()

# ?ŒŒ?¼ ëª¨ë“œ 'r' - readline()
f = open('example.txt', 'r')
lines = f.readlines()
print(lines)

for line in lines:
    print(line)

f.close()

# ?ŒŒ?¼ ëª¨ë“œ 'r' - read()
f = open('example.txt', 'r')
data = f.read()
f.close()
data

# with open() as ?ŒŒ?¼ ê°ì²´
with open('example.txt', "w") as f:
    f.write("Now is better than never.")
# data = f.read()       # ?˜¤ë¥? ë°œìƒ

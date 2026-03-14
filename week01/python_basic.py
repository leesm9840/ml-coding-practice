a = 3
b =4

# ������
print(a ** b)
print(a ** 3)

# ������ ����
print(a % b)
print(7 % 3)

# ������ �� ���ϱ�
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

# ���ڿ� ���ϱ�
print(head * 2)
print("=" * 5)

# ���ڿ� �ε���
a = "Now is better than never"
print(a[0])
print(a[4])
print(a[-1])
print(a[-2])

# ���ڿ� �����̽�
b = a[0] + a[1] + a[2]
print(b)

print(a[4:6])
print(a[19:])
print(a[:3])
print(a[7:-11])

# ���� ���� ���
a = "Python"
print(a.count('p'))

# ���� ��ġ Ȯ��
print(a.find('y'))
print(a.find('p'))
print(a.index('y'))
# print(a.index('p')) # ���� �߻�

# ���� ����
b = ","
c = b.join('Abcd')
print(c)

# ��ҹ��� ��ȯ
print(a.upper())
print(a.lower())

# ���� ����
d = "           py          "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

# ���ڿ� ���� (�Ұ���)
a = "Python"
# a[1] = 'y'    #���� �߻�

# ���ڿ� �ٲٱ�
a = "Python is difficult."
print(a.replace("difficult", "funny"))
print(a)

# ���ڿ� ������
print(a.split())

b = "a, b, c, d"
print(b)
print(b.split(','))

# ����Ʈ �����
a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']]

# ����Ʈ �ε���
print(d[0])
print(d[2])
print(d[3][-1])

# ����Ʈ �����̽�
print(d[0:3])

# ����Ʈ �����̽�
print(a + b)
print(b[0] + " hi~ ^^;")
# print(a[0] + " hi~ ^^;")  # ���� �߻�

# ����Ʈ �߻�
print(a * 3)

# ����Ʈ ����
a[2] = 99
print(a)

a[1:2] = ['a', 'b', 'c']
print(a)

a[-1] = ['d', 'e', 'f']
print(a)

# ����
del a[-1]
print(a)

# ���� �߰�
a.append(5)
print(a)

# ���� ����
b.sort()
print(a)

# ���� ���� ������
a = [3, 5, 1, 9]
a.reverse()
print(a)

# ���� ��ġ Ȯ��
print(a.index(9))

# ���� ����
a.insert(0, 99)
print(a)

# ���� ����
a.remove(99)
print(a)

b = [ 1, 2, 3]
print(b.pop())
print(b)

print(b.pop(0))
print(b)

# Ư�� ���Ұ��� ����
a = [2, 1, 0, 2, 3, 2, 4, 2]
print(a.count(2))

# Ʃ�� �����
t1 = (1, )
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4), ('Life', 'is'))

# Ʃ�� �ε���
print(t4[0])
print(t4[3][-1])

# Ʃ�� �����̽�
t4[0:4]

# Ʃ�� ����
print(t1 + t2)
# print(t1 + "hi~ ^^;")     # ���� �߻�

#Ʃ�� �ݺ�
t2 * 10

# Ʃ�� ����(�Ұ���)
# t2[2] = 99    # ���� �߻�

# ��ųʸ� �����
dic = {'name':'Hong', 'phone':'01012345678', 'birth':'0814'}

# ���� �߰�
dic[1] = 'a'
print(dic)

dic['pet'] = 'dog'
print(dic)

# ���� ����
del dic[1]
print(dic)

# ������ value ���ϱ�
print(dic['phone'])
print(dic['name'])

# key�� ����Ʈ �����
print(dic.keys())
print(list(dic.keys()))

for key in dic.keys():
    print(dic[key])

# value�� ����Ʈ �����
print(dic.values())
print(list(dic.values()))

# key, value �� ���ϱ�
print(dic.items())

for key, value in dic.items():
    print(key + ":" + value)

# ���� ����
dic.clear()
print(dic)

# ���� �����
s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2)
s3 = set([4, 5, 6, 7, 8, 9])
print(s3)

#������ ����
print(s2 & s3)
print(s2.intersection(s3))

# ������ ����
print(s2 | s3)
print(s2.union(s3))

# ������ ����
print(s2 - s3)
print(s3 - s2)
print(s2.difference(s3))
print(s3.difference(s2))

# ���� �� �� �߰�
s2.add(7)
print(s2)

# ���� ���� �� �߰�
s2.update([6, 7, 8, 9, 10])
print(s2)

# Ư�� ���� ����
s2.remove(7)
print(s2)

s2 = set([1, 2, 3, 4, 5, 6, 3, 1, 6])
print(s2)

# �� ������
x = 3
y = 2
print(x == y)
print(x != y)
print(x >= y)

# ������ ����
money = 1300
if money >= 1200 and money < 3500:
    print('������ Ż �� �ֽ��ϴ�.')

# �׷� �ڷ����� �������� �˻��ϱ�
print(1 in [1, 2, 3])
print(x in [1, 2, 3])
print(x not in [1, 2,3])
print('a' in ['a', 'b', 'c', 'd'])
print('i' not in 'Python')

# �ƹ� �͵� ���� �ʰ� ����
if money >= 10:
    pass
else:
    print('��������!')

"""# 4. �ݺ���"""

# for �ݺ���1
test_list = ['one', 'two', 'three']
for i in test_list:
    x = i + '!'
    print(x)

# for �ݺ���2
number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1

    if score > 60:
        print("%d�� �л��� �հ��Դϴ�." %number)
    else:
        print("%d�� �л��� ���հ��Դϴ�." %number)

#while ��
i =0
while i < 5:
    i += 1
    print('*' * i)

# �Լ� ����
def sum1(a, b):
    x = a + b
    return x

def sum2(*args):
    x = 0
    for i in args:
        x += i
    return x

# �Լ� ȣ��
a = 5
b = 3
print(sum1(a, b))
print(sum1(3, 5))
print(sum2(1, 2, 3, 4, 5))
print(sum2(2, 3.5, 10))

"""## ���� �Լ�"""

# ���� x�� ���밪�� ��ȯ
print(abs(-3.5))

# �׷� �ڷ����� ���� x�� ��� ���Ұ� ��(0�� �ƴ� ��)�̸� True ��ȯ
print(all([1, 2, 3, 4]))
print(all([4, -2, 0.0, 4]))

# �׷� �ڷ����� ���� x�� ���� �� �ϳ��� ���̸� True ��ȯ
print(any([1, 2, 3 , 4]))
print(any([4, -2, 0.0, 4]))

# �ƽ�Ű�ڵ� ���� ���� ���� ���
print(chr(97))
print(chr(48))

# ���ڿ� ���� �ƽ�Ű�ڵ� �� ���
print(ord('a'))
print(ord('0'))

# ��ü x�� ���� ��� ������ ��� �Լ� �����ֱ�
print(dir([1, 2, 3]))
print(dir({'1':'a'}))
print(dir(1))

print(int('3'))         # x�� ���� ���·� ��ȯ
print(str(3))           # x�� ���ڿ� ���·� ��ȯ

# x�� ����Ʈ�� ��ȯ
print(list("Python"))
print((1, 2, 3))

# x�� Ʃ�÷� ��ȯ
print(tuple("Python"))
print(tuple([1, 2, 3]))

# x�� �ڷ����� ��ȯ
print(type("abc"))
print(type(a))

# ������ ������ �Լ� ����
sum = lambda a, b: a + b

print(sum(3, 5))

# �ִ�, �ּҰ� ��ȯ
print(max([1, 4, 2, 8, 6]))
print(max("Python"))

print(min([1, 4, 2, 8, 6]))
print(min("Python"))

# x�� y���� ����� ��ȯ
print(pow(2, 4))

# ����� �Է����� ���� ���� ���ڿ��� ��ȯ1
c = input("���� �Է����ּ���:")
print(c)

# ����� �Է����� ���� ���� ���ڿ��� ��ȯ2
c = input("������ �Է��ϼ���: ")
print(c)

# �Է� ���� ���ڿ� �ش�Ǵ� ������ ���� ��ȯ
print(range(5))
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10 ,2)))

for i in range(5, 20, 3):
    print(i)

# �Է°� s�� ���̸� ��ȯ
len('Python')

print(sorted([3, 0, 2, 1]))
print(sorted('Python'))

# ��Ű��, ��� ���
# Request('http://www.sunmoon.ac.kr')   # ���� �߻�

import urllib.request
urllib.request.Request('http://www.sunmoon.ac.kr')

import pandas
pandas.DataFrame()

from datetime import datetime
datetime.now()

# ���� ��ü ����
f = open('example.txt', 'w')
print(f)

# ���� �ݱ�
f.close()

# ���� ����
f = open('example.txt', 'w')
for i in range(1, 6):
    data = '%d��° ���Դϴ�. \n' % i
    f.write(data)
f.close()

# ���Ͽ� ���� �߰��ϱ�
f = open('example.txt', 'w')
for i in range(6, 11):
    data = '%d��° �� �߰��մϴ�. \n' % i
    f.write(data)
f.close()

# ���� ��� 'r' - readline()
f = open('example.txt', 'r')


while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()

# ���� ��� 'r' - readline()
f = open('example.txt', 'r')
lines = f.readlines()
print(lines)

for line in lines:
    print(line)

f.close()

# ���� ��� 'r' - read()
f = open('example.txt', 'r')
data = f.read()
f.close()
data

# with open() as ���� ��ü
with open('example.txt', 'w') as f:
    f.write("Now is better than never.")
# data = f.read()       # ���� �߻�
a = 3
b = 4

# 지수승
print(a ** b)
print(a ** 3)

# 나머지 연산
print(a % b)
print(7 % 3)

# 나눗셈 몫 구하기
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

# 문자열 곱하기
print(head * 2)
print("=" * 5)

# 문자열 인덱싱
a = "Now is better than never"
print(a[0])
print(a[4])
print(a[-1])
print(a[-2])

# 문자열 슬라이싱
b = a[0] + a[1] + a[2]
print(b)

print(a[4:6])
print(a[19:])
print(a[:3])
print(a[7:-11])

# 문자 개수 계산
a = "Python"
print(a.count('p'))

# 문자 위치 확인
print(a.find('y'))
print(a.find('p'))
print(a.index('y'))
# print(a.index('p')) # 오류 발생

# 문자 삽입
b= ","
c= b.join('Abcd')
print(c)

# 대소문자 변환
print(a.upper())
print(a.lower())

# 공백 제거
d = "               py                  "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

# 문자열 수정 (불가능)
a = "Pithon"
# a[1] = 'y'    #오류 발생

#문자열 바꾸기
a = "Python is difficult."
print(a.replace("difficult", "funny"))
print(a)

#문자열 나누기
print(a.split())

b = "a, b, c, d"
print(b)
print(b.split(','))

#리스트 만들기
a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']]

# 리스트 인덱싱
print(d[0])
print(d[2])
print(d[3][-1])

# 리스트 슬라이싱
print(d[0:3])

# 리스트 연결
print(a+b)
print(b[0] + " hi~ ^^;")
# print(a[0] +" hi~ ^^;")   #오류 발생

# 리스트 반복
print(a * 3)

# 리스트 수정
a[2] = 99
print(a)

a[1:2] = ['a', 'b', 'c']
print(a)

a[-1] = ['d', 'e', 'f']
print(a)

# 삭제
del a[-1]
print(a)

# 원소 추가
a.append(5)
print(a)

# 원소 정렬
b.sort()
print(a)

# 원소 순서 뒤집기
a = [3, 4, 1, 9]
a.reverse()
print(a)

# 원소 위치 확인
print(a.index(9))

# 원소 삽입
a.insert(0, 99)
print(a)

# 원소 삭제
a.remove(99)
print(a)

b = [1, 2, 3]
print(b.pop())
print(b)

print(b.pop(0))
print(b)

# 특정 원소값의 개수
a = [2, 1, 0, 2, 3, 2, 4, 2]
print(a.count(2))

# 튜플 만들기
t1 = (1, )
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4), ('Life', 'is'))

# 튜플 인덱싱
print(t4[0])
print(t4[3][-1])

# 튜플 슬라이싱
t4[0:3]

# 튜플 연결
print(t1 + t2)
# print(t1 + "hi~ ^^;")     #오류 발생

# 튜플 반복
t2 * 10

# 튜플 수정(불가능)
# t2[2] = 99        #오류 발생

#딕셔너리 만들기
dic = {'name':'Hong', 'phone':'01012345678', 'birth':'0814'}

# 원소 추가
dic[1] = 'a'
print(dic)

dic['pet'] = 'dog'
print(dic)

# 원소 삭제
del dic[1]
print(dic)

# 원소의 value 구하기
print(dic['phone'])
print(dic['name'])

# key의 리스트 만들기
print(dic.keys())
print(list(dic.keys()))

for key in dic.keys():
    print(dic[key])

# value의 리스트 만들기
print(dic.values())
print(list(dic.values()))

# key, value 쌍 구하기
print(dic.items())

for key, value in dic.items():
    print(key + ":" + value)

# 원소 삭제
dic.clear()
print(dic)

# 집합 만들기
s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2)
s3 = set([4, 5, 6, 7, 8, 9])
print(s3)

# 교집합 연산
print(s2 & s3)
print(s2.intersection(s3))

# 합집합 연산
print(s2 | s3)
print(s2.union(s3))

# 차집합 연산
print(s2 - s3)
print(s3 - s2)
print(s2.difference(s3))
print(s3.difference(s2))

# 원소 한 개 추가
s2.add(7)
print(s2)

# 원소 여러 개 추가
s2.update([6, 7, 8, 9, 10])
print(s2)

# 특정 원소 제거
s2.remove(7)
print(s2)

s2 = set([1, 2, 3, 4, 5, 6, 3, 1, 6])
print(s2)

# 비교 연산자
x = 3
y = 2
print(x == y)
print(x != y)
print(x >= y)

# 조건의 연결
money = 1300
if money >= 1200 and money < 3500:
    print('버스를 탈 수 있습니다.')

# 그룹 자료형의 원소인지 검사하기
print(1 in [1, 2, 3])
print(x in [1, 2, 3])
print(x not in [1, 2, 3])
print('a' in ['a', 'b', 'c', 'd'])
print('i' not in 'Python')

# 아무 것도 하지 않게 설정
if money >= 10:
    pass
else:
    print('저금하자!')

"""# 4. 반복문"""

#for 반복문1
test_list = ['one', 'two', 'three']
for i in test_list:
    x = i + '!'
    print(x)

# for 반복문2
number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1

    if score > 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다."%number)

# while 문
i = 0
while i < 5:
    i += 1
    print('*' * i)

# 함수 정의
def sum1(a, b):
    x = a + b
    return x

def sum2(*args):
    x = 0
    for i in args:
        x += i
    return x

# 함수 호출
a = 5
b = 3
print(sum1(a, b))
print(sum1(3, 5))
print(sum2(1,2, 3, 4, 5))
print(sum2(2, 3.5, 10))

"""## 내장 함수"""

# 숫자 x의 절대값을 반환
print(abs(-3.5))

# 그룹 자료형의 변수 x의 모든 원소가 참(0이 아닌 값)이면 True 반환
print(all([1, 2, 3, 4]))
print(all([4, -2, 0.0, 4]))

# 그룹 자료형의 변수 x의 원소 중 하나라도 참이면 True 반환
print(any([1, 2, 3, 4]))
print(any([4, -2, 0.0, 4]))

# 아스키코드 값에 대한 문자 출력
print(chr(97))
print(chr(48))

# 문자에 대한 아스키코드 값 출력
print(ord('a'))
print(ord('0'))

# 객체 x가 가진 멤버 변수와 멤버 함수 보여주기
print(dir([1, 2, 3]))
print(dir({'1':'a'}))
print(dir(1))

print(int('3'))             # x를 정수 형태로 반환
print(str(3))               # x를 문자열 형태로 반환

# x를 리스트로 반환
print(tuple("Python"))
print(tuple([1, 2, 3]))

# x의 자료형을 반환
print(type("abc"))
print(type(a))

# 간단한 삽입형 함수 생성
sum = lambda a, b: a + b

print(sum(3,5))

# 최대, 최소값 반환
print(max([1, 4, 2, 8, 6]))
print(max("Python"))

print(min([1, 4, 2, 8, 6]))
print(min("Python"))

# x의 y제곱 결과값 반환
print(pow(2, 4))

c = input("값을 입력해주세요:")
print(c)

c = input("정수를 입력하세요:")
print(c)

print(range(5))
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10 ,2)))

for i in range(5, 20, 3):
    print(i)

len('Python')

print(sorted([3, 0, 2, 1]))
print(sorted('Python'))


import urllib.request
urllib.request.Request('http://www.sunmoon.ac.kr')

import pandas
pandas.DataFrame()

from datetime import datetime
datetime.now()

f = open('example.txt', 'w')
print(f)

f.close()

f = open('examlpe.txt', 'w')
for i in range(1, 6):
    data = '%d번째 줄입니다. \n' %i
    f.write(data)
f.close()

f = open('example.txt', 'w')
for i in range(6, 11):
    data = '%d번째 줄 추가입니다. \n' %i
    f.write(data)
f.close()

f = open('example.txt', 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()

f = open('example.txt', 'r')
lines = f.readlines()
print(lines)

for line in lines:
    print(line)

f.close()

f = open('exampel.txt', 'r')
data = f.read()
f.close()
data

with open('example.txt', 'w') as f:
    f.write("Now is better than never.")

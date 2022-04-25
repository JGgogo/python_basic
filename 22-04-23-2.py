# Chapter03-1
# 파이썬 완전 기초 
# 숫자형 

# 파이썬 지원 자료형 
"""
int : 정수
float : 실수
complex :  복소수
bool : 불린
str : 문자형(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dit : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'anaconda'
float = 10.0 #10(정수) =/= 10.0(실수) 기계입장에서는 다름
int = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learing",
    "version" : 2.0
}
tuple = (7, 8, 9)
set =  {1, 2, 3}
# 소가로 중가로 대가로에 따라 데이텨 형태가 바뀐다.
# 쓰다보면 익숙해 진다네 

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(dict))
print(type(int))
print(type(list))


# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) = x ** y x의 y제곱
"""

# 정수 선언

i = 77
i2 = -14
big_int = 77777777777777777777777777888686868

# 정수 출력

print(i)

print(i2)

print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.142592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습

i1 = 39
i2 = 393
big_int1 = 138457823947519
big_int2 = 23457092384570293847502
f1 = 1.234
f2 = 2.54

#+

print(">>>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2 )
print("big_int1 + big_int2 : ", big_int1 + big_int2)


#*

print(">>>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2 )
print("big_int1 * big_int2 : ", big_int1 * big_int2)

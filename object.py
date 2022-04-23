#다양한 변수 선언법
# 변수 네이밍 규칙 ! 
# 예약어
# Chater 02 - 2
# 파이썬 완전 기초 
# 파이썬 변수 

from tkinter import N

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) # 타입 ->int
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75

#재선언  // 재선언하면 덮어쓰이게 된다. 전에 값은 사라진다.
var = "Change value"

#출력
print(var)
print(type(var))
print()

# 큰 프로젝트는 변수 사전이 있다 / 작은건 내 머리속에 사전을 만들어 놔야 좋다

#Object References 
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))
print()

#예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n 
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 값이 같아지면 주소도 같아진다?? 
# 값이 같아지면 내부적으로 (인터프리터 자체에서)하나의 인스턴스로 할당해준다
# 값을 같다면 하나의 오브젝트로 설정을 해버린다.
#  이런것 하나하나 최적화를 시켜야만 빠른 프로그램이 될 수 있기 때문에
# 나중에 값을 바꿔주면 그때 되서 파이썬을 새로운 아이디를 할당한다.

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언 
# 네이밍 규칙을 가지고 변수를 선언해야한다
# camel case : numberOfCoLLegeGraduates 첫글자 소문자 이후 대문자
# -> Method
# pascal Case : NumberOfCollegeGraduates 첫글자 대문자 이후 대문자 
# -> Class
# Snake Case : number_of_college_graduates
#-> 파이썬에서 변수를 선언할 때
#  규칙을 지켜야 좋다... 작동은 되나 불문율

# 허용하는 변수 선언 법
age = 1
Age =2
aGe = 3 
AGE = 4
a_g_e =5

# 변수이름을 숫자, 특수문자로 시작하면 에러가 난다.


# 예약어는 변수명으로 불가능 
for = 3 # 에러가 난다 // class // google에 python reserve words 

"""
Python
Keywords	 	 	 
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""







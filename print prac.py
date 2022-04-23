# Chapter2-1
# 파이썬 온전 기초
# print 사용법
# 참조 파일 url

print('python')
print("python")
print('''python''') 
print("""python""")

print()

#separator 옵션 
print('p','y','t','o','n', sep="   ")




# end 옵션  end 안에 들어간 문자로 다음 프린트문과 이어준다\
# 줄을 계속 이어 쓸 수 있다.


print('wlcome to', end=" ")
print('IT news', end=' ')
print('web Site')



# file 옵션 #예약어 import 
import sys

print('learn Python', file=sys.stdout)



# format 사용(d, s, f)
# d 정수 s 문자열 f 실수 

print('%s %s' %("one",'two'))
print('{} {}'.format('one','two'))
print('{1},{0}'.format('one','two'))


# %s
print('%10s' % ('nice'))